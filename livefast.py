from fastapi import FastAPI

#just use the FastAPI to make a object so that we can use the functionality of the Fast api framework
app = FastAPI()

@app.get("/hello")
async def hello():
    return {"hello": "world"}