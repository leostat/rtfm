#!/usr/bin/env python3
"""# Yay its now python3!
##
# Inspired by : https://xkcd.com/293/
# https://www.amazon.co.uk/Rtfm-Red-Team-Field-Manual/dp/1494295504
# Thanks for the Scaffolding Max!
##"""
import optparse
import urllib.request, urllib.parse, urllib.error
import hashlib
import sys
import sqlite3
import os.path
import signal

#########################################################################
# RTFM: Just Read the Friggin Manual
#########################################################################
#########################################################################
# Copyright: lololol
#########################################################################
__version__ = "1.0.1"
__prog__ = "rtfm"
__authors__ = ["See References: They are the real writers! Program by Alex Innes : 2017-2018"]

#########################################################################
## Fixes:
##  * Check for dupe tags
##  * Warn on dupe tags
##  * Drop whitespace from tags, allows a user to do things like webapp
##
## Pipeline:
##  * Create a HTML page 	      : H
##  * Template engine(autofill [user] : A user = innes, pass = password, attacker = 1.1.1.1, victim = 2.2.2.2
##  * Make code more sane and betterize the layout
##
## Future:
##  * Cool Thing mode
##  * Fix the typos
#########################################################################

#########################################################################
# Configuration
#########################################################################

EXIT_CODES = {
	"ok"	  : 0,
	"generic" : 1,
	"invalid" : 3,
	"missing" : 5,
	"limit"   : 7,
}


if os.name == 'nt':
	ANSI = {
	# TODO : make it look nice on windows
		"white" : '',
		"purple" : '',
		"blue" : '',
		"green" : '',
		"yellow" : '',
		"red" : '',
		"bold" : '',
		"reset" : ''
	}
else:
	ANSI = {
		"white" : '\033[37m',
		"purple" : '\033[95m',
		"blue" : '\033[94m',
		"green" : '\033[92m',
		"yellow" : '\033[93m',
		"red" : '\033[91m',
		"bold" : '\033[1m',
		"reset" : '\033[0m'
	}


#########################################################################
# Main program
#########################################################################

def run():
	sqlcmd = []
	sqltpl = []
	sqllst = []
	iok = ''
	if options.update:
		Updater(conn)
		iok = 1
	if options.insert != None:
		Insert(conn)
		iok = 1
	if options.SA != None:
		sqlcmd.append(" AND (c.cmd LIKE ? OR c.cmnt like ? or tc.tag LIKE ? OR c.author LIKE ?)")
		sqltpl.append("%"+options.SA+"%")
		sqltpl.append("%"+options.SA+"%")
		sqltpl.append("%"+options.SA+"%")
		sqltpl.append("%"+options.SA+"%")
		iok = 1
	if options.cmd != None:
		sqlcmd.append(" AND c.cmd LIKE ?")
		sqltpl.append("%"+options.cmd+"%")
		iok = 1
	if options.remark != None:
		sqlcmd.append(" AND c.cmnt LIKE ?")
		sqltpl.append("%"+options.remark+"%")
		iok = 1
	if options.author != None:
		sqlcmd.append(" AND c.author LIKE ?")
		sqltpl.append("%"+options.author+"%")
		iok = 1
	if options.date != None:
		if options.date == 'today' or options.date == 'now':
			sqlcmd.append(" AND c.date = date('now')")
			iok = 1
		else:
			sqlcmd.append(" AND c.date = ?")
			sqltpl.append(options.date)
			iok = 1
	if options.refer != None:
		for REF in options.refer.split(','):
			sqllst.append(' group_concat(rc.ref) like ? ')
			sqltpl.append("%"+REF+"%")
		iok = 1
	if options.tag != None:
		for TAG in options.tag.split(','):
			sqllst.append(' group_concat(tc.tag) like ? ')
			sqltpl.append("%"+TAG+"%")
		iok = 1
	if options.delete != None and options.delete.isdigit():
		cur = conn.cursor()
		sql = "DELETE FROM tblcommand WHERE cmdid = ?"
		debug(sql)
		cur.execute(sql, (options.delete,))
		ok("Deleted CMD "+str(options.delete))
		iok = 1
		conn.commit()
		sys.exit()
	if options.dump:
		Dump(conn)
		iok = 1
		sys.exit()
	if not iok:
		debug("http://www.youtube.com/watch?v=qRFhNZNu_xw")
		err("RTFM: rtfm -h OR rtfm.py -c ''")
	else:
		Search(conn, sqlcmd, sqltpl, sqllst)

