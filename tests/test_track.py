import unittest
import midi
from mididim.chord import Major
from mididim.track import Track
from mididim.pitch import pitch2n as pitch

class TestTrack(unittest.TestCase):
    def setUp(self):
        print "Within setUp"
        self.C = Major(pitch.C_0)
        self.track1 = Track(name='Test_0')

    def tearDown(self):
        print "Within tearDown"

    def test_track_name(self):
        evt0 = self.track1[0]
        self.assertIsInstance(evt0, midi.TrackNameEvent)
        self.assertEqual(evt0.text, 'Test_0')

    def test_track_eof(self):
        evt0 = self.track1[-1]
        self.assertIsInstance(evt0, midi.EndOfTrackEvent)
        self.assertEqual(evt0.tick, 0)


