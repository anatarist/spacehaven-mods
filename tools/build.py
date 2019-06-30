#!/usr/bin/env python3

import os
import textwrap

from xml.etree import ElementTree

VERSION = '0.0.2'


readme = open('README.md', 'w')

readme.write(textwrap.dedent("""\
    # Space Haven Mods

    This is a collection of unofficial mods tool for [Space Haven by Bugbyte](http://bugbyte.fi/spacehaven/), an early-alpha spaceship colony sim.

    It is **not associated with Bugbyte or Space Haven in any way** other than that it adds some mods to the game. These are intended to be a sneak peek at what modding might be able to do, and in the future will be updated to use official mod support.

    All of the mods are downloadable from [the releases page](https://github.com/anatarist/spacehaven-mods/releases) and require [the unofficial mod loader](https://github.com/anatarist/spacehaven-modloader) to use.


"""))

for mod in os.listdir('mods'):
    info = ElementTree.parse(os.path.join('mods', mod, 'info')).getroot()

    if info.find('wip') is not None:
        continue

    readme.write(textwrap.dedent("""\
        ## {name}

        {description}


    """).format(
        name=info.find("name").text.strip(),
        description=info.find("description").text.strip()
    ))

    os.system("cd mods && zip -r {mod}-{version}.zip {mod}".format(mod=mod, version=VERSION))

readme.close()

os.system("rm -r dist")
os.system("mkdir -p dist")
os.system("mv mods/*.zip dist")
os.system("open dist")
