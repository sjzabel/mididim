'''
Utilities for ticks/beats
'''

'''
Near as I can tell there are 24 clock 248 messages per quarter note
hmmm... depends on scale it appears

nope seems like 24 is for rt playback? and something like 240 for pattern definition
'''
TPB = TICKS_PER_BEAT = PULSES_PER_QUARTER_NOTE = 24.0

WHOLE_NOTE = WN = 4 * TPB            # 96
HALF_NOTE = HN = 2 * TPB             # 48
QUARTER_NOTE = QN = TPB              # 24
EIGHTH_NOTE = EN = .5 * TPB          # 12
SIXTEENTH_NOTE = SN = .25 * TPB      # 6
THIRTYSECOND_NOTE = TN = .125 * TPB  # 3
SIXTYFORTH_NOTE = SFN = 0.0625 * TPB # 1.5
