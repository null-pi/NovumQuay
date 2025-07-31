import logging

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from cass_websocket.routes import router as websocket_router

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    logger.info("Starting up the application...")
    yield
    # Code to run on shutdown
    logger.info("Shutting down the application...")


app = FastAPI(lifespan=lifespan)

app.include_router(websocket_router, prefix="/ws", tags=["websocket"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)