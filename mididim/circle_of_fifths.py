'''
The circle of fifths is a useful tool for determining the various chord within a progression based on key

Much of what I have learned about the circle of 5ths and how to code for it is from
Rand Scullard's excellent JS app http://randscullard.com/CircleOfFifths/ 
(It is very useful and well done)
'''
#  The currently selected tonic in the tonic table.
default_tonic = "C"

#  The currently selected mode in the mode table.
default_mode = "ionian"

#  This is for computer consumption... so we will never s'see' Rands css
position_cord_type = [
    'major',
    'major',
    'major',
    'minor',
    'minor',
    'minor',
    'diminished'
]

#  Hash table of key signatures, where the key is the number of sharps (positive) or flats (negative).
#  The value is an array of note names in the key signature, starting at the 1: 00 clock position
#  and ending at the 12: 00 position.
key_signatures_d = {
    "-13":  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Cbb", "Gbb", "Dbb" ],
    "-12":  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "Gbb", "Dbb" ],
    "-11":  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "Dbb" ],
    "-10":  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-9" :  [ "G",   "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-8" :  [ "G",   "D",   "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-7" :  [ "G",   "D",   "A",   "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-6" :  [ "G",   "D",   "A",   "E",   "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-5" :  [ "G",   "D",   "A",   "E",   "B",   "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-4" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-3" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-2" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    "-1" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
     "0" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
     "1" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
     "2" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "Ab", "Eb", "Bb",  "F",   "C"   ],
     "3" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "Eb", "Bb",  "F",   "C"   ],
     "4" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "Bb",  "F",   "C"   ],
     "5" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "F",   "C"   ],
     "6" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "C"   ],
     "7" :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     "8" :  [ "F##", "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     "9" :  [ "F##", "C##", "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     "10":  [ "F##", "C##", "G##", "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     "11":  [ "F##", "C##", "G##", "D##", "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     "12":  [ "F##", "C##", "G##", "D##", "A##", "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     "13":  [ "F##", "C##", "G##", "D##", "A##", "E##", "C#", "G#", "D#", "A#",  "E#",  "B#"  ]
}

#  Array of scale degrees in the Lydian mode, starting at the first note position on the
#  circle and proceeding clockwise. Modes other than Lydian are simply rotations of this array by
#  the number of steps specified by mode_info_d.counter_clockwise_offset
degrees_li = [1, 5, 2, 6, 3, 7, 4]

#  Hash table of information on each tonic that can be selected by the user, where the key is
#  the tonic itself, and the value has two pieces of info:  clock_position is the clock position on the
#  circle where the notes of the Lydian mode begin for that tonic. key_signature_id is the key signature
#  in the key_signatures_d table for that tonic in the Lydian mode. (The mode_info_d table
#  is used to translate this info into modes other than Lydian.)
tonic_info_d = {
    "B#":  {'clock_position': 12, 'key_signature_id': 13 },
    "E#":  {'clock_position': 11, 'key_signature_id': 12 },
    "A#":  {'clock_position': 10, 'key_signature_id': 11 },
    "D#":  {'clock_position': 9,  'key_signature_id': 10 },
    "G#":  {'clock_position': 8,  'key_signature_id': 9  },
    "C#":  {'clock_position': 7,  'key_signature_id': 8  },
    "F#":  {'clock_position': 6,  'key_signature_id': 7  },
    "B" :  {'clock_position': 5,  'key_signature_id': 6  },
    "E" :  {'clock_position': 4,  'key_signature_id': 5  },
    "A" :  {'clock_position': 3,  'key_signature_id': 4  },
    "D" :  {'clock_position': 2,  'key_signature_id': 3  },
    "G" :  {'clock_position': 1,  'key_signature_id': 2  },
    "C" :  {'clock_position': 12, 'key_signature_id': 1  },
    "F" :  {'clock_position': 11, 'key_signature_id': 0  },
    "Bb":  {'clock_position': 10, 'key_signature_id': -1 },
    "Eb":  {'clock_position': 9,  'key_signature_id': -2 },
    "Ab":  {'clock_position': 8,  'key_signature_id': -3 },
    "Db":  {'clock_position': 7,  'key_signature_id': -4 },
    "Gb":  {'clock_position': 6,  'key_signature_id': -5 },
    "Cb":  {'clock_position': 5,  'key_signature_id': -6 },
    "Fb":  {'clock_position': 4,  'key_signature_id': -7 }
}

#  Hash table of information on each mode that can be selected by the user, where the key is
#  the mode itself, and the counter_clockwise_offset value has the number of steps counterclockwise around
#  the circle where the mode begins, relative to Lydian. For example, if the Lydian begins
#  at 3: 00, then the Mixolydian of the same tonic begins at 1: 00.
mode_info_d = {
    "lydian"     :   { 'offset':  0 },
    "ionian"     :   { 'offset': -1 },
    "mixolydian" :   { 'offset': -2 },
    "dorian"     :   { 'offset': -3 },
    "aeolian"    :   { 'offset': -4 },
    "phrygian"   :   { 'offset': -5 },
    "locrian"    :   { 'offset': -6 }
}


def get_info(tonic=default_tonic, mode=default_mode):
    if not tonic in tonic_info_d:
        raise Exception("Please use one of the following tonics ['{}']".format("', '".join(tonic_info_d.keys())))
    tonic_info = tonic_info_d[tonic]

    if not mode in mode_info_d:
        raise Exception("Please use one of the following modes ['{}']".format("', '".join(mode_info_d.keys())))
    mode_info = mode_info_d[mode]

    #  I suspect that this is no longer needed and that we could use the most common
    #   names internally
    note_names = key_signatures_d[
        tonic_info['key_signature_id']
    ]
