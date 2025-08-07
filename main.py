from fastapi import FastAPI
from app.api import device_510k, classification, enforcement

# Create FastAPI app instance
app = FastAPI(title="Local openFDA API")

# Include routers
app.include_router(device_510k.router, prefix="/device/510k", tags=["510k"])
app.include_router(classification.router, prefix="/device/classification", tags=["classification"])
app.include_router(enforcement.router, prefix="/device/enforcement", tags=["enforcement"])

@app.get("/")
async def root():
    """Root endpoint that provides information about the API."""
    return {
        "message": "Welcome to the Local openFDA API",
        "endpoints": {
            "510k": "/device/510k",
            "classification": "/device/classification",
            "enforcement": "/device/enforcement"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
