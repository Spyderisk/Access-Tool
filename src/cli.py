# Copyright 2023 The Spyderisk Authors

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at:

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# <!-- SPDX-License-Identifier: Apache 2.0 -->
# <!-- SPDX-FileCopyrightText: 2023 The Spyderisk Authors -->
# <!-- SPDX-ArtifactOfProjectName: Spyderisk -->
# <!-- SPDX-FileType: Source code -->
# <!-- SPDX-FileComment: Original by Jacob Lewis, November 2023 -->

# ===  Argument Handling  ===


import argparse

HELP_SUBCOMMANDS =\
"""
Actions list:
dump-all
load-all

dump-form <form_name>
dump-module <module_name>
dump-query <query_name>
dump-table <table_name>
dump-schema

dump-forms
dump-modules
dump-queries
dump-tables

load-form <form_name>

load-csvs <csvs_directory>
load-tables
load-queries
load-forms
"""


def subp(p, action, extra=None, db=False):
    parser = p.add_parser(action)

    if extra != None:
        parser.add_argument(extra)
    
    if db:
        parser.add_argument(
            "database",
            help="Path to a microsoft access database",
        )

        parser.add_argument(
            "export",
            help="Path to a folder where Kraken will export/pull from"
        )


def parse_args():
    parser = argparse.ArgumentParser(
        prog='Kraken',
        description='Microsoft Access to SQL converter',
    )

    s = parser.add_subparsers(help="Use action-list for actions", metavar="action", dest="action")

    subp(s, "action-list")

    subp(s, "pull", db=True)
    subp(s, "push", db=True)

    subp(s, "dump-form", "form_name")
    subp(s, "dump-module", "module_name", db=True)
    subp(s, "dump-query", "query_name", db=True)
    subp(s, "dump-database", db=True)
    # subp(s, "dump-table", "table_name", db=True)
    # subp(s, "dump-schema", db=True)

    subp(s, "dump-forms", db=True)
    subp(s, "dump-modules", db=True)
    subp(s, "dump-queries", db=True)
    # subp(s, "dump-tables", db=True)

    subp(s, "load-form", "form_name", db=True)

    subp(s, "load-csvs", "csvs_directory", db=True)
    subp(s, "load_database", db=True)
    subp(s, "load-queries", db=True)
    subp(s, "load-forms", db=True)

    args = parser.parse_args()

    if not args.action:
        parser.print_help()
        exit(1)

    if args.action == "action-list":
        print(HELP_SUBCOMMANDS)
        exit(0)

    return args