####
# Functions
####
def Search(conn, sqlcmd, sqltpl, sqllst):
	cur = conn.cursor()
	sql = "SELECT c.cmdid, c.cmd, c.cmnt, c.date, c.author, group_concat(DISTINCT tc.tag), group_concat(DISTINCT ref)"
	sql += " FROM tblcommand c JOIN tbltagmap tm ON tm.cmdid = c.cmdid JOIN tbltagcontent tc ON "
	sql += " tc.tagid = tm.tagid JOIN tblrefmap rm ON rm.cmdid = c.cmdid"
	sql += " JOIN tblrefcontent rc on rc.id = rm.refid"
	sql += " ".join(sqlcmd)
	sql += " GROUP BY c.cmdid "
	if options.refer != None or options.tag != None:
		sql += ' HAVING '
		sql += 'AND'.join(sqllst)
	debug("S: "+sql)
	debug("W: "+str(sqltpl))
	cur.execute(sql, sqltpl)
	rows = cur.fetchall()
	debug("This Returned : "+str(rows))
	for cmd in rows:
		PrintThing(cmd)


def Updater(conn):
	ok("This may appear to hang. Run with debug to get more info")
	icmd = []
	itags = []
	irefs = []
	athing = []
	cur = conn.cursor()
	cur.execute("PRAGMA journal_mode = MEMORY")

	# First Check for Updates to the program
	version_info = 'https://raw.githubusercontent.com/leostat/rtfm/master/updates/version.txt'
	# version_info = 'http://127.0.0.1/version.txt'
	ok('Program version information :')
	req = urllib.request.urlopen(version_info)
	updates = req.read().splitlines()
	for line in updates:
		update = line.decode('utf8').split(',')
		if update[0] == __version__:
			ok("You are up to date :")
			print(update[0])
			print(update[1].replace('+','\n'))
			print(update[2])
			print(update[3])
			print("+++++++++++++++++++++++++++")
			break
		else:
			print(update[0])
			print(update[1].replace('+','\n'))
			print(update[2])
			print(update[3])
			print("+++++++++++++++++++++++++++")

	# Now update the DB
	uplist = 'https://raw.githubusercontent.com/leostat/rtfm/master/updates/updates.txt'
	req = urllib.request.urlopen(uplist)
	updates = req.read().decode('utf8').splitlines()
	for line in updates:
		update = line.split(",")
		debug("S : SELECT * from tblUpdates where hash like '"+update[1]+"'")
		cur.execute("SELECT * from tblUpdates where hash like ?", (update[1], ))
		row = cur.fetchall()
		if len(row) == 0:
			download = urllib.request.urlopen(update[2])
			downfile = download.read()
			hash = hashlib.sha1()
			hash.update(downfile)
			if update[1] == hash.hexdigest():
				skipc = skipt = 0
				for cmdline in downfile.decode('utf8').splitlines():
					if (cmdline not in ('EOC', '')) and skipc == 0:
						icmd.append(cmdline)
						continue
					elif skipc == 0:
						skipc = 1
						continue
					if (cmdline not in ('EOT', '')) and skipt == 0:
						itags.append(cmdline)
						continue
					elif skipt == 0:
						skipt = 1
						continue
					if cmdline not in ('EOR', ''):
						irefs.append(cmdline)
					else:
						skipc = skipt = 0
						debug("Command : "+str(icmd))
						debug("Tags : "+str(itags))
						debug("References : "+str(irefs))
						newid = dbInsertCmdS(conn, icmd)
						dbInsertTags(conn, itags, newid)
						dbInsertRefs(conn, irefs, newid)
						icmd = []
						itags = []
						irefs = []
						continue
			else:
				warn("Warning SHA1 mis-match : Ignoring this one for now")
				continue
			ok("Hopefully added lots of new commands")
			debug("I: INSERT INTO tblupdates values (NULL, "+update[1]+", "+update[2]+", date('now')")
			cur.execute("INSERT INTO tblupdates values (NULL, ?, ?, date('now'))", (update[1], update[2]))
			conn.commit()
		else:
			debug("XXX Skipping Update : "+update[1])
		ok("Parsed Line of update")
	# This function checks for typo fixes to the DB
	# XXX Late night hack, probabley a better way of doing this!, seems super innefficent
	erlist = 'https://raw.githubusercontent.com/leostat/rtfm/master/updates/errata.txt'
	# erlist= 'http://127.0.0.1/errata.txt'
	req = urllib.request.urlopen(erlist)
	updates = req.read().decode('utf8').splitlines()
	debug(str(updates))
	for line in updates:
		update = line.split(",")
		debug("S : SELECT * from tblUpdates where hash like '"+update[1]+"'")
		cur.execute("SELECT * from tblUpdates where hash like ?", (update[1], ))
		row = cur.fetchall()
		if len(row) == 0:
			download = urllib.request.urlopen(update[2])
			downfile = download.read()
			hash = hashlib.sha1()
			hash.update(downfile)
			if update[1] == hash.hexdigest():
				skipa = skipt = skipr = hack = conts = 0
				sql = ""
				for cmdline in downfile.decode('utf8').splitlines():
					if (conts == 1) and (cmdline != "EOU"):
						conts = 0
						athing.append(cmdline)
						continue
					if (cmdline in ('tblcommand', 'tbltagcontent', 'tblrefcontent')) and skipt == 0:
						non_prep_table = cmdline
						skipt = 1
						continue
					elif skipt == 0:
						err("Typo in Errata : Aborting")
					if (cmdline not in ('EOA', '')) and skipa == 0:
						non_prep_row = cmdline
						continue
					elif skipa == 0:
						skipa = 1
						continue
					if not skipr:
						athing.append(cmdline)
						skipr = 1
						continue
					if (cmdline != "EOU") and cmdline in ('cmd','cmnt','author','tag','ref'):
						sql+=" AND "+cmdline+" LIKE ? "
						conts = 1
						continue
					if cmdline == "EOU":
						text="S : UPDATE '"+non_prep_table+"' SET '"+non_prep_row+"' = '"+athing[0]+"' WHERE 1"+sql
						debug(text)
						debug(str(athing))
						sql_string="UPDATE '"+non_prep_table+"' SET '"+non_prep_row+"' = ? WHERE 1 "+sql
						cur.execute(sql_string, (athing))
						athing = []
						sql = ""
						hack = skipr = skipa = skipt = conts = 0
			else:
				warn("Warning SHA1 mis-match : Ignoring this one for now")
				continue
			ok("Hopefully fixed lots of commands")
			debug("I: INSERT INTO tblupdates values (NULL, "+update[1]+", "+update[2]+", date('now')")
			cur.execute("INSERT INTO tblupdates values (NULL, ?, ?, date('now'))", (update[1], update[2]))
			conn.commit()
	ok("Update complete")
	exit()

