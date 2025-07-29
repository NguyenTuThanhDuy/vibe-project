from fastapi import FastAPI

app = FastAPI(title="Vibe Kanban", description="A modern kanban board API", version="0.1.0")

@app.get("/")
async def root():
    return {"message": "Hello from Vibe Kanban!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
