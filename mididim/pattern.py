import midi

'''
Helper functions for generating a midi.Pattern and adding track0 with the correct information.
'''
from mididim.rhythm import BASE_RESOLUTION

def get_default_44_pattern(name="Default 4/4 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=4, time_signature_denominator=2)


def get_default_34_pattern(name="Default 3/4 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=3, time_signature_denominator=2)


def get_default_54_pattern(name="Default 5/4 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=5, time_signature_denominator=2)


def get_default_68_pattern(name="Default 6/8 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=6, time_signature_denominator=3)


def get_default_78_pattern(name="Default 7/8 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=7, time_signature_denominator=3)


def get_default_88_pattern(name="Default 8/8 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=8, time_signature_denominator=3)


def get_default_98_pattern(name="Default 9/8 Pattern", bpm=120):
    return get_pattern(name=name, bpm=bpm, time_signature_numerator=9, time_signature_denominator=3)


def get_pattern(name="Default Pattern", bpm=120, time_signature_numerator=4, time_signature_denominator=2, resolution=BASE_RESOLUTION):
    '''
    name
    bpm=120
    time_signature_numerator
    time_signature_denominator: this is used as 2 ** time_signature_denominator

    so 
    tsn=4 tsd=2 evaluates out to 4/4 time
    tsn=5 tsd=3 evaluates out to 5/8 time
    '''
    return midi.Pattern(format=1, resolution=resolution, tracks=[
        [
            midi.TrackNameEvent(tick=0, text=name),
            # midi.TimeSignatureEvent(tick=0, data=[time_signature_numerator, 2**time_signature_denominator, 24, 8]),
            midi.TimeSignatureEvent(tick=0, data=[time_signature_numerator, time_signature_denominator, 24, 8]),
            midi.SetTempoEvent(tick=0, bpm=bpm),
            midi.EndOfTrackEvent(),
        ]
    ])
