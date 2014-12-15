'''
Some helpers for a midi track
:) for instance... I always forget to add the midi.EndOfTrackEvent()
'''
import midi

class Track(midi.Track):
    default_track_name_ct = 0
    def __init__(self, name=None):
        if name is None:
            name = 'Track {}'.format(self.default_track_name_ct)
            self.default_track_name_ct += 0

        super(Track, self).append(
            midi.TrackNameEvent(text=name)
        )

        #now add the closing event
        super(Track, self).append(
            midi.EndOfTrackEvent()
        )

    def __iadd__(self, other):
        eote = self.pop()
        self = super(Track, self).__iadd__(other)
        super(Track, self).append(eote)
        return self

    def append(self, itm):
        eote = self.pop()
        super(Track, self).append(itm)
        return super(Track, self).append(eote)

    def extend(self, other):
        eote = self.pop()
        self = super(Track, self).__iadd__(other)
        super(Track, self).append(eote)

