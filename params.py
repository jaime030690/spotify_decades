# Dict with key signatures. Values correspond to Spotify's API response for key signature.
# Keys are made up of a list where index 0 corresponds to the most common term for the key signature in the minor mode; index 1 corresponds to the major.
key_signatures = {
    0: ['C', 'C'],
    1: ['C#', 'C#/Db'],
    2: ['D', 'D'],
    3: ['D#/Eb', 'Eb'],
    4: ['E', 'E'],
    5: ['F', 'F'],
    6: ['F#', 'F#/Gb'],
    7: ['G, ''G'],
    8: ['G#/Ab', 'Ab'],
    9: ['A', 'A'],
    10: ['A#/Ab', 'Bb'], 
    11: ['B', 'B']
}

# Dict with modes. Values correspond to Spotify's API response for mode.
modes = {
    0: 'minor',
    1: 'major'
}