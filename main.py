from fastapi import FastAPI

app = FastAPI(title="BlackRock AutoSave")

@app.get("/")
def home():
    return {"message": "BlackRock AutoSave API Running 🚀"}
