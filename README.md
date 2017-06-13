#  What is it?
RTFM is a great and useful book, BUT a bit pointless when you have to transcribe it, so this little program will aim to be the spiritual successor to it.

I would recommend picking up a copy of the book from Amazon, it is pretty handy to have!

#Quick Start
 $ chmod +x rtfm.py
 $ ./rtfm.py -u
 $ ./rtfm.py -c 'rtfm'

# Usage 
```
$ rtfm.py -h
Usage: rtfm.py [OPTIONS]

For when you just cant remember the syntax,  you should just RTFM

Options:
  --version             show program's version number and exit
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
                        Search by date, usefull for when you want to commit
                        back!
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
Searching the DB is handled through the following switches: t, c, R, r, a and, A:

-c is search for a command:
```
./rtfm.py -c rtfm

++++++++++++++++++++++++++++++
Command ID : 0
Command    : RTFM

Comment    : helpception
Tags       : Linux
Date Added : 2017-01-30
++++++++++++++++++++++++++++++
```

-t is search for a tag, Tags can be shown through -Dt
```
rtfm.py -Dt
 | linux |  | bash |  | text manipulation |  | cisco |  | networking |  | loop |  | pivoting |  | files |  | passwords |  | enumeration |  | user information |  | interesting |  | scanning |  | hp |  | brute |  | http |  | web application |  | XSS |  | cookies |  | metasploit |  | certificates |  | stealth |  | smb |  | MitM |  | dns |  | package management |  | reverse shells |  | Windows |  | perl |  | python |  | php |  | ruby |  | sql injection |  | mysql |  | shell |  | mssql |  | Oracle |  | users |  | wireless |  | wifi |  | configuration |  | av evasion |  | powershell |  | memory |  | impacket |  | filesystem |  | IIS |  | process management |  | privilege escalation |  | remote command shell |  | hashes |  | recon |  | cracking |  | nessus |  | subnets |  | packet capture |  | reference |  | web address |  | java |  | solaris |  | forensics |  | ldap |  | Anti Virus |  | GIT |  | interesting  |  | Cloud |  | RDP |  | shells |  | encyption |  | test |  | a | 

./rtfm.py -t windows
```

-a is to search by author:
`./rtfm.py -a innes`

-A is 'Added on date', this can be one of yyyy-mm-dd, or now/today, most usefull for dumping out commands you have added to commit back to the git!
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

All of these can be combinded to create a very specfic search should you wish, shown here with debugging on:
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

RTFM implements a simple text file format to pull in updates to the database, these are shared VIA git, and implement a simple sha check to make sure they have not been corupt during download. The updates called by the command are 'safe' in the form they wont write over your DB, should you git pull, it probabley will overwrite your DB. If you are git cloning, you can move your database to '/etc/rtfm/snips.db' to protect your database file. 
```
./rtfm.py -u
[WARNING]: No DB, please run rtfm -u
[OK]: This may appear to hang. Run with debug to get more info
[OK]: Program version information :
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

	xx: Show update process
```

The update process also now drags in errata for the local DB allowing me a centralised way of neatly fixing the typos which have filtered into the DB. These are set through https://raw.githubusercontent.com/leostat/rtfm/master/updates/errata.txt. This allows things to be 'fixed' without needing to remove anything from the database.

# Inserting into the Database
Like all good cheatsheets it is possible to add your own content to the database. This is managed through the -i segment of the program. When adding commands you must add them with comments, references, and tags. Else at the moment, they will not be returned from the DB. Minor bug really. There are two main methods of adding commands to the database, Either in three steps adding all the commands you wish, Tag these commands up, then insert references. Or in one step, adding all commands, along with their tags and references. Most of the time you will be wanting to call -E:
```
$ rtfm.py -i E
Enter your command    : Command One
Enter you comment     : Comment One
Enter Author          : Author
Enter a tag (blank for end) : Tag
Enter a tag (blank for end) : 
Enter a reference (blank for end) : Reference
Enter a reference (blank for end) : 
[OK]: Added Rows :1
[OK]: Added a new tag and a tagmap
[OK]: Added a new Ref and a refmap
Enter your command    : ^C
```

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
# Deleteing content
This is simple enough, 'tis just using:
`rtfm.py --delete 1`

# Debugging
Througout the entire program, I have tried to add 'debug' calls '-d', these show you what the SQL is doing, what is being passed around.

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

# The TODO  list
 * The 'important' functionality is present, but still lots of work to do
 * Changes are happening on the DB, which means it may 'break' from time to time, just do a git pull to fix 
 
## Fixes:
 * Probabley should use prepared statements : local so dont care
 * Check for dupe tags
 * Warn on dupe tags

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
