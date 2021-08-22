from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root(number: int):
    return {"number": number + 1}
