from typing import BinaryIO
from services.transcription_service import transcribe
from services.report_structuring import structure_report

def generate_report(filename: str, audio_file: BinaryIO) -> str:
    transcript = transcribe(filename, audio_file)
    report = structure_report(transcript)

    return {
        "raw_transcript": transcript,
        "structured_report": report,
    }