def dbInsertTags(conn, tags, cmdid):
	cur = conn.cursor()
	for tag in tags:
		debug("S : SELECT tagid from tbltagcontent where tag like '"+tag+"'")
		cur.execute("SELECT Tagid FROM Tbltagcontent where tag like ?", (tag, ))
		count = cur.fetchall()
		if len(count) > 1:
			err("More than one tag returned! "+str(count))
		elif len(count) == 1:
			debug("Tag found : "+str(count[0][0]))
			debug("I: INSERT INTO tbltagmap values ("+str(count[0][0])+", "+str(cmdid)+")")
			cur.execute("INSERT INTO tbltagmap values (NULL, ?, ?)", (str(count[0][0]), str(cmdid)))
			conn.commit()
			ok("Added tags")
		elif len(count) == 0:
			debug("Tag not found in DB")
			debug("I: INSERT INTO tbltagcontent VALUES (NULL, '"+tag+"')")
			cur.execute("INSERT INTO tbltagcontent values (NULL, ?)", (tag, ))
			debug("We have added Tag : "+str(cur.lastrowid))
			debug("I: INSERT INTO tbltagmap values ("+str(cur.lastrowid)+", "+str(cmdid)+")")
			cur.execute("INSERT INTO tbltagmap values (NULL, ?, ?)", (cur.lastrowid, cmdid))
			conn.commit()
			ok("Added a new tag and a tagmap")
		else:
			err("I dont know how you even got here,  https://www.youtube.com/watch?v = dQw4w9WgXcQ")

