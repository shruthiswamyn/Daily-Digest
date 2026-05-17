SARVAGNA: Your Daily Digest 🎙️
Welcome to SARVAGNA, your daily AI‑powered podcast digest — developed by Shruthi.
This project builds upon the crewAI framework to orchestrate intelligent multi‑agent collaboration for generating, curating, and publishing audio digests on AI, manufacturing, and industrial technology.

The goal is to make SARVAGNA a seamless, automated system that transforms research insights into engaging podcast episodes.

⚙️ Installation
Ensure you have Python ≥3.10 <3.14 installed.
This project uses UV for dependency management and package handling.

Install UV:

bash
pip install uv
Then navigate to your project directory and install dependencies:

(Optional) Lock and install via CLI:

bash
crewai install
🧩 Setup
Create a .env file at the project root and add:

Code
MODEL=gpt-4.1-mini-2025-04-14
OPENAI_API_KEY=sk-
GEMINI_API_KEY=
SERPER_API_KEY=
Obtain API keys:

OpenAI

Gemini

Serper

🚀 Running the Project
To generate your daily digest and assemble the AI agents:

bash
crewai run
This command initializes the SARVAGNA Crew, orchestrating agents to produce podcast content and save the output in the outputs/ folder.

The default configuration creates a report.md and .wav audio files summarizing daily insights.

🛠️ Customization
Edit src/podcaster/config/agents.yaml → define your agents

Edit src/podcaster/config/tasks.yaml → define your tasks

Edit src/podcaster/crew.py → add logic, tools, and parameters

Edit src/podcaster/main.py → customize input flow and execution

🌐 Streamlit Frontend
The project includes a Streamlit demo app (app.py) that displays:

A branded banner: SARVAGNA — Your Daily Digest

Author credit: Developed by Shruthi

Audio player interface for generated episodes

Run locally:

bash
streamlit run app.py
Deploy publicly via Streamlit Cloud.