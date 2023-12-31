# Kraken, wrestling Microsoft Access into open source

## TL;DR overview of Kraken

Kraken makes [Microsoft Access](https://en.wikipedia.org/wiki/Microsoft_Access) repeatable,
using plain ASCII text files. This means that someone you have never met can clone your
Git repository containing text files, and run Kraken to create an application in their 
copy of Microsoft Access. They will see the same program, database and user interface
you developed, even though Access does not support dump/restore from text files, and generally
prevents anything that would help users move away from Access.

Kraken is an essential first step to replacing Access with an open source solution.

## More detailed overview

Microsoft Access is an obsolete visual application builder tool, still used
fairly widely because many organisations rely on legacy Access applications.
First released more than 30 years ago, Access was not designed for a modern
multiuser world with software source code maintained in Git, and networked
SQL databases, or even the internet. Legacy Access applications are increasingly
difficult to maintain.

Ideally Access applications would be translated to some other open source
system that does not rely on Access, or Micosoft Windows, or any Microsoft
products at all. This is a problem that many other people have tried to fix,
so we broke it down.

Instead of a single-user untrackable GUI point-and-click development
environment, Kraken turns Access applications into [diffable](https://en.wiktionary.org/wiki/diffable) 
plain text files that can be stored in Git, and put online using services such as
[SourceHut](https://sr.ht), [Codeberg](https://codeberg.org) or [GitHub](https://github.com).

After the files are retrieved from the Git service using a command such as ```git pull```, kraken
can then be used to load them into Microsoft Access, forming a complete GUI application in the
normal Access way. Microsoft Access and Microsoft Windows are still needed to run the source code,
but we can now see what needs to be done to remove this dependency.

But for now, we have solved the important step of making Access development repeatable,
using standard development tools.

# Technical overview

kraken is a Python 3 program to dump the contents of a Microsoft Access
database program to diffable plain text. An Access application (often confusingly
called an "Access Database") is made of these components:

* data in an SQL database, accessible by rows and columns using the SQL language
* graphical forms created with a GUI form builder, containing buttons and other GUI objects
* source code written in [Visual Basic for Applications](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications). The source code can be linked to any object within an Access form, for example to be executed when a button is clicked
* SQL queries that are used to extract data from the database
* Other object types such as macros, which we do not use. We have not tested dumping them from Access, however we look forward to hearing how other people get on who do use these objects

Once kraken is installed and running, the Access application workflow can look like this:

1. Make a change to an Access application within Microsoft Access
2. Outside Access, in a directory under Git control, run ```kraken``` with some commandline paramers to dump the context of a database to plain text. Run the command ```git diff``` to verify that changes have been made that you expect.
3. Run ```git commit -a``` and write a log message
4. Run ```git push```

Anyone else who can see the Git repository, for example on
[GitHub](https://github.com/), [CodeBerg](https://codeberg.com/) or [SourceHut](https://sr.ht/), can then do a
```git clone``` followed by ```kraken push``` and then a new Access
application is created locally for the user.

---

# Installation

You will need to [install Python 3 for Windows](https://docs.python.org/3/using/windows.html#installation-steps).
If you do this successfully, you should be able to type ```python``` at the Windows CMD command prompt. We have only 
tested on Python version 3.12.0, but would expect higher versions to work. We know that versions 3.11.x do not work.

At the Windows CMD prompt, use the ```pip``` command to install the kraken pre-requisites.

```shell
python -m pip install -r requirements.txt
```

---

## Using Kraken

### Basic usage

```shell
python src/kraken.py [action] ... [database] [export]
```

database: Path to an Access (.accdb) file  
export:   Path to where you want kraken to export/pull files from  
action:   Pick from this list:  

Pull from Access/Push to Access, all data types (ie the full Access application)

- pull
- push

Dump induvidual items

- dump-form <form_name>
- dump-module <module_name>
- dump-query <query_name>
- dump-table <table_name>
- dump-schema

Dump all of a category

- dump-forms
- dump-modules
- dump-queries
- dump-tables

Load back into access

- load-form <form_name> (Note it is the name of the form found inside `<export>/forms/`)
- load-csvs <csvs_directory>
- load-tables
- load-queries
- load-forms

### Additional Tools

Kraken has multiple additional tools located inside `src/tools/`

#### conv_utf16-ascii.py

Used to convert the UTF16 files which Access uses for forms and turns them into 8-bit ASCII. 

Usage: `python conv_utf16-ascii.py <Path to file/directory of files>`

#### strip_guids.py

Strips the GUIDs from an exported form. We don't know why Access generates different
GUIDs every time, but they prevent diffing forms and so we need to remove them. Access
does not seem to mind.

Usage: `python strip_guids.py <Path to file/directory of files>`

#### gen_docs.py

Generates documentation the functions implemented by Access's COM object. It will write this to `doc.txt`.

Usage: `python gen_docs.py`

---

## Background

Here is a list of facts, rather than a coherent story. No doubt people familiar
with the history of computing can improve the following, and we would love to
hear from you.

- Microsoft Access is more than 30 years old, and it is still present in quite a lot of
companies around the world. It is (even now) quite a good protoyping tool for
form-based GUI applications, which describes most business apps.
Microsoft have tried to kill the Access product off multiple times, but there are large
Microsoft customers who are so dependent on Access applications that they ask for
to still be maintained. This means that while Access still works, Microsoft have not
improved it for many years.

- Access can work with remote SQL databases (using ODBC), but it is a
Windows-only desktop app which is often very memory hungry, has lots of quirks and bugs,
and is completely unsuitable for use in the 21st century. Even by non-programmers,
who are often the people that start writing Access apps which then go on to become vital to an
organisation.

- Microsoft also made Access very hard to migrate away from. There is a lot
that is not documented. The BASIC programming language is VBA, not .NET basic,
meaning there are no other implementations of it. There is an "Export" feature
that produces plain text files, but it doesn't export everything that makes up
an Access application.

- Many many companies have spent money migrating away from Access applications. One 
common approach is to ignore the Access app except as a visual prototype.
There is no automated migration tool or technique that works for everyone, and nothing
at all which is open source.

- There are good things to say about Access applications, starting with longevity.
Access code written decades ago still runs just as well today, while most web
front-end code in javascript/Node/etc needs to be rewritten every 2-3 years. Whatever
we choose to replace Access with in future, it needs to be designed to last a very long
time.
