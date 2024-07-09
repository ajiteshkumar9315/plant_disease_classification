from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI()

@app.get("/ping")     #this is how wwe specify the end point.

async def ping():
    return "hello, i am alive"

@app.post('/predict')
async def predict(
        file: UploadFile = File(...)
):
    pass

if __name__  == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
