from fastapi import FastAPI

from card.card_api import card_router
from transfers.transfers_api import trans_router
from users.user_api import user_router

from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(card_router)
app.include_router(user_router)
app.include_router(trans_router)