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

# ===  Access COM wrapper  ===
# Implemented such that MS Access only gets opened when it is actually needed

from os.path import join
from os import environ, remove
import win32com.client as win32


class Access:
    __app: win32.dynamic.CDispatch | None
    __currentProject: None  # = project.Application.CurrentProject
    __currentData: None  # = project.Application.CurrentData
    path: str

    def __init__(self, path: str) -> None:
        self.path = path

        self.__app = None
        self.__currentProject = None
        self.__currentData = None

    def is_init(self) -> bool:
        return self.__app is not None

    def app(self) -> win32.dynamic.CDispatch:
        if not self.is_init():
            self.__open_access()

        return self.__app

    def currentProject(self):
        if not self.is_init():
            self.__open_access()

        return self.__currentProject

    def currentData(self):
        if not self.is_init():
            self.__open_access()

        print(type(self.__currentData))

        return self.__currentData

    def __open_access(self):
        try:
            self.__app = win32.gencache.EnsureDispatch('Access.Application')
        except AttributeError:  # If the cache is broken, it will error
            print("Cache import failure")
            temp = join(environ["TEMP"], "gen_py")
            try:
                remove(temp)  # Fails, due to lack of permissions
                self.__app = win32.gencache.EnsureDispatch(
                    'Access.Application')
            except PermissionError:
                print(f"Unable to clear cache, please delete '{temp}'")
                exit(-1)

        self.__app.Application.OpenCurrentDatabase(self.path)

        self.__currentProject = self.__app.Application.CurrentProject
        self.__currentData = self.__app.Application.CurrentData

    def quit(self):
        if self.is_init():
            self.__app.Application.Quit()