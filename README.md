# spotify-artist-discography

I've recently switched from using Spotify to a selfhosted Navidrome setup, I created this script so I could grab my current music library artists, search their discography on spotify to generate a list of all their albums and then use that list to fill in any missing gaps.

## Result

I am finding a bunch of duplicate albums, e.g Delux editions or re-releases

```
    "The Fratellis": {
        "albums": [
            "Half Drunk Under a Full Moon (Deluxe)",
            "Half Drunk Under A Full Moon (Deluxe)",
            "Half Drunk Under a Full Moon",
            "Half Drunk Under A Full Moon",
            "IN YOUR OWN SWEET TIME (+3 Bonus Track)",
            "In Your Own Sweet Time",
            "Eyes Wide, Tongue Tied (Super Deluxe)",
            "Eyes Wide, Tongue Tied",
            "Eyes Wide, Tongue Tied (Deluxe)",
            "We Need Medicine (Exclusive Commentary)",
            "We Need Medicine (Deluxe Edition)",
            "We Need Medicine",
            "Here We Stand",
            "Here We Stand (UK Version)",
            "Here We Stand (other BPs international)",
            "Costello Music"
        ]
    },
```

## Installation

Create new python env

```bash
python -m venv env
```

activate env

```bash
source env/bin/activate
```

install requirements

```bash
pip install -r requirements.txt
```

## Artist List

### Example

rename artists.txt.example to artists.txt

### Generating artists.txt

```bash
cd music/albums
ls > artists.txt
```

## Setup .env

Rename .env.example to .env

`SPOTIPY_CLIENT_ID` - Create: https://developer.spotify.com/dashboard/login

`SPOTIPY_CLIENT_SECRET` - Client secret from created client id
