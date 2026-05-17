from crewai import Crew, Agent
from podcaster.tools import search_tool, file_writer_tool, file_read_tool, openai_voice_tool

# Define your agent with a sharper backstory
podcaster_agent = Agent(
    role="AI Manufacturing Research Podcaster",
    goal="Deliver daily research-driven updates on AI in shock absorbers, manufacturing, and industrial technology, backed by technical terms, company references, and market insights.",
    backstory=(
        "This agent hosts the 'AI Manufacturing Digest' podcast, focusing on the latest applied AI research "
        "in shock absorbers, automotive manufacturing, and industrial technology. It reports on technical breakthroughs, "
        "published studies, patents, and company innovations. Each update highlights pioneers across the world, "
        "press releases, production plans, and market trends, while also projecting the future of shock absorber technology."
    ),
    tools=[search_tool, file_writer_tool, file_read_tool, openai_voice_tool],
    verbose=True
)

# Define your crew with a multi-step pipeline
Podcaster = Crew(
    agents=[podcaster_agent],
    tasks=[
        {
            "description": "Search for the latest AI research and industry updates in shock absorbers, manufacturing, and industrial technology.",
            "agent": podcaster_agent,
            "expected_output": "A list of credible research updates, company press releases, patents, and market news."
        },
        {
            "description": "Write a 2-minute digest script using strong technical terms, company names, and references to pioneers in shock absorbers and manufacturing. Include future outlooks and production/market trends.",
            "agent": podcaster_agent,
            "expected_output": "A polished newsletter script with technical terminology, company references, and market updates."
        },
        {
            "description": "Convert the digest script into audio using OpenAI TTS.",
            "agent": podcaster_agent,
            "expected_output": "A .wav audio file containing a 1-minute spoken summary of AI research and industry updates in shock absorbers and manufacturing."
        }
    ]
)
