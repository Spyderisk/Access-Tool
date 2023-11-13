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

# ===  Tool for converting UTF-16 to ASCII  ===
# Access stores its Form objects (among others) in UTF-16. Most text processing
# tools including diff and git need special configuration to handle this, and 
# so we convert to plain ASCII. Access is happy to import forms in ASCII text.


import codecs
import os
import traceback
import shutil

def convert_file(path: str, out: str, force = False):
    # Force: copy the file regardless of operation
    try:
        with codecs.open(path, 'r', 'utf-16') as rd:
            lines = rd.read()
        with codecs.open(out, 'w', 'ascii') as wt:
            wt.write(lines)
    except UnicodeError as e:
        if force:
            shutil.copy(os.path.abspath(path), os.path.abspath(out))
        else:
            raise e


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="conv_utf16_ascii",
        description="Converts utf16 files to ascii, or directories of utf16",
    )

    parser.add_argument(
        'file',
        type=str,
    )

    args = parser.parse_args()

    if os.path.isdir(args.file):
        for file in os.listdir(args.file):
            path = os.path.join(args.file, file)

            try:
                convert_file(path, path)
            except UnicodeError:
                print(f"{path} conversion error")
                traceback.print_exc()
    else:
        try:
            convert_file(args.file, args.file)
        except UnicodeError:
            print(f"{args.file} conversion error")
            traceback.print_exc()