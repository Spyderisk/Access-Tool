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

# ===  Form dumping / loading  ===


import traceback
import os
from settings import Settings
from access.access import Access

# ===  DUMPING  ===


def dumpForm(formName, a: Access, s: Settings):
    try:
        a.app().DoCmd.OpenForm(formName)
        a.app().Application.SaveAsText(
            2, formName, os.path.join(s.formExport, formName + ".frm"))
        a.app().DoCmd.Close(2, formName)
    except:
        print("Form error", formName)
        traceback.print_exc()


def dumpAllForms(a: Access, s: Settings):
    allForms = a.currentProject().AllForms
    formNames = []
    for i in range(allForms.Count):
        formNames.append(allForms.Item(i).Name)

    count = 1
    for formName in formNames:
        print(f"\rDumping form {count}/{len(formNames)} -> {formName}", end="")
        dumpForm(formName, a, s)
        count += 1
    print()

# ===  LOADING  ===


def loadForm(formName, a: Access, s: Settings):
    a.app().Application.LoadFromText(
        2, formName, os.path.join(s.formExport, formName + ".frm"))


def loadForms(a: Access, s: Settings):
    formNames = [file for file in os.listdir(
        s.formExport) if file.split(".")[1] == "frm"]

    count = 1
    for formName in formNames:
        print(f"\rLoading forms {count}/{len(formNames)}", end="")
        loadForm(formName.split(".")[0], a, s)
        count += 1
    print()
