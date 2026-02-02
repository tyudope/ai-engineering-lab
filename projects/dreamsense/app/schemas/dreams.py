from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from pydantic import ConfigDict

class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")

# Why this schema looks like this (quick but important)
# 	•	Min/max lengths: protects your API (and OpenAI spend) + ensures meaningful input.
# 	•	InsightTag: UI-friendly “chips” (label + confidence) without pretending it’s scientific.
# 	•	confidence: helps tone-down authority (“low/medium/high” instead of numeric).
# 	•	reflection_questions and feedback: forces the model to produce actionable output

# Request
class DreamAnalyzeRequest(StrictModel):

    dream_text:str = Field(
        ...,
        min_length = 20,
        max_length = 4000,
        description = "User's dream description in natural language."
    )


    user_context: Optional[str] = Field(
        default = None,
        max_length = 1000,
        description = "Optional waking-life context (stressors, events, mood)."
    )

    intensity:int = Field(
        default = 3,
        ge = 1,
        le = 5,
        description = "How intense the dream felt (1-5)."
    )



# Response
    
class InsightTag(StrictModel):
    label: str = Field(..., min_length = 2, max_length = 40)
    confidence: Literal["low", "medium", "high"] = "medium"


class DreamAnalyzeResponse(StrictModel):
    summary: str = Field(..., min_length = 10, max_length = 600)

    emotions: List[InsightTag] = Field(
        default_factory=list,
        description = "Detected emotions as short tags."
    )

    themes: List[InsightTag] = Field(
        default_factory=list,
        description="Themes/patterns commonly linked to such dreams."
    )

    interpretation:str = Field(
        ...,
        min_length = 40,
        max_length = 1200,
        description = "Soft, non-diagnostic interpretation (might/could/often)."
    )

    reflection_questions: List[str] = Field(
        default_factory=list,
        min_length=1,
        max_length=3,
        description = "1-3 reflective questions for the user."
    )


    feedback: List[str] = Field(
        default_factory = list,
        min_length=1,
        max_length=5,
        description = "Practical, gentle suggestion (journaling, stress check, sleep hygiene)."
    )

    safety_note:str = Field(
        default = "This is reflective content, not medial or mental-health advice.",
        max_length = 200
    )



