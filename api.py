from fastapi import FastAPI

#test
app = FastAPI()


@app.get("/")
def root():
    return "Hello from Cloud Run CD"
