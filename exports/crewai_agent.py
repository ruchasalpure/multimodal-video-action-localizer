from crewai import Agent

multimodal_video_action_localizer = Agent(
    role="Multimodal Video Action Localizer",
    goal="Deliver high-precision autonomous Multimodal Video Action Localizer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
