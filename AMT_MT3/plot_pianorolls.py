import matplotlib.pyplot as plt
import numpy as np
import pretty_midi as pm

# Load MIDI file into PrettyMIDI object
midi_targ = pm.PrettyMIDI('recordings/Slakh2100-Track01895-all_src.mid')
midi_pred = pm.PrettyMIDI('recordings/Slack2100-Track01895-transcribed.mid')

def get_instruments(midi_data):
    instruments_set = set()
    for inst in midi_data.instruments:
        if len(inst.notes) > 0:
            instruments_set.add(midi_program_to_class(inst.program))
    return instruments_set

def midi_program_to_class(midi_program):
    if midi_program in range(0, 8):
        return 'Piano'
    elif midi_program in range(8, 16):
        return 'Chromatic Percussion'
    elif midi_program in range(16, 24):
        return 'Organ'
    elif midi_program in range(24,32):
        return 'Guitar'
    elif midi_program in range(32,40):
        return 'Bass'
    elif midi_program in range(40,48):
        return 'Strings'
    elif midi_program in range(48,56):
        return 'Ensemble'
    elif midi_program in range(56,64):
        return 'Brass'
    elif midi_program in range(64,72):
        return 'Reed'
    elif midi_program in range(72,80):
        return 'Pipe'
    elif midi_program in range(80,88):
        return 'Synth Lead'
    elif midi_program in range(88,96):
        return 'Synth Pad'
    elif midi_program in range(96,104):
        return 'Synth Effects'
    elif midi_program in range(104,112):
        return 'Ethnic'
    elif midi_program in range(112,120):
        return 'Percussive'
    elif midi_program in range(120,128):
        return 'Sound Effects'

inst_set_targ = get_instruments(midi_targ)
inst_set_pred = get_instruments(midi_pred)
inst_set_targ.remove('Ensemble')
inst_set_targ.remove('Brass')

def get_piano_roll_by_inst(midi_data, instrument):
    pr = np.zeros((128, int(midi_data.get_end_time() * 100)))

    for inst in midi_data.instruments:
        if midi_program_to_class(inst.program) != instrument: continue

        for note in inst.notes:
            pr[note.pitch, int(note.start * 100):int(note.end * 100)] = inst.program
                
    return pr

# Get piano rolls for both MIDI files and plot
plt.figure(figsize=(20,10))

for i, instrument in enumerate(inst_set_targ):
    pr_targ = get_piano_roll_by_inst(midi_targ, instrument)
    pr_pred = get_piano_roll_by_inst(midi_pred, instrument)

    plt.subplot(len(inst_set_targ), 2, i*2+1)
    plt.imshow(pr_targ[21:109, 500:1000], origin='lower', aspect='auto', cmap='twilight')
    plt.title('Ground Truth ' + instrument)

    plt.subplot(len(inst_set_targ), 2, i*2+2)
    plt.imshow(pr_pred[21:109, 500:1000], origin='lower', aspect='auto', cmap='twilight')
    plt.title('Transcribed ' + instrument)

plt.tight_layout()
plt.savefig('pianorolls.png')
