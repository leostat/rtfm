#  what 
RTFM is a great and useful book, BUT a bit pointless when you have to transcribe it, so this little program will aim to be the spiritual successor to it.

I would recommend picking up a copy of the book from amazon, it is pretty handy to have!

# Usage 
```
Usage: rtfm.py [OPTIONS]

For when you just cant remember the syntax,  you should just RTFM

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -t TAG, --tag=TAG     Specify one or more tags to look for (a, b, c)
  -c CMD, --cmd=CMD     Specify a command to search (ls)
  -R REMARK, --remark=REMARK
                        Search the comments feilds
  -r REFER, --reference=REFER
                        Search for the reference [reference]
  -p PRINTER, --print=PRINTER
                        Print Types : P(retty) p(astable) w(iki) h(tml)
  -i INSERT, --insert=INSERT
                        Insert c(ommand) | t(ags) r(eferances)
  -D DUMP, --dump=DUMP  Just Dump infomration about
                        t(ags)|c(commands)|r(eferances)a(ll)
  -d, --debug           Display verbose processing details (default: False)
  -u, --update          Check for updates (default: false)
  -v                    Shows the current version number and the current DB
                        hash and exits (lies, it will do though)
  --delete				Delete a ID from the DB

Example: rtfm.py -c rtfm -t linux -R help -r git -pP -d
```
Its pretty much a simple search program, nothing to fancy, examples include:

Search for the command rtfm
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
Show us all windows commands with the term psexec
`./rtfm.py -t windows -c psexec`

Show us all the current tags
`./rtfm.py -D t`

Pull Updates to the DB
`./rtfm.py -u`
 * Note: Seems to be buggy on NFS shares 

The updates are 'safe' in the form they wont write over your DB, git pull is not a safe update

Add a tag to the CMD
`./rtfm.py -i t`


Insert commands into the db
`./rtfm.py -i c`

On all of these, I have tried to add 'debug' calls '-d'

There is also a number of output options, such as copy any paste, pretty, wiki and HTML:
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

```
# The TODO  list
 * Lots, this is an alpha so far
 * The 'important' functionality is present, but still lots of work to do

## Fixes:
 * Probabley should use prepared statements : local so dont care
 * Check for dupe tags
 * Warn on dupe tags
 * Re-jig the updater and the inserter

## Pipeline:
 * Create a HTML page 	      : H
 * create a WIKI format 	      : W
 * Drop to SQL Shell               : s
 * Template engine(autofill [user] : A user = innes, pass = password, attacker = 1.1.1.1, victim = 2.2.2.2
 * Make code more sane and betterize the layout

## Future:
 * Cool Thing mode
 * Fix the typos


# Credits 
The people that deserve the credits will be in the reference table of the DB. They are the ones doing the work!

# Thanks
Thanks in no particular order :) : 
@VC
@Rekzon
