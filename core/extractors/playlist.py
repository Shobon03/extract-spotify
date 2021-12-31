"""
Extracts Spotify playlist information. Makes part of spotify-extractor.

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

import requests

from core.commons.get_token import getToken
from core.commons.generate_file import generateFile

def getPlaylist(playlistID):

  accessToken = getToken()

  def requestPlaylist(requestType, offset = 0):
    if requestType == "tracks":
      return requests.get(
        f"https://api.spotify.com/v1/playlists/{playlistID}/tracks?limit=100&offset={offset}", 
        headers = {
          "Authorization": "Bearer " + accessToken
        }
      ).json()

    else:
      return requests.get(f"https://api.spotify.com/v1/playlists/{playlistID}", 
        headers = {
          "Authorization": "Bearer " + accessToken
        }
      ).json()


  playlistDetails = requestPlaylist("details")

  playlistName = playlistDetails["name"]
  playlistOwner = playlistDetails["owner"]["display_name"]


  items = {
    "name": playlistName, 
    "owner": playlistOwner, 
    "spotify-playlist-link": playlistDetails["external_urls"]["spotify"]
  }
  def getPlaylistTracks(trackID = 0):
    for tracks in range(len(playlist["items"])):
      
      artists = ""
      for artist in range(len(playlist["items"][tracks]["track"]["artists"])):
        if artist == 0:
          artists = playlist["items"][tracks]["track"]["artists"][artist]["name"]
        
        else:
          artists += "; " + playlist["items"][tracks]["track"]["artists"][artist]["name"]

      track = {}
      track["name"] = playlist["items"][tracks]["track"]["name"] 
      track["artists"] = artists
      track["album"] = playlist["items"][tracks]["track"]["album"]["name"]
      track["spotify-track-link"] = playlist["items"][tracks]["track"]["external_urls"]["spotify"]

      items[trackID] = track
      trackID += 1

    return trackID


  playlist = requestPlaylist("tracks")
  lastID = getPlaylistTracks()

  offset = 100
  while playlist["items"] != []:
    playlist = requestPlaylist("tracks", offset)
    offset += 100

    lastID = getPlaylistTracks(lastID)

  items["total-tracks"] = lastID

  print("\nInformation gathered successfully!")

  generateFile("json", "playlists", playlistName, playlistOwner, items)