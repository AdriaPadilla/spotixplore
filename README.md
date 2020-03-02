# Spotixplore V 0.1.5
[![Anaconda-Server Badge](https://anaconda.org/adriapadilla/spotixplore/badges/version.svg)](https://anaconda.org/adriapadilla/spotixplore)  [![Anaconda-Server Badge](https://img.shields.io/pypi/v/spotixplore.svg)](https://pypi.org/project/spotixplore/)

![Spotixplore graph image](https://github.com/AdriaPadilla/spotixplore/blob/master/spotixplore/img/img1.png
)

## 1. What is this about?
***Important note: Spotixplore is not finished!***

This tool has been created to explore the possibilities of the Spotify WEB API, and more concertedly, the way in which music is recommended and related. Spotixplore provides a bunch of metrics for each song, in order to develop patterns that allow a better understanding of the operation of Spotify, as well as the study of music production and consumption and the effect on users.

## 2. Limitations
Spotify applies some limitations.

If you are interested in limitations. visit:

https://developer.spotify.com/documentation/web-api/

### 3. Installation
Option 1: Pip install

```bash
...$: pip install spotixplore
```

Option 1.1: Conda install
```bash
conda install -c adriapadilla spotixplore
```

Option 2: Hardcode

Step 1: Clone this repository in your pc

```bash
...$: git clone https://github.com/AdriaPadilla/spotixplore.git
```

Step 2: Access the main folder
```bash
...$: cd spotixlpre
```

Step 3: Execute install
```bash
.../spotixplore/$: python3 setup.py install
```

## 4. Configuration

To use this applications, you'll need Spotify API credentials:

+ Go to: https://developer.spotify.com/dashboard/login
+ Create a new account or login
+ Click on "Create Client ID"
+ Copy your "Client ID" and "Client Secret"
+ Open "credentials.py" and place your credentials between " ":
```python
SPOTIPY_CLIENT_ID = "YOUR CLIENT ID"
SPOTIPY_CLIENT_SECRET = "YOU SECRET CLIENT ID"
```

## 5. Execution
Steps:

1. Go to the installation folder
2. find starting_point.py
3. Put your Spotify playlist (one, or more). Following the correct format:
```python3
PLAYLISTS = ["4KvPhEa7g4aeCfOp3HMtOj", "anotherplaylist", "anotherplaylist"]
```

**To execute**, just run main.py:
```bash
.../your_path_to/spotixplore/$: python3 main.py
```
OR:
```bash
.../no_matter_where_you_are/$: python3 -m spotixplore.main
```

### Change the nº of related tracks

Working to make it more easy!

You have to change "limit=" property on line 88 of "recommended_tracks.py"

## 6. The Output
The application will create 2 files:

One .XLSX file for each playlist with all the data, including recommended tracks.

One .CSV file with node relations to generate a graph network visualization.
