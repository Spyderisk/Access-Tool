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

# ===  Table dumping / loading  ===


import pyodbc
import sqlite3
import sys
from os import popen, path
from settings import Settings
from access.access import Access

# ===  DUMPING  ===


def dumpTable(tableName, s: Settings, db: str):
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db + ';')

    # Converter added due to decode error - https://github.com/mkleehammer/pyodbc/issues/328#issuecomment-419655266
    conn.add_output_converter(pyodbc.SQL_WVARCHAR, decode_sketchy_utf16)

    cursor = conn.cursor()

    # path = os.path.join(exportPath, "database-schema.sql")
    # f = open(path, "a")
    # f.write("CREATE TABLE " + tableName + getFieldsAndTypes(cursor, tableName) + "\n")
    # f.close()

    con = sqlite3.connect(path.join(
        s.exportPath, "DomainModel.db"), isolation_level=None)
    cur = con.cursor()
    cur.execute("CREATE TABLE " + tableName +
                getFieldsAndTypes(cursor, tableName))

    # cursor.execute("select * from " + tableName)
    # path = os.path.join(exportPath, "table-contents.sql")
    # f = open(path, "a")
    # for row in cursor:
    #     row = rowString(row)
    #     # cur.execute("INSERT INTO " + tableName + " VALUES " + row)
    #     f.write("INSERT INTO " + tableName + " VALUES " + row + "\n")
    # f.close()


def dumpTables(s: Settings, db: str):
    # print(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + sys.argv[2] + ';')
    print(*sys.argv, sep=", ")
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db + ';')

    cursor = conn.cursor()
    # tables starting with "_" not included because they were causing errors and they don't have a csv file counterpart?
    tables = [listing[2] for listing in cursor.tables(
        tableType='TABLE') if listing[2].startswith("_") == False]

    count = 1
    for table in tables:
        print(f"Dumping table {count}/{len(tables)}", end="\r")
        dumpTable(table, s, db)
        count += 1
    print()


def decode_sketchy_utf16(raw_bytes):
    s = raw_bytes.decode("utf-16le", "ignore")
    try:
        n = s.index('\x00')
        s = s[:n]
    except ValueError:
        pass
    return s


def getFieldsAndTypes(cursor, tableName):
    fieldsList = []
    typesList = []
    for row in cursor.columns(table=tableName):
        fieldsList.append(row.column_name)
        typesList.append(row.type_name)

    s = "("
    for i in range(len(fieldsList)):
        s = s + fieldsList[i] + " " + typesList[i] + ", "
    s = s[:-2] + ")"
    return s


def dumpSchema(s: Settings):
    dump = popen(f"sqlite3 {path.join(
        s.exportPath, "domainModel.db")} .dump").read()

    # db = sqlite3.connect(os.path.join(s.exportPath, "DomainModel.db"))

    # dump = db.iterdump()

    file = open(path.join(s.exportPath, "data.sql"), "w")
    file.write(dump)

    # for line in dump:
    #     file.write(line + '\n')

# def removExtension(fileName):
#     return fileName.split(".")[0]

# def fieldsString(fields):
#     s = str(fields)
#     s = s.replace("[", "(")
#     s = s.replace("]", ")")
#     s = s.replace("'", "")
#     return s

# def rowString(row):
#     return str(row).replace("None", "NULL")

# ===  LOADING  ===


def loadTables(a: Access, s: Settings):
    filePath = path.join(s.exportPath, "data.sql")
    with open(filePath) as file:
        lines = len(file.readlines())

    with open(filePath) as file:
        count = 1
        for line in file:
            print("\rloading tables {}%".format(int(count/lines*100)), end="")
            if line.startswith("CREATE") or line.startswith("INSERT"):
                a.app().DoCmd.RunSQL(line)
            count += 1
    print()
