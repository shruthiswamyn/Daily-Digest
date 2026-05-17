import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from podcaster.tools.custom_tool import openai_voice_tool

if __name__ == "__main__":
    filename = openai_voice_tool("Hello, this is my podcast intro!")
    print("Generated audio file:", filename)
