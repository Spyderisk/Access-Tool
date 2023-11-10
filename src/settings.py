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

# ===  Kraken Settings  ===
# Holds configuration settings for kraken, currently only export paths


import os


class Settings:
    exportPath: str
    formExport: str
    moduleExport: str
    tableExport: str
    queryExport: str

    def __init__(self, exportPath):
        self.exportPath = exportPath

        self.formExport = os.path.join(exportPath, "forms")
        self.moduleExport = os.path.join(exportPath, "modules")
        self.tableExport = os.path.join(exportPath, "tables")
        self.queryExport = os.path.join(exportPath, "querys")

        paths = [self.exportPath, self.formExport,
                 self.moduleExport, self.tableExport, self.queryExport]

        for path in paths:
            try:
                os.mkdir(path)
            except FileExistsError:  # May fail is exists, but this is fine
                pass
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                raise
