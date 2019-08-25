from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import mediainfo

audio_path = "resouces/the_speech_that_made_obama_president.mp3"
#audio_path = 'resouces/the_speech_that_made_obama_president.wav'

audio_fmt = audio_path.split('.')[-1]

audio = None
try:
    audio = AudioSegment.from_file(audio_path, format=audio_fmt)
except:
    print('failed to load audio file')

if audio:
    audio_info = mediainfo(audio_path)
    print('filename', audio_info['filename'])
    print('codec', audio_info['codec_name'])
    print('size', audio_info['size'])
    print('sample_rate', audio_info['sample_rate'])
    print('channels', audio_info['channels'])
    print('sample_fmt', audio_info['sample_fmt'])
    print('bits_per_sample', audio_info['bits_per_sample'])
    
    print('duration (secs): ', audio.duration_seconds)
    #play(audio)

    filename = audio_info['filename'].split('.')[0]
    duration = audio.duration_seconds
    num_of_parts = int (round(duration / 60, 0))
    print('num_of_parts:', num_of_parts)

    audios = []
    for i in range(num_of_parts):
        head = i * 60 * 1000
        tail = (i+1) * 60 * 1000
        part = audio[head:tail]
        part_filename = '{}_{}.{}'.format(filename, str(i), audio_fmt)
        print(part_filename)
        part.export(part_filename, format=audio_fmt)
