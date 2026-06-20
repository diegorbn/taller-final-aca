from fastapi import FastAPI

from app.routers.snacks import router as snacks_router

app = FastAPI(
    title="Intergalactic Snack Bar API",
    description=(
        "A dummy API for managing snacks sold to aliens, astronauts, "
        "and other hungry space travelers."
    ),
    version="1.0.0",
)

app.include_router(snacks_router)


@app.get("/", tags=["General"])
def root():
    """
    Return a welcome message.

    This endpoint can also be used to verify that the API is running.
    """
    return {
        "message": "Welcome to the Intergalactic Snack Bar!",
        "warning": "Do not feed the black hole."
    }


@app.get("/health", tags=["General"])
def health_check():
    """
    Check whether the API is working.
    """
    return {
        "status": "healthy",
        "snack_reactor": "online"
    }