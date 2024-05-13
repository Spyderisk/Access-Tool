# Short summary

Spyderisk is licensed under the Apache 2.0 license.

The [README in the licenses directory](./LICENSES/README.md) explains *how* developers should apply
license headers to files in Spyderisk. This document is about the *why and what* of licensing.

The site [TL;DR Legal](https://www.tldrlegal.com/license/apache-license-2-0-apache-2-0)
summarises the Apache license as:
> You can do what you like with the software, as long as you include the required notices.
> This permissive license contains a patent license from the contributors of the code.

For most people most of the time, this is all you need to know - please use and enjoy Spyderisk!

# Spyderisk Open Project Copyright and Licenses

Spyderisk source code is available entirely under [Open
Source](https://opensource.org/osd) licenses, either the [Apache2
license](licenses/LICENSE-2.0.txt) as described above, or occasionally other licenses which are
compatible with Apache2. 

We use two standards to maintain copyright and licensing of all artefacts in the Spyderisk project:

* The [REUSE](https://reuse.software/spec/) high-level system of files and directories regarding licensing
* The [SPDX software component descriptors](https://spdx.dev/), which are Software Bill of Materials (SBOM) system

Both of these standards can be read by humans and machines, so Spyderisk is
compatible with various automated due diligence systems.

# Licensor or Contributor?

The distinction matters legally, but in the day-to-day we just want to
acknowledge the work done by many people over the years. Only someone who owns
code has the right to license that code. Many substantial Spyderisk
contributors commit their work but do not own their contributions, and
therefore they cannot be a licensor.

Spyderisk licensing is explained by its history:

* In 2023, when all source code was open sourced, the University of Southampton (Soton) was the main copyright licensor
* There were many individual code contributors employed by Soton who were and remain Spyderisk authors, but all of their work in Spyderisk while being Soton employees is owned by Soton. These authors (called "contributors" to avoid confusion) are therefore not copyright licensors
* A small proportion of the Spyderisk code has been incorporated from other open source projects, and remains copyrighted by its respective owners/licensors
* Any future contributors to Spyderisk who are not Soton employees will own their contributions, and so they will be both authors and owners/licensors
* Some future contributors may be in a similar situation to Soton employees, and their employer will own all their Spyderisk contributons. We would respectfully request that contributors check with their employer to see if they have the right to contribute individually, because we think that is better for the project overall.

There is much more detail in the detailed [HISTORY file](./HISTORY.md).

Many Spyderisk source files simply state "Copyright the Spyderisk licensors" at
the top in the manner specified by the SPDX standard, where the
owners/licensors are listed in the [LICENSORS file](./LICENSORS.md). This is
usually followed by the statement "Original by A. Person", where "A. Person" is
listed in the [CONTRIBUTORS file](./CONTRIBUTORS.md) regardless of whether or
not they have any copyright ownership. CONTRIBUTORS should contain a list of
all known code contributors, while LICENSORS will be a much shorter list of
copyright owners.

Spyderisk documentation is generally under a Creative Commons license, again
explained in detail in ```licenses/README.md```.

# No CLA

As a matter of policy, Spyderisk does not and will not have a Contributor License Agreement (CLA),
for reaons similar to [Red Hat](https://opensource.com/article/19/2/cla-problems),
the [Software Freedom Conservancy](https://sfconservancy.org/blog/2014/jun/09/do-not-need-cla/) and
other leading open source voices. 

Spyderisk adheres to the "inbound = outbound" principle, where Licensors get
exactly the same rights as anyone else in the world. While we use the excellent
Apache 2 license from [apache.org](https://apache.org), Spyderisk is not
affiliated with apache.org, and we do not use the Apache CLAs or other tools
which do not share rights equally with all.
