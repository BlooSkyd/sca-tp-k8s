from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/stress")
def stress(duration: int = 60):
    timeout = time.time() + duration
    while time.time() < timeout:
        _ = 123456 * 123456
    return {"status": "finished", "duration": duration}