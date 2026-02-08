# AI_DJ

AI_DJ is a FastAPI app that generates a DJ-ready playlist based on a party theme, emotional flow, and duration. It uses the OpenAI Responses API to return structured JSON that matches a strict schema.

**Features**
- Playlist generation with a short analysis
- Strict request/response validation via Pydantic
- Clean UI with live counters and client-side validation

**Project Structure**
- `app/main.py` — FastAPI app and routes
- `app/api/playlist.py` — API endpoint
- `app/core/` — OpenAI client + prompt templates
- `app/schemas/` — Pydantic schemas
- `app/static/index.html` — UI

**Setup**
1. Create a `.env` file in `projects/ai_dj` with:
   ```
   OPENAI_API_KEY=your_key_here
   ```
2. Install dependencies from the project root if needed:
   ```
   pip install -r requirements.txt
   ```
3. Run the server (from `projects/ai_dj`):
   ```
   uvicorn app.main:app --reload
   ```

**UI**
- Open `http://127.0.0.1:8000/ui`

**API**
- `POST /dj/create_playlist`

Request body:
```json
{
  "theme_of_party": "Neon rooftop afterparty in Tokyo, 2am–5am, cinematic but upbeat",
  "emotional_flow_of_the_songs": [
    "mysterious",
    "slow-burn groove",
    "euphoric lift",
    "hands-in-the-air peak",
    "warm glide-down"
  ],
  "duration": 180
}
```

Response body:
```json
{
  "analyze": "Short reasoning about the playlist choices...",
  "songs": [
    "Artist: Track : 3.45",
    "Artist: Track : 4.10"
  ]
}
```

**Validation Limits**
- `theme_of_party`: 20–4000 characters
- `emotional_flow_of_the_songs`: 2–5 items
- `duration`: 10–600 minutes
- Response `analyze`: 20–1200 characters

**Troubleshooting**
- 401/403 errors: check `OPENAI_API_KEY` in `.env`
- 500 errors: check server logs for the exception detail
- Validation errors: confirm request matches limits above
