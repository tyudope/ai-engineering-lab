# DreamSense

DreamSense is a small GenAI project that provides **structured, non-diagnostic psychological reflections** on user-described dreams.

The goal is not dream prediction or therapy, but to practice **AI engineering fundamentals**: building reliable systems around probabilistic models, enforcing output contracts, and designing safe interactions with LLMs.

This project lives inside the `ai-engineering-lab` repository under:

```
ai-engineering-lab/projects/dreamsense/
```

---

## What it does

- Takes a dream description from the user
- Generates a short summary
- Extracts emotions and themes
- Provides a soft psychological interpretation
- Asks reflective questions
- Gives gentle, practical feedback

Important: DreamSense does **not** provide medical or mental-health advice.

---

## Why this project exists

This project is intentionally simple in scope, but serious in design.

It focuses on:
- Schema-first GenAI design
- Guardrails and safety
- Deterministic API contracts around LLM output
- Defensive handling of model failures
- Minimal UI to expose model behavior clearly

The idea is to learn how to **build systems around LLMs**, not just call an API.

---

## Tech stack

- Python
- FastAPI
- Pydantic
- OpenAI (Responses API)
- Jinja2 (server-rendered UI)
- Minimal vanilla JS (loading state only)

---

## Project structure

From `ai-engineering-lab/projects/dreamsense/`:

```
dreamsense/
├─ app/
│  ├─ main.py
│  ├─ api/
│  │  └─ routes/
│  │     ├─ dreams.py
│  │     ├─ ui.py
│  │     └─ health.py
│  ├─ core/
│  │  ├─ config.py
│  │  ├─ openai_client.py
│  │  ├─ prompts.py
│  │  └─ prompt_templates.py
│  ├─ schemas/
│  │  └─ dreams.py
│  ├─ templates/
│  │  ├─ index.html
│  │  ├─ result.html
│  │  └─ error.html
│  └─ static/
│     └─ style.css
├─ .env.example
└─ README.md
```

---

## Configuration

DreamSense uses environment variables.

Create a `.env` file in:

```
ai-engineering-lab/projects/dreamsense/.env
```

Example:

```env
OPENAI_API_KEY=sk-xxxxxxxx
OPENAI_MODEL=gpt-4.1-mini
```

Notes:
- Do not commit `.env`
- Keep `.env.example` committed as a reference

---

## Running locally

From `ai-engineering-lab/projects/dreamsense/`:

```bash
uvicorn app.main:app --reload
```

Open:
- UI: http://127.0.0.1:8000/
- OpenAI health check: http://127.0.0.1:8000/health/openai

---

## Health check

To verify your OpenAI key and model access:

```bash
curl http://127.0.0.1:8000/health/openai
```

Expected response:

```json
{
  "status": "ok",
  "openai_reply": "ok"
}
```

---

## API endpoint

### POST `/dreams/analyze`

Example request:

```json
{
  "dream_text": "I was running late for a flight and every gate was closed.",
  "user_context": "Upcoming exams",
  "intensity": 4
}
```

Example response (simplified):

```json
{
  "summary": "...",
  "emotions": [{"label": "anxiety", "confidence": "high"}],
  "themes": [{"label": "fear of failure", "confidence": "medium"}],
  "interpretation": "...",
  "reflection_questions": ["..."],
  "feedback": ["..."],
  "safety_note": "This is reflective content, not medical advice."
}
```

---

## Safety notes

- No diagnosis or therapy claims
- Soft, non-authoritative language enforced
- Output must match a strict Pydantic schema
- Invalid or unsafe model output is rejected

Safety is enforced in **code**, not just in prompts.

---

## What this project demonstrates

- Designing GenAI systems with strict output contracts
- Defensive handling of unreliable model output
- Integrating LLMs into a real backend
- Exposing AI behavior through a simple UI

---

## Possible next steps

- Save dream history (SQLite)
- Detect recurring themes
- Export reflections (Markdown/PDF)
- Add basic tests and logging

---

## Disclaimer

DreamSense is for educational and reflective purposes only.  
It does not replace professional mental-health care.

Built as part of **ai-engineering-lab**.
