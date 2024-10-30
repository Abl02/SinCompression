from pydub import AudioSegment
import sys


# Load your MP3 file
sound = AudioSegment.from_mp3(sys.argv[1])
# Export it as a WAV file
sound.export(sys.argv[2], format="wav")
