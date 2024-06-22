_**UNMAINTAINED: PUBLIC ARCHIVE AS OF 22-06-2024**_

# spotify extractor

A simple CLI tool written in Python for extracting Spotify playlist, album or track information!

# Libraries used

- requests

# Extracted information

Using this script, you can generate .txt or .json files with information from a Spotify playlist, album or track.

The generated file will have:

- Playlist

```
{
  "name": "",
  "owner": "",
  "spotify-playlist-link": "",
  "0": {
    "name": "",
    "artists": "",
    "album": "",
    "spotify-track-link": ""
  },
  ...
}
```

- Album

- Tracks

# Executing

On a terminal emulator, simply run:

`$ extractor`

# License

```
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
```
