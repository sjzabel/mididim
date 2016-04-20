'''
The circle of fifths is a useful tool for determining the various chord within a progression based on key

Much of what I have learned about the circle of 5ths and how to code for it is from
Rand Scullard's excellent JS app http://randscullard.com/CircleOfFifths/ 
(It is very useful and well done)
'''
import collections


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
    -13:  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Cbb", "Gbb", "Dbb" ],
    -12:  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "Gbb", "Dbb" ],
    -11:  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "Dbb" ],
    -10:  [ "Abb", "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -9 :  [ "G",   "Ebb", "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -8 :  [ "G",   "D",   "Bbb", "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -7 :  [ "G",   "D",   "A",   "Fb",  "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -6 :  [ "G",   "D",   "A",   "E",   "Cb",  "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -5 :  [ "G",   "D",   "A",   "E",   "B",   "Gb",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -4 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -3 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -2 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
    -1 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
     0 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
     1 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "Db", "Ab", "Eb", "Bb",  "F",   "C"   ],
     2 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "Ab", "Eb", "Bb",  "F",   "C"   ],
     3 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "Eb", "Bb",  "F",   "C"   ],
     4 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "Bb",  "F",   "C"   ],
     5 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "F",   "C"   ],
     6 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "C"   ],
     7 :  [ "G",   "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     8 :  [ "F##", "D",   "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     9 :  [ "F##", "C##", "A",   "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     10:  [ "F##", "C##", "G##", "E",   "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     11:  [ "F##", "C##", "G##", "D##", "B",   "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     12:  [ "F##", "C##", "G##", "D##", "A##", "F#",  "C#", "G#", "D#", "A#",  "E#",  "B#"  ],
     13:  [ "F##", "C##", "G##", "D##", "A##", "E##", "C#", "G#", "D#", "A#",  "E#",  "B#"  ]
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
    "B#":  {'rotation': -11, 'clock_position': 12, 'key_signature_id': 13 },
    "E#":  {'rotation': -10, 'clock_position': 11, 'key_signature_id': 12 },
    "A#":  {'rotation': -9,  'clock_position': 10, 'key_signature_id': 11 },
    "D#":  {'rotation': -8,  'clock_position': 9,  'key_signature_id': 10 },
    "G#":  {'rotation': -7,  'clock_position': 8,  'key_signature_id': 9  },
    "C#":  {'rotation': -6,  'clock_position': 7,  'key_signature_id': 8  },
    "F#":  {'rotation': -5,  'clock_position': 6,  'key_signature_id': 7  },
    "B" :  {'rotation': -4,  'clock_position': 5,  'key_signature_id': 6  },
    "E" :  {'rotation': -3,  'clock_position': 4,  'key_signature_id': 5  },
    "A" :  {'rotation': -2,  'clock_position': 3,  'key_signature_id': 4  },
    "D" :  {'rotation': -1,  'clock_position': 2,  'key_signature_id': 3  },
    "G" :  {'rotation':  0,  'clock_position': 1,  'key_signature_id': 2  },
    "C" :  {'rotation': -11, 'clock_position': 12, 'key_signature_id': 1  },
    "F" :  {'rotation': -10, 'clock_position': 11, 'key_signature_id': 0  },
    "Bb":  {'rotation': -9,  'clock_position': 10, 'key_signature_id': -1 },
    "Eb":  {'rotation': -8,  'clock_position': 9,  'key_signature_id': -2 },
    "Ab":  {'rotation': -7,  'clock_position': 8,  'key_signature_id': -3 },
    "Db":  {'rotation': -6,  'clock_position': 7,  'key_signature_id': -4 },
    "Gb":  {'rotation': -5,  'clock_position': 6,  'key_signature_id': -5 },
    "Cb":  {'rotation': -4,  'clock_position': 5,  'key_signature_id': -6 },
    "Fb":  {'rotation': -3,  'clock_position': 4,  'key_signature_id': -7 }
}

#  Hash table of information on each mode that can be selected by the user, where the key is
#  the mode itself, and the counter_clockwise_offset value has the number of steps counterclockwise around
#  the circle where the mode begins, relative to Lydian. For example, if the Lydian begins
#  at 3: 00, then the Mixolydian of the same tonic begins at 1: 00.

#  SZABEL I'm using collection.deque so the negative number becomes positive
mode_info_d = {
    "lydian"     :   { 'offset':  0, 'rotation': 0 },
    "ionian"     :   { 'offset': -1, 'rotation': 1 },
    "major"      :   { 'offset': -1, 'rotation': 1 },
    "mixolydian" :   { 'offset': -2, 'rotation': 2 },
    "dorian"     :   { 'offset': -3, 'rotation': 3 },
    "aeolian"    :   { 'offset': -4, 'rotation': 4 },
    "minor"      :   { 'offset': -4, 'rotation': 4 },
    "phrygian"   :   { 'offset': -5, 'rotation': 5 },
    "locrian"    :   { 'offset': -6, 'rotation': 6 }
}


def get_key_info(tonic=default_tonic, mode=default_mode):
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

    #  deque note_names for rotation
    note_names = collections.deque(note_names)
    degrees = collections.deque(degrees_li)

    #  rotate notes so that tonic is in position 0
    note_names.rotate(tonic_info['rotation'])

    #  now rotate both degrees and notes by mode
    note_names.rotate(mode_info['rotation'])
    degrees.rotate(mode_info['rotation'])

    #  now write everything to a dict
    return_d = {}
    for i, degree in enumerate(degrees):
        return_d[degree] = {
            'tonic': note_names[i],
            'cord_type': position_cord_type[i]
        }

    return return_d
