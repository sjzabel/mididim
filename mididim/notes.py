import math

class Note(object):
    def __init__(self, name, octave, midi_value, semitone, frequency):
        self.name = name
        self.octave = octave
        self.midi_value = midi_value
        self.semitone = semitone
        self.frequency = frequency

    def __repr__(self):
        return self.name

    def __str__(self):
        return midi_value

class Notes(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._populate_notes()
    def __getattr__(self, addr_nm):
        return self[addr_nm]

    def _populate_notes(self):
        '''
        in case for whatever reason... I somehow need to remake this
        '''
        for octave in range(0, 11):
            for name, semitone in [
                   ('C', 0),
                   ('Cs', 1),
                   ('Db', 1),
                   ('D', 2),
                   ('Ds', 3),
                   ('Eb', 3),
                   ('E', 4),
                   ('F', 5),
                   ('Fs', 6),
                   ('Gb', 6),
                   ('G', 7),
                   ('Gs', 8),
                   ('Ab', 8),
                   ('A', 9),
                   ('As', 10),
                   ('Bb', 10),
                   ('B', 11)
               ]:
                midi_value = (12 * octave) + semitone
                if midi_value >= 128:
                   continue

                variable_name = "{}{}".format(name, octave)
                english_name = variable_name.replace('s', '#')

                frequency = 440.0 * math.pow(
                    2.0, (
                        (midi_value - 69)/12
                    )
                )
                self[variable_name] = Note(
                    name=english_name,
                    octave=octave-1,
                    midi_value=midi_value,
                    semitone=semitone,
                    frequency=frequency
                )
