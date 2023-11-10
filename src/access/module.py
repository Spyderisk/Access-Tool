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

# ===  Module dumping / loading  ===


import traceback
import os
from settings import Settings
from access.access import Access

# ===  DUMPING  ===


def dumpModule(moduleName, a: Access, s: Settings):
    try:
        a.app().DoCmd.OpenModule(moduleName)
        a.app().Application.SaveAsText(
            5, moduleName, os.path.join(s.moduleExport, moduleName + ".bas"))
        a.app().DoCmd.Close(5, moduleName)
    except:
        print("Module error", moduleName)
        traceback.print_exc()


def dumpAllModules(a: Access, s: Settings):
    allModules = a.currentProject().AllModules
    moduleNames = []
    for i in range(allModules.Count):
        moduleNames.append(allModules.Item(i).Name)

    count = 1
    for moduleName in moduleNames:
        print(f"\rDumping module {
              count}/{len(moduleNames)} -> {moduleName}", end="")
        dumpModule(moduleName, a, s)
        count += 1
    print()

# ===  LOADING  ===


def loadModules(a: Access, s: Settings):
    files = [file for file in os.listdir(
        s.moduleExport) if file.split(".")[1] == "bas"]

    count = 1
    for file in files:
        print(f"\rLoading module {count}/{len(files)}", end="")
        moduleName = file.split(".")[0]
        a.app().Application.LoadFromText(
            5, moduleName, os.path.join(s.moduleExport, file))
        count += 1
    print()
