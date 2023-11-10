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

# ===  Query dumping / loading  ===


import traceback
import os
from settings import Settings
from access.access import Access

# ===  DUMPING  ===


def dumpQuery(queryName, a: Access, s: Settings):
    dbName = a.app().DBEngine.Workspaces(0).Databases(0).Name
    try:
        queryString = a.app().DBEngine.Workspaces(
            0).OpenDatabase(dbName).QueryDefs(queryName).SQL
        path = os.path.join(s.queryExport, queryName + ".sql")
        f = open(path, "w")
        f.write(queryString)
        f.close()
    except:
        print("Query error", queryName)
        traceback.print_exc()


def dumpAllQueries(a: Access, s: Settings):
    allQueries = a.app().Application.CurrentData.AllQueries
    queryNames = []
    for i in range(allQueries.Count):
        queryNames.append(allQueries.Item(i).Name)

    count = 1
    for queryName in queryNames:
        print(f"\rDumping query {
              count}/{len(queryNames)} -> {queryName}", end="")
        dumpQuery(queryName, a, s)
        count += 1
    print()

# ===  LOADING  ===


def loadQueries(a: Access, s: Settings):
    files = [file for file in os.listdir(
        s.queryExport) if file.split(".")[1] == "sql"]

    count = 1
    for file in files:
        print(f"\rLoading table {count}/{len(files)}", end="")
        sql = open(os.path.join(s.queryExport, file), "r")
        dbName = a.app().DBEngine.Workspaces(0).Databases(0).Name
        a.app().DBEngine.Workspaces(0).OpenDatabase(
            dbName).CreateQueryDef(file.split(".")[0], sql.read())
        count += 1
    print()
