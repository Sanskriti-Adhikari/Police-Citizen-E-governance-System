from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from criminal_records import router as records_router, criminal_records
from officers import router as officers_router, officers, auto_allocate_officer
from complaints import router as complaints_router, complaints
from emergency_alerts import router as emergency_router
from notifications import router as notifications_router
from analytics import router as analytics_router

app = FastAPI(title="E-Governance API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_methods=[""],
    allow_headers=["*"],
)

# Include all routers
app.include_router(records_router, prefix="/api")
app.include_router(officers_router, prefix="/api")
app.include_router(complaints_router, prefix="/api")
app.include_router(emergency_router, prefix="/api")
app.include_router(notifications_router, prefix="/api")
app.include_router(analytics_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "E-Governance API is running", "version": "1.0"}

if name=="main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)