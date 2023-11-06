#/bin/bash

# pip install piano_transcription_inference

audio_file="/import/c4dm-05/ll307/repositories/demos/AMT_high_res_piano_transcription/recordings/J.S._Bach_-_Toccata_and_Fugue_in_D_Minor_BWV_565_Amy_Turk_Harp.mp3"
output_file=$audio_file".transcribed.mid"

python3 transcribe.py --audio_file $audio_file --output_file $output_file --device cuda