def dbInsertRefs(conn, refs, cmdid):
	cur = conn.cursor()
	for ref in refs:
		debug("S : SELECT id from tblrefcontent where ref like '"+ref+"'")
		cur.execute("SELECT id FROM Tblrefcontent where ref like ?", (ref, ))
		count = cur.fetchall()
		if len(count) > 1:
			err("More than one ref returned! "+str(count))
		elif len(count) == 1:
			debug("Ref found : "+str(count[0][0]))
			debug("I: INSERT INTO tblrefmap values ("+str(count[0][0])+", "+str(cmdid)+")")
			cur.execute("INSERT INTO tblrefmap values (NULL, ?, ?)", (str(count[0][0]), str(cmdid)))
			conn.commit()
			ok("Added Refs")
		elif len(count) == 0:
			debug("ref not found in DB")
			debug("I: INSERT INTO tblrefcontent VALUES (NULL, '"+ref+"')")
			cur.execute("INSERT INTO tblrefcontent values (NULL, ?)", (ref, ))
			debug("We have added Ref : "+str(cur.lastrowid))
			debug("I: INSERT INTO tblrefmap values ("+str(cur.lastrowid)+", "+str(cmdid)+")")
			cur.execute("INSERT INTO tblrefmap values (NULL, ?, ?)", (cur.lastrowid, cmdid))
			conn.commit()
			ok("Added a new Ref and a refmap")
		else:
			err("I dont know how you even got here,  https://www.youtube.com/watch?v = dQw4w9WgXcQ")

def dbInsertCmdS(conn, cmd):
	cur = conn.cursor()
	if options.debug:
		debug("CMD : "+str(cmd))
		debug("I: INSERT INTO tblcommand VALUES (NULL, '"+str(cmd[0])+"', '"+str(cmd[1])+ \
			 "', " +str(cmd[2])+"', "+"date('now'))")
	cur.execute("""INSERT INTO tblcommand VALUES (NULL, ?, ?, ?, date("now"));""", cmd)
	conn.commit()
	ok("Added Rows :"+str(cur.rowcount))
	return cur.lastrowid

def dbInsertCmd(conn, cmds):
	cur = conn.cursor()
	cur.execute("SELECT max(cmdid) from tblcommand")
	max_id = cur.fetchall()
	if options.debug:
		for cmd in cmds:
			debug("I: INSERT INTO tblcommand VALUES (NULL, '"+str(cmd[0])+"', '"+str(cmd[1]) \
				+"', '"+str(cmd[2])+"', "+"date('now'))")
	cur.executemany('INSERT INTO tblcommand VALUES (NULL, ?, ?, ?, date("now"));', cmds)
	conn.commit()
	ok("Added Rows : " + str(cur.rowcount))
	cur.execute("SELECT max(cmdid) FROM tblcommand")
	new_max_id = cur.fetchall()
	ok("New Top ID : " + str(new_max_id[0][0]) + " | Number of CMD's Added : " \
		+ str(new_max_id[0][0]-max_id[0][0]))


