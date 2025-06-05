from google.adk.agents import Agent


class TravelPlannerAgent(Agent):
    def _init_(self, *args, max_tokens=200, **kwargs):
        super()._init_(*args, **kwargs)
        self.max_tokens = max_tokens

    def generate_response(self, prompt: str) -> str:
        response = super().generate_response(
            prompt,
            max_output_tokens=self.max_tokens,
            temperature=0.7,
        )
        return response


travel_agent = TravelPlannerAgent(
    model="gemini-2.0-flash-001",
    name="travel_agent",
    description="A helpful travel planning assistant that provides personalized recommendations.",
    max_tokens=200,  # Increased token limit for detailed travel plans
    instruction="""
    Act as a knowledgeable travel planner and provide focused travel recommendations:
    - Ask for key details like destination, duration, budget, and interests
    - Suggest specific attractions, restaurants, and activities
    - Include practical tips about transportation and accommodation
    - Consider seasonal factors and local customs
    - Provide estimated costs when possible
    - Break down recommendations by days/categories
    - Keep suggestions concise but informative
    """,
)