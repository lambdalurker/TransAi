from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source="https://youtu.be/1ItQnh3LWeg?si=GYi8ZB_2iLI5-DAx"

chunks= process_input(source)

print(transcribe_all(chunks))
