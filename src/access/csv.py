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

# ===  CSV Loading  ===


import sqlite3
import pandas as pd
import os
from settings import Settings

# ===  LOADING  ===


def loadCSV(path, tableName, s: Settings):
    con = sqlite3.connect(os.path.join(
        s.exportPath, "DomainModel.db"), isolation_level=None)
    csv = pd.read_csv(path)
    csv.to_sql(tableName, con, if_exists='append', index=False)


def loadCSVs(path, s: Settings):
    files = os.listdir(path)
    count = 1
    for file in files:
        print(f"\r{count}/{len(files)} tables", end="")
        loadCSV(os.path.join(path, file), file.split(".")[0], s)
        count += 1
    print()
