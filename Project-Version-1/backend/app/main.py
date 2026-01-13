# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routers import auth, crimes, criminals, complaints, emergency, officers, notices, heatmap, upload

app = FastAPI(title="E-Governance Police System API", version="1.0.0")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(crimes.router, prefix="/api/crimes", tags=["Crimes"])
app.include_router(criminals.router, prefix="/api/criminals", tags=["Criminals"])
app.include_router(complaints.router, prefix="/api/complaints", tags=["Complaints"])
app.include_router(emergency.router, prefix="/api/emergency", tags=["Emergency Alerts"])
app.include_router(officers.router, prefix="/api/officers", tags=["Officers"])
app.include_router(notices.router, prefix="/api/notices", tags=["Notices"])
app.include_router(heatmap.router, prefix="/api/heatmap", tags=["Heatmap"])
app.include_router(upload.router, prefix="/api/upload", tags=["File Upload"])

# Root
@app.get("/")
async def root():
    return {"message": "E-Governance Police System API", "version": "1.0.0"}

# Health Check
@app.get("/health")
async def health_check():
    from datetime import datetime
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
