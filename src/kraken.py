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

# ===  Kraken entrypoint  ===


from os.path import abspath

from cli import parse_args
from access.access import Access
from settings import Settings
from access.form import dumpForm, dumpAllForms, loadForm, loadForms
from access.module import dumpModule, dumpAllModules, loadModules
from access.query import dumpQuery, dumpAllQueries, loadQueries
from access.table import dumpTable, dumpTables, dumpSchema, loadTables
from access.csv import loadCSVs


args = parse_args()

# Paths must be absolute
args.database = abspath(args.database)
args.export = abspath(args.export)

access = Access(args.database)
settings = Settings(args.export)

match args.action:
    case "dump-all":
        dumpAllForms(access, settings)
        dumpAllModules(access, settings)
        dumpAllQueries(access, settings)
        dumpTables(settings, args.database)
        dumpSchema(settings)

    case "load-all":
        loadTables(access, settings)
        loadQueries(access, settings)
        loadForms(access, settings)
        loadModules(access, settings)

    case "dump-form":
        dumpForm(args.form_name, access, settings)
    case "dump-module":
        dumpModule(args.module_name, access, settings)
    case "dump-query":
        dumpQuery(args.query_name, access, settings)
    case "dump-table":
        dumpTable(args.table_name, settings, args.database)
    case "dump-schema":
        dumpSchema(settings)

    case "dump-forms":
        dumpAllForms(access, settings)
    case "load-forms":
        loadForms(access, settings)
    case "dump-modules":
        dumpAllModules(access, settings)
    case "dump-queries":
        dumpAllQueries(access, settings)
    case "dump-tables":
        dumpTables(settings, args.database)
        loadCSVs(args.table_name, settings)

    case "load-form":
        loadForm(args.form_name, access, settings)

    case "load-csvs":
        loadCSVs(args.csvs_directory, settings)
    case "load-tables":
        loadTables(access, settings)
    case "load-queries":
        loadQueries(access, settings)
    case "load-modules":
        loadModules(access, settings)

access.app().Application.Quit()
