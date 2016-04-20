'''
Chord definitions
'''
from mido import Message

class AbstractChord(object):
    def __init__(self, root, key=None):
        self._root = root
        self._key = key

    def note_on(self, time=0, velocity=64, pattern=None):
        '''
        pattern is an opening for things like strums, fingerpicking and arpeggios
        pattern must yeild
        '''
        if pattern is not None:
            return pattern(self, time=time, velocity=velocity)

        rslt = []
        for offset in self.asc:
            rslt.append(
                    Message('note_on', time=time, velocity=velocity, note=self._root + offset)
            )
            time = 0
        return rslt

    def note_off(self, time=0, pattern=None):
        '''
        pattern is an opening for things like strums, fingerpicking and arpeggios
        pattern must yeild
        '''
        if pattern is not None:
            return pattern(self, time=time, velocity=velocity)

        rslt = []
        for offset in self.asc:
            rslt.append(
                Message('note_off', velocity=0, time=time, note=self._root + offset)
            )
            time = 0

        return rslt

class Major(AbstractChord):
    '''
    Major 1-3-5
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2     3  4     5     6     7  R
    '''
    asc = [0, 4, 7]
    desc = [7, 4, 0]

class Minor(AbstractChord):
    '''
    Minor 1-b3-5
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2  b3    4     5     6     7  R
    '''
    asc = [0, 3, 7]
    desc = [7, 3, 0]

class Diminished(AbstractChord):
    '''
    Diminished 1-b3-b5
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2  b3    4  b5       6     7  R
    '''
    asc = [0, 3, 6]
    desc = [6, 3, 0]

class MajorSeventh(AbstractChord):
    '''
    MajorSeventh 1-3-5-7
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2     3  4     5     6     7  R
    '''
    asc = [0, 4, 7, 11]
    desc = [11, 7, 4, 0]

class DominantSeventh(AbstractChord):
    '''
    DominantSeventh 1-3-5-b7
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2     3  4     5     6 b7     R
    '''
    asc = [0, 4, 7, 10]
    desc = [10, 7, 4, 0]

class MinorSeventh(AbstractChord):
    '''
    MinorSeventh 1-b3-5-b7
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2 b3     4     5     6 b7     R
    '''
    asc = [0, 3, 7, 10]
    desc = [10, 7, 3, 0]

class MinorSeventhFlatFive(AbstractChord):
    '''
    MinorSeventh 1-b3-b5-b7
        1  2  3  4  5  6  7  8  9 10 11 12 13
    b0  0  1  2  3  4  5  6  7  8  9 10 11 12
        R     2 b3     4 b5        6 b7     R
    '''
    asc = [0, 3, 6, 10]
    desc = [10, 6, 3, 0]


# :) I'm not delving into 9ths and 11ths now
#  TODO: delve into 9ths and 11ths
