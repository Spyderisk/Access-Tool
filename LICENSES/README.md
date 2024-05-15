# Licenses in Kraken

If you have any questions do please ask
[team@spyderisk.org](mailto://team@spyderisk.org). This was originally developed for
the [Spyderisk Open Project](https://github.com/Spyderisk) and we use Spyderisk licensing.

We follow the 
[SPDX software component Bill of Materials](https://spdx.dev/) specification within individual source
files.

We use the [Apache 2](./APACHE-2.0.txt) license. If we use a library written by someone else,
if the third-party code has a license compatible with the
[Open Source Definition](https://opensource.org/osd/) then it will not conflict with
the Apache 2.0 license and we can freely use it.

# Apache 2.0 license - how to apply to Kraken files

In order to apply the Apache license to a source code file in the Spyderisk
project, insert the following comment block at the top, replacing the text in
[square brackets] with the correct values.

```
Copyright [YEAR] The Spyderisk Licensors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at:

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

<!-- SPDX-License-Identifier: Apache 2.0 -->
<!-- SPDX-FileCopyrightText: [YEAR] The Spyderisk Licensors -->
<!-- SPDX-ArtifactOfProjectName: Spyderisk -->
<!-- SPDX-FileType: Source code -->
<!-- SPDX-FileComment: Original by [NAME OF CONTRIBUTOR], [MONTH] [YEAR] -->
```

# Creative Commons BY-SA - documentation and config files

We do not to apply copyright headers to README files such as the one you are reading.
If we add any non-Markdown forms of documentation should have an explicit CC BY-SA
license at the top. 

```
Copyright 2023 The Spyderisk Authors

<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
<!-- SPDX-FileCopyrightText: 2023 The Spyderisk Authors -->
<!-- SPDX-ArtifactOfProjectName: Spyderisk -->
<!-- SPDX-FileType: Documentation -->
<!-- SPDX-FileComment: Original by Dan Shearer, October 2024 -->
```

# What about third-party GPL code?

The important thing about Kraken is that it works, nobody is really worried 
about licensing so long as it is open source. There are two cases:

1. GPLv2 code, which we cannot use.  GPLv2 is the one major open source license which is
[incompatible with the Apache license](https://en.wikipedia.org/wiki/Apache_License#Compatibility).
2. GPLv3/AGPLv3/LGPLv2/LGPLv3 - we can use such code if we need to.

Unlike version 2, the
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt) is 
compatible with Apache 2.0, **but only in one direction**.  After codebases
under these two licenses are combined, the combined result can only be
distributed under the GPLv3 (again, there are some additional but this is
approximately correct.) That is unlikely to ever be a problem for Kraken,
so yes of course we can use GPL code other than v2.
