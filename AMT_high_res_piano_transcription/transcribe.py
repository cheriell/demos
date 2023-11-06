from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import argparse



if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--audio_file', type=str, required=True)
    arg_parser.add_argument('--output_file', type=str, required=True)
    arg_parser.add_argument('--device', type=str, default='cuda')
    args = arg_parser.parse_args()

    # Check arguments
    assert args.device in ['cuda', 'cpu']

    # Load audio
    (audio, _) = load_audio(args.audio_file, sr=sample_rate, mono=True)

    # Transcriptor
    transcriptor = PianoTranscription(device=args.device)    # 'cuda' | 'cpu'

    # Transcribe and write out to MIDI file
    transcribed_dict = transcriptor.transcribe(audio, args.output_file)