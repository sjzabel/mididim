'''
Rhythm helpers
'''
import midi


BASE_RESOLUTION = (2 ** 6) * 3


class AbstractTimeUnit(object):
    unit_multiplier = -1

    def __init__(self):
        self._dots = 0
        self._tick = round(self.unit_multiplier * BASE_RESOLUTION)

    def dot(self):
        '''
        A dot adds 1/2 of the prior unit
        ala
        . + 1/2
        .. + 1/2 + 1/4
        ... + 1/2 + 1/4 + 1/8
        '''
        self._dots += 1
        print 'dot: {}'.format(self._dots)

        return self

    def sum_dots(self):
        if self.dots is not 0:
            return sum([self._tick/(2**i) for i in xrange(1, self._dots +1)])

        return 0

    def get_tick(self):
        return self._tick + self.sum_dots()


class AbstractRest(AbstractTimeUnit):
    pass


class AbstractNote(AbstractTimeUnit, list):
    def __init__(self, pitch, velocity=100):
        self.dots = 0
        self.pitch = pitch
        self.velocity = velocity


    def __iter__(self):
        print '__iter__'

        len_of_note = self.get_tick()

        if hasattr(pitch, 'asc'):
            # turn notes on
            for offset in pitch.asc:
                self.append(
                    midi.NoteOnEvent(tick=0, velocity=velocity, pitch=pitch._root + offset)
                )

            # turn notes off
            for offset in pitch.asc:
                self.append(
                    midi.NoteOffEvent(tick=len_of_note, pitch=pitch._root + offset)
                )
                # we want to turn off all of the remaining notes right away
                len_of_note = 0

        else:
            # turn notes on
            self.append(
                midi.NoteOnEvent(tick=0, velocity=velocity, pitch=pitch)
            )

            # turn notes off
            self.append(
                midi.NoteOffEvent(tick=len_of_note, pitch=pitch)
            )

        return super(AbstractNote, self).__iter__()


class WholeNote(AbstractNote):
    unit_multiplier = 4.0


class HalfNote(AbstractNote):
    unit_multiplier = 2.0


class QuarterNote(AbstractNote):
    unit_multiplier = 1.0


class QuarterNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / 3


class EigthNote(AbstractNote):
    unit_multiplier = 1.0 / (2 ** 1)


class EigthNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / ((2 ** 1) * 3)


class SixteenthNote(AbstractNote):
    unit_multiplier = 1.0 / (2 ** 2)


class SixteenthNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / ((2 ** 2) * 3)


class ThirtySecondNote(AbstractNote):
    unit_multiplier = 1.0 / (2 ** 3)


class ThirtySecondNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / ((2 ** 3) * 3)


class SixtyForthNote(AbstractNote):
    unit_multiplier = 1.0 / (2 ** 4)


class SixtyForthNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / ((2 ** 4) * 3)


class OneHundredTwentyEightNote(AbstractNote):
    unit_multiplier = 1.0 / (2 ** 5)


class OneHundredTwentyEightNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / ((2 ** 5) * 3)


class TwoHundredFiftyForthNote(AbstractNote):
    unit_multiplier = 1.0 / (2 ** 6)


class TwoHundredFiftyForthNoteTriplet(AbstractNote):
    unit_multiplier = 1.0 / ((2 ** 6) * 3)


# Rests
class WholeRest(AbstractRest):
    unit_multiplier = 4.0


class HalfRest(AbstractRest):
    unit_multiplier = 2.0


class QuarterRest(AbstractRest):
    unit_multiplier = 1.0


class QuarterRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / 3


class EigthRest(AbstractRest):
    unit_multiplier = 1.0 / (2 ** 1)


class EigthRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / ((2 ** 1) * 3)


class SixteenthRest(AbstractRest):
    unit_multiplier = 1.0 / (2 ** 2)


class SixteenthRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / ((2 ** 2) * 3)


class ThirtySecondRest(AbstractRest):
    unit_multiplier = 1.0 / (2 ** 3)


class ThirtySecondRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / ((2 ** 3) * 3)


class SixtyForthRest(AbstractRest):
    unit_multiplier = 1.0 / (2 ** 4)


class SixtyForthRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / ((2 ** 4) * 3)


class OneHundredTwentyEightRest(AbstractRest):
    unit_multiplier = 1.0 / (2 ** 5)


class OneHundredTwentyEightRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / ((2 ** 5) * 3)


class TwoHundredFiftyForthRest(AbstractRest):
    unit_multiplier = 1.0 / (2 ** 6)


class TwoHundredFiftyForthRestTriplet(AbstractRest):
    unit_multiplier = 1.0 / ((2 ** 6) * 3)