def Insert(conn):
	if options.insert == 't':
		tags = []
		tag = 'EasterEgg'
		cmdid = input("What CMD are we adding tags too? : ")
		while tag != '':
			tag = input("Enter a tag (blank for none) : ")
			if tag != '':
				tags.append(tag)
		if (tags == []) or (cmdid == '') or (not cmdid.isdigit()):
			err("No,  Just why  : "+str(cmdid)+" : "+str(tags))
		dbInsertTags(conn, tags, cmdid)
	elif options.insert == 'c':
		cmds = []
		cmd = 'wget http://'
		while not (cmd == '' or cmd == 'EOC'):
			cmd = input("Enter your command    : ")
			cmt = input("Enter your comment     : ")
			author = input("Enter Author          : ")
			if cmd not in ('', 'EOC'):
				cmds.append((cmd, cmt, author))
		dbInsertCmd(conn, cmds)
		exit()
	elif options.insert == 'r':
		refs = []
		ref = 'http://necurity.co.uk'
		cmdid = input("What CmdID are we adding refs to? : ")
		while ref != '':
			ref = input("Enter a reference (blank for none) : ")
			if ref != '':
				refs.append(ref)
		if (refs == []) or (cmdid == '') or (not cmdid.isdigit()):
			err("No,  Just why  : "+str(cmdid)+" : "+str(refs))
		dbInsertRefs(conn, refs, cmdid)
	elif options.insert == "ta":
		cur = conn.cursor()
		ok("This tags everything without tags,  mainly for DB init")
		ok("Enter blank line to commit changes")
		toTag = []
		debug("S : SELECT CmdID, cmd, cmnt FROM tblcommand")
		cur.execute("SELECT CmdID, cmd, cmnt FROM tblcommand")
		cmds = cur.fetchall()
		debug("This Returned : "+str(cmds))
		for cmd in cmds:
			debug("S : SELECT tagid FROM tbltagmap WHERE cmdid = "+str(cmd[0]))
			cur.execute("SELECT tagid FROM tbltagmap WHERE cmdid = "+str(cmd[0]))
			TagCount = cur.fetchall()
			if TagCount == []:
				toTag.append(cmd)
		debug("Count : "+str(len(toTag))+"\nTagging : "+str(toTag))
		counter = len(toTag)
		for cmd in toTag:
			counter = counter-1
			tag = 'Easter Egg'
			tags = []
			warn("Number left :"+str(counter))
			ok("Command ID : "+str(cmd[0]))
			ok("		Command    : "+str(cmd[1]))
			ok("		Comment    : "+str(cmd[2]))
			ok("v These are known tags")
			options.dump = 't'
			Dump(conn)
			print(" == == ONE TAG A LINE == == \n")
			while tag != '':
				tag = input("Enter a tag (blank for none) : ")
				if tag != '':
					tags.append(tag)
				if (tags == []) or (cmd == ''):
					err("No,  Just why  : "+str(cmd)+" : "+str(tags))
			dbInsertTags(conn, tags, cmd[0])
	elif options.insert == 'E':
		cmd = 'while true; do sl; done'
		while cmd != '':
			icmd = []
			itags = []
			irefs = []
			cmd = input("Enter your command    : ")
			cmt = input("Enter your comment     : ")
			author = input("Enter Author          : ")
			if cmd not in ('', 'EOC'):
				icmd.extend((cmd, cmt, author))
			tag = 'EasterEgg'
			while tag != '':
				tag = input("Enter a tag (blank for end) : ")
				if tag != '':
					itags.append(tag)
			if len(itags) == 0:
				err("No,  All parts required for E")
			ref = 'https://lg.lc'
			while ref != '':
				ref = input("Enter a reference (blank for end) : ")
				if ref != '':
					irefs.append(ref)
			if len(irefs) == 0:
				err("No,  All parts required for E")
			debug("Command : "+str(icmd))
			debug("Tags : "+str(itags))
			debug("References : "+str(irefs))
			newid = dbInsertCmdS(conn, icmd)
			dbInsertTags(conn, itags, newid)
			dbInsertRefs(conn, irefs, newid)
	else:
		err("RTFM : rtfh.py -h")
	exit()

