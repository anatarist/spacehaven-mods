#!/usr/bin/env python3

import os
import textwrap

from xml.etree import ElementTree

VERSION = '0.0.2'


readme = open('README.md', 'w')

readme.write(textwrap.dedent("""\
    # Space Haven Mods

    An unofficial collection of mods for Space Haven by Bugbyte. Requires the [unofficial mod loader](https://github.com/anatarist/spacehaven-modloader) to use.

    All of the mods are downloadable from [the releases page](https://github.com/anatarist/spacehaven-mods/releases).


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
