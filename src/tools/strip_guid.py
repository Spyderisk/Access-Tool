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

# ===  Tool for stripping GUIDs from Access forms  ===
# The GUIDs do not have any known purpose, and since they change every time they
# prevent the files from being diffed.


import os
import conv_utf16_ascii


def strip_guid(path: str, out: str):
    conv_utf16_ascii.convert_file(path, path + ".temp", force=True)

    ifile = open(path + ".temp", "r")
    ofile = open(out, "w")

    for line in ifile:
        if line.find("GUID") > 0:  # Skip 2 lines for the GUID
            ifile.readline()
            ifile.readline()
        else:
            ofile.write(line)

    ifile.close()
    ofile.close()
    os.remove(path + ".temp")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="GUIDStripper",
        description="Strips GUIDs out of kraken .frm dump files",
    )

    parser.add_argument(
        'file',
        type=str,
    )

    args = parser.parse_args()

    if os.path.isdir(args.file):
        for file in os.listdir(args.file):
            path = os.path.join(args.file, file)
            strip_guid(path, path)
            print(file)
    else:
        strip_guid(args.file, args.file)