def Dump(conn):
	cur = conn.cursor()
	if options.dump == 'a':
		debug("S : SELECT * FROM Tblcommand")
		cur.execute("SELECT * FROM Tblcommand")
		rows = cur.fetchall()
		for cmd in rows:
			debug(str(cmd[0]))
			print(cmd[1])
			print(cmd[2])
			print('EOC')
			tags = AsocTags(cur, cmd)
			ltags = tags[-1].split("| ")
			for tag in ltags:
				if tag != '':
					print(tag)
			print('EOT')
			refs = AsocRefs(cur, cmd)
			lrefs = refs[-1].split("| ")
			for ref in lrefs:
				if ref != '':
					print(ref)
			print('EOR')
		ok('Dumped all in update format. Why,  you stealing things?')
	elif options.dump == 'c':
		debug("Running Comand : SELECT * FROM Tblcommand")
		cur.execute("SELECT * FROM Tblcommand")
		rows = cur.fetchall()
		for cmd in rows:
			print(cmd[1])
			print(cmd[2])
			print('EOC')
	elif options.dump == 't':
		debug("Running Comand : SELECT tag FROM Tbltagcontent")
		cur.execute("SELECT Tag FROM Tbltagcontent")
		rows = cur.fetchall()
		for row in rows:
			sys.stdout.write(str(" | "+row[0])+" | ")
		sys.stdout.flush()
		print()
	elif options.dump == 'r':
		debug("Running Comand : SELECT ref FROM Tblrefcontent")
		cur.execute("SELECT ref FROM Tblrefcontent")
		rows = cur.fetchall()
		for row in rows:
			print(row[0])
		print('EOR')
	else:
		err("RTFM: rtfm -h")

def PrintThing(ret_cmd):
	if not options.printer:
		print("++++++++++++++++++++++++++++++")
		print("Command ID : "+str(ret_cmd[0]))
		print("Command    : "+str(ret_cmd[1])+'\n')
		print("Comment    : "+str(ret_cmd[2]))
		print("Tags       : "+str(ret_cmd[5]))
		print("Date Added : "+str(ret_cmd[3]))
		print("Added By   : "+str(ret_cmd[4]))
		print("References\n__________\n"+str(ret_cmd[6].replace(',', '\n')))
		print("++++++++++++++++++++++++++++++\n")
	elif options.printer == 'c':
		print(str(ret_cmd[1]))
	elif options.printer == 'p':
		print("++++++++++++++++++++++++++++++")
		print(str(ret_cmd[1])+'\n')
		print(str(ret_cmd[2]))
		print("++++++++++++++++++++++++++++++\n")
	elif options.printer == 'd':
		print(str(ret_cmd[1]))
		print(str(ret_cmd[2]))
		print(str(ret_cmd[4]))
		print('EOC')
		print(str(ret_cmd[5].replace(',', '\n')))
		print('EOT')
		print(str(ret_cmd[6].replace(',', '\n')))
		print('EOR')
	elif options.printer == 'w':
		print("= "+str(ret_cmd[2])+" = ")
		print(" "+str(ret_cmd[1]))
		print(str(ret_cmd[5].replace(',', ', ')))
		print(str(ret_cmd[6].replace(',', '\n')))
	elif options.printer == 'P':
		table_data = [\
			["Added By " + str(ret_cmd[4]), "Cmd ID : " + str(ret_cmd[0])],
			["Command ", str(ret_cmd[1])],
			["Comment  ", str(ret_cmd[2])],
			["Tags  ", str(ret_cmd[5]).replace(',', '\n')],
			["Date added", str(ret_cmd[3])],
			["References", str(ret_cmd[6]).replace(',', '\n')]\
			]
		table = AsciiTable(table_data)
		max_width = table.column_max_width(1)
		wrapped_string = '\n'.join(wrap(str(ret_cmd[1]), max_width))+"\n"
		table.table_data[1][1] = wrapped_string
		print(table.table)
	else:
		err("Please seek help")


