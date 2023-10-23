from piano_transcription_inference import PianoTranscription, sample_rate, load_audio

# Load audio
filename = '../recordings/maestro-2004-MIDI-Unprocessed_XP_22_R2_2004_01_ORIG_MID--AUDIO_22_R2_2004_04_Track04_wav.wav'
(audio, _) = load_audio(filename, sr=sample_rate, mono=True)

# Transcriptor
transcriptor = PianoTranscription(device='cuda')    # 'cuda' | 'cpu'

# Transcribe and write out to MIDI file
transcribed_dict = transcriptor.transcribe(audio, 'transcribed.mid')