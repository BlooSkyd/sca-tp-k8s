import time
from fastapi import FastAPI, Response, status

class FakeDB:
    def __init__(self):
        time.sleep(15)
        self.counter = 0

    def query(self):
        self.counter += 1
        if self.counter >= 30:
            while True:
                time.sleep(1)
        if self.counter % 10 == 0:
            time.sleep(60)
        return True

app = FastAPI()
db_instance = None

@app.get("/startup")
def startup():
    global db_instance
    if db_instance is None:
        db_instance = FakeDB()
    return {"status": "started"}

@app.get("/readiness")
def readiness():
    if db_instance is None:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    db_instance.query()
    return {"status": "ready"}

@app.get("/liveness")
def liveness():
    if db_instance is None:
        return Response(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    db_instance.query()
    return {"status": "alive"}