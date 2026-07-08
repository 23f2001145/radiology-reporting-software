from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()  

with open("prompts/structure_reports.txt", "r") as file:
    system_prompt = file.read()

def structure_report(raw_transcript: str) -> dict: 

    try : 
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role" : "system",
                    "content" : system_prompt,
                },
                {
                    "role": "user",
                    "content": f"Structure this radiology dictation:\n\n{raw_transcript}"
                }
            ],
            temperature=0  # keep it deterministic, no creativity needed here
        )

        raw_output = response.choices[0].message.content

    except Exception as e:
        raise RuntimeError(
            f"Structuring failed :\n{e}"
        ) from e

    # parse and pretty print
    try:
        structured = json.loads(raw_output)
        return structured
        # print("\n\n\n--- STRUCTURED REPORT ---")
        # print(f"TECHNIQUE:\n{structured.get('technique', '')}\n")
        # print(f"FINDINGS:\n{structured.get('findings', '')}\n")
        # print(f"IMPRESSION:\n{structured.get('impression', '')}\n")
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Invalid JSON returned by LLM.\nRaw output:\n{raw_output}"
        ) from e