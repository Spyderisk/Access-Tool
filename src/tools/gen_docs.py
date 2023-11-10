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

# ===  COM documentation generator  ===
# Opens a Microsoft Access com object and runs through it, writing all modules, functions and properties to `doc.txt`
# This is needed as existing com browsers can be a bit funky at times and no official documentation exists

import win32com.client as win32
import os

def open_access() -> win32.dynamic.CDispatch:
    try:
        return win32.gencache.EnsureDispatch('Access.Application')
    except AttributeError:  # If the cache is broken, it will error
        print("Cache import failure")
        temp = os.path.join(os.environ["TEMP"], "gen_py")
        try:
            os.remove(temp)  # Fails, due to lack of permissions
            return win32.gencache.EnsureDispatch('Access.Application')
        except PermissionError:
            print(f"Unable to clear cache, please delete '{temp}'")
            exit(-1)


def get_members(object) -> tuple[list, list, list]:
    items = [name for name in dir(object)]

    modules = []
    methods: list[tuple[function, str]] = []
    properties = []

    for item_name in items:
        try:
            item = getattr(object, item_name)

            # Filter out builtins
            if str(type(item)) not in ["<class 'builtin_function_or_method'>"]:
                # print(item)
                if getattr(item, "__call__"):
                    methods.append((item, item_name))
                else:
                    print(item_name)
                    modules.append(get_members(item))
        except:
            properties.append(item_name)

    return (modules, methods, properties)


def write_node(node: tuple[list, list, list], i=1):
    print(f"{len(node[0])}, {len(node[1])}, {len(node[2])}")

    file.write("Functions:\n")
    for item in node[1]:
        file.write(f"    {item[1]}: {type(item[0])}\n")

    file.write("Misc:\n")
    for item in node[2]:

        file.write(f"    {item}\n")


project = open_access()
file = open("doc.txt", "w")

tree = get_members(project)

file.write("MS ACCESS COM DOCS\n\n")

write_node(tree, 0)
