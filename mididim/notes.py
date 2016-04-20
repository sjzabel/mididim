import math

def make_notes_file():
    '''
    in case for whatever reason... I somehow need to remake this
    '''
    lines = []
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
            value = (12 * octave) + semitone
            if value >= 128:
               continue

            variable_name = "{}{}".format(name,octave - 1)
            english_name = variable_name.replace('s', '#')

            frequency = 440.0 * math.pow(
                2.0, (
                    (value - 69)/12
                )
            )
            lines.append(
                "{variable_name} = {{'name': '{english_name}', 'octave': {octave}, 'value': {value}, 'frequency': {frequency} }}".format(
                    variable_name=variable_name,
                    english_name=english_name,
                    octave=octave-1,
                    value=value,
                    frequency=frequency
                )
            )
    return lines
