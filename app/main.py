from fastapi import FastAPI
from .database import engine, Base
from .routes import accounts, auth

# Initialize the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI app instance
app = FastAPI()

# Include the routes
app.include_router(auth.router)
app.include_router(accounts.router)

# Root endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Banking Dashboard API"}
