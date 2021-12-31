"""
Replaces invalid filename characters. Makes part of spotify-extractor.

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

from string import ascii_letters as asciiLetters

def replaceCharacters(name):
  invalidCharacters = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]
  for characterIndex in range(len(invalidCharacters)):
    name = name.replace(invalidCharacters[characterIndex], "-")

  while name[0] not in asciiLetters:
    if name[0] == " ":
      name = name[1:]
    
    else:
      break

  return name