def RefMapper(cur, refids):
	# XXX probabley shoud just be an if for ref or tag
	if len(refids) == 1:
		debug("S : SELECT Ref from tblrefcontent where id  = "+str(refids[0][0]))
		cur.execute("SELECT Ref from tblrefcontent where id = ?", refids[0])
		text = cur.fetchall()
		return text[0][0]
	elif len(refids) > 1:
		# TODO : Yeh i know this == bad,  but I will get round making it better at some point
		# AKA Yeh deal with it will probabley be here until the end of time
		sql = "SELECT ref FROM tblrefcontent where id = -1 "
		for refid in refids:
			sql += " OR id = "+str(refid[0])
		debug("S : "+sql)
		cur.execute(sql)
		textlist = cur.fetchall()
		text = ''
		for item in textlist:
			text += item[0]+"\n"
		return text
	else:
		return "xXx ! No Refs for this ! xXx "

def TagMapper(cur, tagids):
	if len(tagids) == 1:
		debug("S : SELECT tag from tbltagcontent where tagid  = "+str(tagids[0][0]))
		cur.execute("SELECT tag from tbltagcontent where tagid = ?", tagids[0])
		text = cur.fetchall()
		return text[0][0]
	elif len(tagids) > 1:
		# TODO : Yeh i know this == bad,  but I will get round making it better at some point
		# AKA Yeh deal with it will probabley be here until the end of time
		sql = "SELECT tag FROM tbltagcontent where tagid = -1 "
		for tagid in tagids:
			sql += " OR tagid = "+str(tagid[0])
		debug("S : "+sql)
		cur.execute(sql)
		textlist = cur.fetchall()
		text = ''
		for item in textlist:
			text += "| "+item[0]+" "
		return text
	else:
		return "xXx ! No tags for this ! xXx "

def AsocTags(cur, cmd):
	debug("S : SELECT TagID FROM tbltagmap WHERE cmdid = " + str(cmd[0]))
	cur.execute("SELECT TagID FROM tbltagmap WHERE cmdid = " + str(cmd[0]))
	RetTagIds = cur.fetchall()
	debug("This returned : " + str(RetTagIds) + " Len : " + str(len(RetTagIds)))
	Tags = TagMapper(cur, RetTagIds)
	l = list(cmd)
	l.append(Tags)
	cmd2 = tuple(l)
	return cmd2

def AsocRefs(cur, cmd):
	debug("S : SELECT RefID FROM TblRefMap WHERE cmdid = "+str(cmd[0]))
	cur.execute("SELECT RefID FROM tblrefmap WHERE cmdid = "+str(cmd[0]))
	RetRefIds = cur.fetchall()
	debug("This returned : "+str(RetRefIds)+" Len : "+str(len(RetRefIds)))
	Tags = RefMapper(cur, RetRefIds)
	l = list(cmd)
	l.append(Tags)
	cmd = tuple(l)
	return cmd


#########################################################################
# Helper Functions
#########################################################################

def debug(msg, override=False):
	if options.debug or override:
		print(ANSI["purple"] + ANSI["bold"] + "[DEBUG]: " + ANSI["reset"] + msg)

def ok(msg):
	print(ANSI["green"] + ANSI["bold"] + "[OK]: " + ANSI["reset"] + msg)

def warn(msg):
	msg = ANSI["yellow"] + ANSI["bold"] + "[WARNING]: " + ANSI["reset"] + msg + "\n"
	sys.stderr.write(msg)

def err(msg, level="generic"):
	if level.lower() not in EXIT_CODES:
		level = "generic"
	msg = ANSI["red"] + ANSI["bold"] + "[ERROR]: " + \
		ANSI["reset"] + msg + "\n"
	sys.stderr.write(msg)
	sys.exit(EXIT_CODES[level])


