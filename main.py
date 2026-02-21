from fastapi import FastAPI
from api.transaction import router as transaction_router
from api.returns import router as returns_router
from api.validator import router as validator_router
from api.temporal_rules import router as temporal_router


app = FastAPI(title="BlackRock AutoSave Retirement Engine")

app.include_router(validator_router)
app.include_router(transaction_router)
app.include_router(returns_router)
app.include_router(temporal_router)



@app.get("/")
def home():
    return {"message": "BlackRock AutoSave Running "}
