# Kraken

## Overview of Kraken, the Access monster

Many people still have legacy Access applications that perform important functions
even despite being obsolete technology. How can they escape?

We had exactly this problem, and we started by making Access repeatable. Perhaps
not quite [reproducible builds](https://en.wikipedia.org/wiki/Reproducible_builds) because
that is quite a high standard, but certainly heading that way.

To do that, we needed a way of turning Access into plain text files that can be
committed to a source code management system like any other code, even though it
was never designed for this and does not look like most kinds of programs. Access is
primarily a visual applications builder.

And that is why we wrote Kraken. kraken is a Python 3 program to dump the
contents of a Microsoft Access database program to a plain text diffable
format. An Access database contains not just tabular data, but also graphical
forms, BASIC source code, SQL queries and other object types.

The result is still tied to Microsoft Access and therefore to Microsoft
Windows, but it makes the logic visible, it makes changes trackable, and it
makes it much easier to plan our next step, which is to make the code work
in a completely open source stack.

---

## Using Kraken

### Basic usage

`python src/kraken.py <action> ... <database> <export>`

database: Path to an Access (.accdb) file  
export:   Path to where you want kraken to export/pull files from  
action:   Pick from this list:  

Dump/Load all data types

- dump-all
- load-all

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

Used to convert the UTF16 files which Access uses for forms and turns them into ascii
Usage: `python conv_utf16-ascii.py <Path to file/directory of files>`

#### strip_guids.py

Strips the GUIDs from an exported form.
Usage: `python strip_guids.py <Path to file/directory of files>`

#### gen_docs.py

Generates documentation for Access's COM object. It will write this to doc.txt
Usage: `python gen_docs.py`

---

## Background

Here is a list of facts, rather than a coherent story. No doubt people familiar
with the history of computing can improve the following, and we would love to
hear from you.

- Microsoft Access is 40 years old, and it is still present in quite a lot of
companies around the world. It is (even now) quite a good protoyping tool for
form-based GUI applications, which describes most business apps.
Microsoft have tried to kill the Access product off multiple times but they
have giant customers who complain because Access is so built-in to their computing
solutions. This means that while Access still works, Microsoft have not invested in
improving it for years.

- Access can work with remote SQL databases (using ODBC), but it is a
Windows-only desktop app which is often
very memory hungry, has lots of quirks and bugs, and is completely unsuitable
for use in the 21st century. Even by non-programmers, who are often the people
that start writing Access apps which then go on to become vital to an
organisation.

- Microsoft also made Access very hard to migrate away from. There is a lot
that is not documented. The BASIC programming language is VBA, not .NET basic,
meaning there are no other implementations of it. There is an "Export" feature
but it doesn't export everything that makes up an Access application.

- An Access application consists of: Forms; Basic code attached to objects on a
form such as a button; Basic code in modules available throughout the application;
database tables stored in the undocumented Jet format; SQL queries that operate on
these tables; macros and one or two other things.

- Many many companies have spent money migrating away from Access applications. It is
possible, including often just by ignoring the Access app except as a visual prototype.
There is no automated migration tool or technique that works for everyone, and nothing
in open source at all.

- There are good things to say about Access. Access code written decades ago
still runs just as well today, but most web front-end code in
javascript/Node/etc needs to be rewritten every two years. From that point of
view Access is cheaper and better over the long term. Which seems nonsense of
course because it is unmaintainable code, but also partly true.
