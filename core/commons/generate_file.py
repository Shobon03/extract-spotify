"""
Generates files with extracted data. Makes part of spotify-extractor.

Copyright (C) 2021  Shobon03

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json

from core.commons.create_folder import createFolder
from core.commons.replace_invalid_characters import replaceCharacters

def generateFile(fileType, whichData, name, author, items):
  createFolder(whichData, author)

  playlistFile = open(f"./extracted-info/{whichData}/{author}/{replaceCharacters(name)}.{fileType}", "w")
  playlistFile.write(json.dumps(items, indent = 2, ensure_ascii = False))
  playlistFile.close()

  print("\nFile generated successfully!")