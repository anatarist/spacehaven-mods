#!/usr/bin/env python3

import os
import textwrap

from xml.etree import ElementTree

VERSION = '0.0.1'


readme = open('README.md', 'w')

readme.write(textwrap.dedent("""\
    # Space Haven Mods

    This is a collection of unofficial mods tool for [Space Haven by Bugbyte](http://bugbyte.fi/spacehaven/), an early-alpha spaceship colony sim.

    It is **not associated with Bugbyte or Space Haven in any way** other than that it adds some mods to the game. These are intended to be a sneak peek at what modding might be able to do, and in the future will be updated to use official mod support.

    All of these mods require [the unofficial mod loader](https://github.com/anatarist/spacehaven-modloader) to use.


"""))

mods = os.listdir('mods')
mods.sort()
for mod in mods:
    info = ElementTree.parse(os.path.join('mods', mod, 'info')).getroot()

    if info.find('wip') is not None:
        continue

    if os.path.exists(os.path.join('mods', mod, 'preview.gif')):
        preview = "![{mod}](/mods/{mod}/preview.gif?raw=true)".format(mod=mod)

    readme.write(textwrap.dedent("""\
        ## {name}

        {preview}

        {description}

        #### [Download {mod}-{version}.zip](https://github.com/anatarist/spacehaven-mods/releases/download/v{version}/{mod}-{version}.zip)


    """).format(
        name=info.find("name").text.strip(),
        description=info.find("description").text.strip(),
        mod=mod,
        preview=preview,
        version=VERSION
    ))

    os.system("cd mods && zip -r {mod}-{version}.zip {mod}".format(mod=mod, version=VERSION))

readme.close()

os.system("rm -r dist")
os.system("mkdir -p dist")
os.system("mv mods/*.zip dist")
os.system("open dist")