#########################################################################
# Starting point
#########################################################################
try:
	from terminaltables import AsciiTable
	from textwrap import wrap
except:
	warn("Unable to have pretty output,  Please 'pip install terminaltables' or remove these lines :)")

if __name__ == "__main__":
	if os.path.exists(os.path.dirname(os.path.realpath(sys.argv[0]))+'/snips.db'):
		conn = sqlite3.connect(os.path.dirname(os.path.realpath(sys.argv[0]))+'/snips.db')
		conn.text_factory = str
	elif os.path.exists('/etc/rtfm/snips.db'):
		conn = sqlite3.connect('/etc/rtfm/snips.db')
		conn.text_factory = str
	else:
		try:
			warn("Cant access the DB, creating a new one in the run path")
			conn = sqlite3.connect(os.path.dirname(os.path.realpath(sys.argv[0]))+'/snips.db')
			conn.text_factory = str
			cur = conn.cursor()
			f = open(os.path.dirname(os.path.realpath(sys.argv[0]))+'/clean.sql','r')
			sql_db = f.read()
			cur.executescript(sql_db)
		except:
			err("Can not access a DB and can not create the file, giving up :'( ")
	cur = conn.cursor()
	sql = "SELECT hash,URL FROM TblUpdates"
	cur.execute(sql)
	dbsversion = cur.fetchall()
	if not dbsversion:
		print(ANSI["yellow"] + ANSI["bold"] + "[WARNING]: " + ANSI["reset"] + "No DB, please run rtfm -u")
	parser = optparse.OptionParser(\
		usage="Usage: %prog [OPTIONS]",
		version="%s: v%s (%s) \nDB updates installed (Hash:URL) :\n %s" % (__prog__, __version__, \
			','.join(__authors__), '\n '.join(map(str, dbsversion))),
		description="For when you just cant remember the syntax,  you should just RTFM",
		epilog="Example: rtfm.py -c rtfm -t linux -R help -r git -pP -d")

	parser.add_option("--delete", action="store", dest="delete",\
		help="Delete specified ID")

	parser.add_option("-e", "--everything", action="store", dest="SA",\
		help="Look through all of RTFM")

	parser.add_option("-t", "--tag", action="store", dest="tag",\
		help="Specify one or more tags to look for (a, b, c)")

	parser.add_option("-c", "--cmd", action="store", dest="cmd",\
		help="Specify a command to search (ls)")

	parser.add_option('-R', '--remark', action='store', dest="remark",\
		help="Search the comments field")

	parser.add_option('-r', '--reference', action='store', dest="refer",\
		help="Search for the reference [reference]")

	parser.add_option('-a', '--author', action='store', dest="author",\
		help="Search for author")

	parser.add_option('-A', '--added-on', action='store', dest="date",\
		help="Search by date, useful for when you want to commit back!")

	parser.add_option('-p', '--print', action='store', dest="printer",\
		help="Print Types : P(retty) p(astable) w(iki) h(tml) d(ump)")

	parser.add_option('-i', '--insert', action='store', dest="insert",\
		help="Insert c(ommand) | t(ags) | r(eferances) | E(verything)")

	parser.add_option('-D', '--dump', action='store', dest="dump",\
		help="Just Dump information about t(ags)|c(commands)|r(eferances)a(ll)")

	parser.add_option('-d', '--debug', action='store_true', dest="debug",\
		help='Display verbose processing details (default: False)')

	parser.add_option('-u', '--update', action='store_true', dest="update",\
		help='Check for updates (default: false)')

	parser.add_option('-v', action='version',\
		help="Shows the current version number and the current DB hash and exits")

	(options, args) = parser.parse_args()

	try:
		debug("Options Set: "+str(options))
		run()
	except KeyboardInterrupt:
		print("\n\nCancelled.")
		sys.exit(0)
