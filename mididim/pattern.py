import midi

'''
480 - 240 - 120 - 60 - 30 - 15 
1/4   1/8   1/16  1/32 1/64 1/128

TODO: meebe multiples of 2 are better
512 - 256 - 128 - 64 - 32 - 16 - 8 - 4 - 2

maybe should base on time sig? 
ala 3/4 might be better as multiples of 3
7/8 as 7
9/8 as 9
5/4 as 5

'''

def get_default_44_pattern(name="Default 4/4 Pattern", bpm=120):
    return midi.Pattern(format=1, resolution=6**5, tracks=[
        [
            midi.TrackNameEvent(tick=0, text=name),
            midi.TimeSignatureEvent(tick=0, data=[4, 2, 24, 8]),
            midi.SetTempoEvent(tick=0, bpm=bpm),
            midi.EndOfTrackEvent(),
        ]
    ])

