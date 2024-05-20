# Kraken, wrestling Microsoft Access into the 21st century

Kraken is a Python script to to convert your entire obsolete/legacy 
[Microsoft Access](https://en.wikipedia.org/wiki/Microsoft_Access) application
to [diffable](https://en.wiktionary.org/wiki/diffable) plain text files, and back again.
Access stores its applications in an undocumented binary format, so this is new, unique and
essential for organisations migrating important applications away from Access.

# Table of contents

* [Introduction ](#introduction-)
* [Important project information](#important-project-information)
* [Overview of Kraken](#overview-of-kraken)
* [Alternative solutions](#alternative-solutions)
* [More detailed overview](#more-detailed-overview)
* [Technical overview](#technical-overview)
* [Installation](#installation)
* [Using Kraken](#using-kraken)
    * [Basic usage](#basic-usage)
    * [Additional Tools](#additional-tools)
        * [conv_utf16-ascii.py](#conv_utf16-ascii.py)
        * [strip_guids.py](#strip_guids.py)
        * [gen_docs.py](#gen_docs.py)
* [Relevant Computing History Background](#relevant-computing-history-background)


# Introduction - why Kraken?

Kraken is useful because:

* plain text files can be managed in a version control system, such as [Git](https://git-scm.com) or [Fossil](https://fossil-scm.org), as used by services like [Codeberg](https://codeberg.org) and [GitHub](https://github.com).
* text files are easy to back up and verify in detail. An Access program/database is one big binary blob, you can back it up but have no way to verify the integrity of that backup
* Access scatters programmatic objects in many places. If you want (for example) just the SQL queries or just the visual forms, Kraken puts them in one place. Who knows what you might discover?
* Access is poorly suited to documenting how a program works. With Kraken, you can tie documentation (eg Markdown files) stored outside Access to the programmable objects inside Access
* text files are a good place to start if you want to migrate code away from Windows. Kraken is an excellent first step to open sourcing legacy Access code.

If you have Access Databases/programs you wish to store in Git, then we invite you to try Kraken. 
[Raise an issue to tell us](https://github.com/Spyderisk/Access-Tool/issues/new) if you have a problem, or just 
want to say it is working great for you.

One day, we plan to write a parser for Access
application and processes it so it can be run using open source tools on Linux.

Kraken is [licensed under generous terms](./LICENSE.md).

# Important project information

Kraken was created by the [Spyderisk Contributors](./CONTRIBUTORS.md) to handle a legacy
Access application to handle
[complicated mathematical relationships](https://github.com/Spyderisk/domain-network/tree/6a/csv)
for the [Spyderisk project](https://github.com/Spyderisk). When Spyderisk was open sourced 
in 2023 Access had to be replaced, and Kraken is how we are doing it.

Kraken is available under [Open Source terms](./LICENSE.md). Everyone is welcome, noting
our [basic rules of decent behaviour](./CODE-OF-CONDUCT.md),
which includes contact details if you want to report a behaviour problem.

We try to make it easy to [contribute to Kraken](./CONTRIBUTING.md) whatever your skills.

You can contact us by:
* [raising a GitHub Issue](https://github.com/Spyderisk/Access-tool/issues/new)
* emailing [team@spyderisk.org](mailto://team@spyderisk.org)

# Overview of Kraken

Kraken makes Microsoft Access code repeatable, using plain ASCII (really UTF-8) text files.
This means that someone can find your Access code online (say on GitHub) and then:

* clone the Git repository containing your code in text files, onto their Windows computer
* run Kraken on their Windows computer, which imports these text files into their copy of Microsoft Access to re-create your application.

They will see the same program, database and user interface you developed, but
they only had access to the code on GitHub. They have *repeated* your program
independently, which has not previously been possible.

Kraken will not:

* replace your Access app with open source. You still need Windows and Access.
* create or know anything about a .accdb file
* work without Python
* run on Linux/Unix

# Alternative solutions

Other people have worked on this problem, with different requirements:
* Santiago Bragagnolo [wrote a paper with source code](https://link.springer.com/chapter/10.1007/978-3-030-64694-3_10)
demonstrating one of the main techniques used in Kraken. Santiago's [Smalltalk](https://pharo.org/) code is 
[available on GitHub](https://github.com/impetuosa/jindao). Santiago is solving a different problem but our techniques overlap.
* Adam Waller maintains [a code module for Microsoft Access](https://github.com/joyfullservice/msaccess-vcs-addin) that will export 
and import from multiple source control systems including Git. Adam's solution is for people who want to stay within the Access/Windows world,
but merely want to add revision control and collaboration to Access. In contrast, Kraken works in Python outside Access, and Access knows
nothing about it.

# More detailed overview

Microsoft Access is an obsolete visual application builder tool, still used
fairly widely because many organisations rely on legacy Access applications.
First released more than 30 years ago, Access was not designed for a modern
multiuser world where software source code is maintained in Git, and databases are networked.
Legacy Access applications are increasingly difficult to maintain.

Ideally, Access applications would be translated to some other open source
system that does not rely on Access, or Micosoft Windows, or any Microsoft
products at all. This is a problem that many other people have tried to fix,
so we broke it down into smaller pieces.

Instead of a single-user untrackable GUI point-and-click development
environment, Kraken turns Access applications into [diffable](https://en.wiktionary.org/wiki/diffable) 
plain text files. These text files can go anywhere, but the only thing we discuss here is
their use in source code version control.

After the files are retrieved from the Git service using a command such as ```git pull```, kraken
can then be used to load them into Microsoft Access, resulting in a complete GUI application in the
normal Access way. Microsoft Access and Microsoft Windows are still needed to run the source code.

But for now, we have solved the important step of making Access development
repeatable, using standard non-Microsoft software development tools.
"Repeatable" means that someone can get the same Access application after
executing "git clone" on a text file repository. Kraken does not however make
Access [reproducible](https://reproducible-builds.org/), because it creates
binary differences in databases for reasons that are invisible to the users.
Reproducibility is about quality software engineering, and Microsoft Access is not.

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

Anyone else who can see the Git repository can then do a
```git clone``` followed by ```kraken push``` and then a new Access
application is created locally for the user.

# Installation

You will need to [install Python 3 for Windows](https://docs.python.org/3/using/windows.html#installation-steps).
If you do this successfully, you should be able to type ```python``` at the Windows CMD command prompt. We have only 
tested on Python version 3.12.0, but would expect higher versions to work. Version 3.11.x and prior do *not* work.

It is good practice to use the [Python venv facility](https://docs.python.org/3/library/venv.html). 

At the Windows CMD prompt, use the ```pip``` command to install the kraken pre-requisites.

```shell
python -m pip install -r requirements.txt
```



# Using Kraken

## Basic usage

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

## Additional Tools

Kraken has multiple additional tools located inside `src/tools/`

### conv_utf16-ascii.py

Used to convert the UTF16 files which Access uses for forms and turns them into 8-bit ASCII. 

Usage: `python conv_utf16-ascii.py <Path to file/directory of files>`

### strip_guids.py

Strips the GUIDs from an exported form. We don't know why Access generates different
GUIDs every time, but they prevent diffing forms and so we need to remove them. Access
does not seem to mind.

Usage: `python strip_guids.py <Path to file/directory of files>`

### gen_docs.py

Generates documentation the functions implemented by Access's COM object. It will write this to `doc.txt`.

Usage: `python gen_docs.py`

# Relevant Computing History Background

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
