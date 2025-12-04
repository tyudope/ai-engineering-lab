from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "hello wolrd?"



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("greet_async:app")

