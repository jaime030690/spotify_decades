# Spotify Decades

## Overview

By the end of 2019 Spotify had the [largest percentage of unique users](https://www.midiaresearch.com/blog/music-subscriber-market-shares-h1-2019/) of all streaming services. Using the Spotify API it is possible to retrieve metadata on individual tracks which is generated algorithmically, we are primarily speaking of key and time signature, tempo, and mode (major/minor).

The goal of this project is to find trends in Spotify-curated playlists "All Out ##s" from the 50s until the 10s using the following values:
* Key signature
* Time signature
* Tempo
* Mode
## Considerations
### Key Signature
Spotify uses integer values to assign key signatures to each track (0 = C, 1 = C#/Db, ... , 11 = B). The algorithm listens for trends in notes and chords throughout the song to assign a value. There is also a confidence interval which ranges from 0 thru 1 to determine the accuracy of the algorithm's decision.

Plotting using increasing integer values on the x-axis would not make much sense since going up by half a step is not intuitive. Popular music is usually written using keys that do not have a lot of flats/sharps as they are easier to perform. Therefore, taking the key of C major (no sharps or flats) and then going up one integer value to C#/Db (seven sharps and five flats respectively) would not cluster the data in a visually appeasing way.

Instead we will use the [circle of fifths](https://en.wikipedia.org/wiki/Circle_of_fifths). We will organize the x-axis starting with 6 flats for index 0, 5 flats for index 1, and so on. When 0 flats is reached (key of C) we will add the sharps next using 1 sharp, then 2 sharps and so on, all the way to 6 sharps. Enharmonically equivalent key signatures (C#/Db and Cb/B) will be bundled together as they sound the same.

### Time Signature
Spotify's algorithm estimates the time signature of a track by measuring the number of beats in each bar (measure). This is an integer value and ranges from 3 to 7. It assumes that the denominator of the time signature is 4, so a time signature value of 3 would indicate a 3/4 time signature.

In the real world most time signatures use powers of 2 for the denominator. If the denominator is a power of 2 however we adjust the denominator by increasing the note value. For example, a time signature of 12/8 (twelve eight notes per measure) can be broken down as four 3/4 measures (three quarter notes per measure). The algorithm should provide a value of 3 in a 12/8 time signature.

Additionally there are irrational time signatures but these are beyond the scope of this project. This is mosly found in the classical realm and avant-garde music.

### Tempo
An integer for the tempo value is returned for the song which corresponds to the beats per minute (BPM) of the song.

### Mode
[Modern musical modes](https://en.wikipedia.org/wiki/Mode_(music)) are used throughout compositions, however Spotify's algorithm recognizes only two: major (Ionian) and minor (Aeolian).

## Method

### Data Selection
Use Spotify's "All Out XXs" from 1950s till 2010s. Retrieve each playlist's ID.

### Data Mining
Spotify's API.

### Playlist Capture
Each Spotify playlist has an identifier. Will use API call to get the track IDs for each playlist.

### Track Information
Retrieve desired information through API calls and save to a csv file.

### Data Wrangling
Review csv file.
