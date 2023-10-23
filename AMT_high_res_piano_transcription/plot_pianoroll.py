import matplotlib.pyplot as plt
import numpy as np
import pretty_midi as pm

# Load MIDI file into PrettyMIDI object
midi_targ = pm.PrettyMIDI('../recordings/maestro-2004-MIDI-Unprocessed_XP_22_R2_2004_01_ORIG_MID--AUDIO_22_R2_2004_04_Track04_wav.midi')
midi_pred = pm.PrettyMIDI('transcribed.mid')

# Get piano rolls for both MIDI files
pr_targ = midi_targ.get_piano_roll(fs=100)
pr_pred = midi_pred.get_piano_roll(fs=100)

# Plot piano rolls
plt.figure(figsize=(8,8))
plt.subplot(211)
plt.imshow(pr_targ[21:109,500:1000], origin='lower', aspect='auto', cmap='twilight')
plt.title('Target')
plt.subplot(212)
plt.imshow(pr_pred[21:109,500:1000], origin='lower', aspect='auto', cmap='twilight')
plt.title('Prediction')
plt.tight_layout()
plt.savefig('pianorolls.png')
