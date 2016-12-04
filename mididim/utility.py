import mido

mido.set_backend('mido.backends.rtmidi')

# control_surface_input_0 = mido.open_input('control_surface_input_0', virtual=True)
# control_surface_output_0 = mido.open_output('control_surface_output_0', virtual=True)
# 
# keyboard_input_0 = mido.open_input('keyboard_input_0', virtual=True)
# keyboard_output_0 = mido.open_output('keyboard_output_0', virtual=True)

instrument_input_0 = mido.open_input('instrument_input_0', virtual=True)
instrument_output_0 = mido.open_output('instrument_output_0', virtual=True)

