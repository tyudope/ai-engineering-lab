from app.schemas.dreams import DreamAnalyzeResponse

def dream_analysis_user_prompt(dream_text: str, user_context:str | None , intensity:int) -> str:

    schema_json = DreamAnalyzeResponse.model_json_schema()

    return f"""
            You will analyze a dream and return a reflective psychological interpretation.

            User dream:
            {dream_text}

            Optional context:
            {user_context or "None"}

            Intensity (1-5):
            {intensity}

            Return JSON that matches this JSON Schema exactly:
            {schema_json}

            Remember:
            - soft language
            - no diagnosis
            - no therapy claims
            """