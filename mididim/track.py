'''
Some helpers for a midi track
:) for instance... I always forget to add the midi.EndOfTrackEvent()

'''
import midi

class Track(midi.Track):
    '''
    Track is a convienence class derived from midi.Track

    it initializes the track with
    1. a TrackNameEvent
    2. a EndOfTrackEvent
    then maintains the the EOT event as the last item
    '''

    default_track_name_ct = 0

    def __init__(self, name=None):
        super(Track, self).__init__()
        if name is None:
            name = 'Track {}'.format(self.default_track_name_ct)
            self.default_track_name_ct += 0

        super(Track, self).append(
            midi.TrackNameEvent(data=name)
        )

        #now add the closing event
        super(Track, self).append(
            midi.EndOfTrackEvent()
        )

    def __iadd__(self, other):
        '''
        __iadd__s to the note list; leaving the EOT event as the last event

        > track[TNE, n1, n2, n3, EOT] += event4
          track[TNE, n1, n2, n3, event4, EOT]
        or
        > track[TNE, n1, n2, n3, EOT] += [nOn4, nOff5]
          track[TNE, n1, n2, n3, nOn4, nOff5, EOT]
        '''
        eote = self.pop()
        self = super(Track, self).__iadd__(other)
        super(Track, self).append(eote)
        return self

    def append(self, itm):
        '''
        appends to the note list; leaving the EOT event as the last event

        > track[TNE, n1, n2, n3, EOT].append(event4)
          track[TNE, n1, n2, n3, event4, EOT]
        '''
        eote = self.pop()
        super(Track, self).append(itm)
        return super(Track, self).append(eote)

    def extend(self, other):
        '''
        extends the note list; leaving the EOT event as the last event

        > track[TNE, n1, n2, n3, EOT].extent([nOn4, nOff5])
          track[TNE, n1, n2, n3, nOn4, nOff5, EOT]
        '''
        eote = self.pop()
        self = super(Track, self).__iadd__(other)
        super(Track, self).append(eote)

    def union(self, track):
        '''
        unions this track to another track using absolute tick and pitch

        keeping the Name and EOT events

        > track[TNE.default_1, nOn.tick_0.pitch_C0, nOff.tick_200.pitch_C0, EOT].union(
            track[TNE.default_2, nOn.tick_100.pitch_C1, nOff.tick_200.pitch_C1, EOT]
            )
          track[TNE.default_1, nOn.tick_0.pitch_C0, nOn.tick_100.pitch_C1,
                nOff.tick_100.pitch_C0, nOff.tick_100.pitch_C1, EOT]
        '''
        pass

