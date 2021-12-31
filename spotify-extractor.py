"""
spotify-extractor: extract playlist, album or track information using Spotify's API.

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

from core.extractors import playlist


def terminateExecution(keyboardInterruption = False):
  print("\nSee ya! =^)")

  if keyboardInterruption == False:    
    input("Press ENTER to terminate... ")


try:
  print("===== SPOTIFY EXTRACTOR =====")
  print("Which Spotify media would you like to extract information? \n1 - Playlist \n2 - Album \n3 - Track \n")

  option = input()
  if option == "1":
    print("\nYou have selected: 1 - Playlist")

    playlistID = input("\nPaste here the Spotify playlist id \nEg. https://open.spotify.com/playlist/<id> <-- this\n")
    playlist.getPlaylist(playlistID)

  elif option == "2": # Album
    pass

  else: # Track
    pass

except KeyboardInterrupt:
  terminateExecution(True)