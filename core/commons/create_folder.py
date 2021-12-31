"""
Saves extracted data in a folder. Makes part of spotify-extractor.

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

import os

def createFolder(type, author):
  try:
    os.makedirs(f"extracted-info/{type}/{author}", exist_ok = True)

    print(f"\nCreated folder \"./extracted-info/{type}/{author}\"")

  except FileExistsError:
    pass

  finally:
    print(f"\nFolder \"extracted-info/{type}/{author}\" already exists. Skipping...")