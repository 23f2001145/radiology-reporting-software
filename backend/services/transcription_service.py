from openai import OpenAI
from dotenv import load_dotenv
from typing import BinaryIO

load_dotenv()

client = OpenAI()  # automatically reads OPENAI_API_KEY from environment

def transcribe(filename: str, audio_file: BinaryIO) -> str:
    try:

        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=(filename, audio_file)
        )
        return transcript.text
    
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}")