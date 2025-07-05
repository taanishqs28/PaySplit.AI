from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import router as v1_router

app = FastAPI(title='PaySplit-AI', version='0.1.0')

# CORS configuration so that the frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    # TODO: Replace '*' with your frontend URL in production
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the API router for version 1
app.include_router(v1_router, prefix="/api/v1")