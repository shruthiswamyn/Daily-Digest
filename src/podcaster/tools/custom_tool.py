import os
import datetime
import wave
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool, tool
from crewai_tools import FileWriterTool, FileReadTool, SerperDevTool
from openai import OpenAI

# Utility to save audio as .wav
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

# Example custom tool schema
class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        return "this is an example of a tool output, ignore it and move along."

# Built‑in tools
file_writer_tool = FileWriterTool()
file_read_tool = FileReadTool()
search_tool = SerperDevTool()

# OpenAI TTS voice tool, now decorated so CrewAI can use it
@tool
def openai_voice_tool(script: str) -> str:
    """
    Generate a voice for the text using OpenAI TTS.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",   # voices: alloy, aria, verse, etc.
        input=script
    )

    audio_bytes = response.read()

    output_dir = os.path.join(os.getcwd(), "outputs")
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = os.path.join(output_dir, f"podcast-{timestamp}.wav")

    wave_file(filename, audio_bytes)
    return filename
