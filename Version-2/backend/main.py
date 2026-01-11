from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import criminal_router, officer_router, analytics_router, allocation_router, holiday_router
from database.sample_data import initialize_sample_data

app = FastAPI(
    title="E-Governance Police/Admin System API",
    description="Backend API for Police Administration and Criminal Records Management",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    initialize_sample_data()

# Include routers
app.include_router(criminal_router.router)
app.include_router(officer_router.router)
app.include_router(analytics_router.router)
app.include_router(allocation_router.router)
app.include_router(holiday_router.router)

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "E-Governance Police/Admin System API",
        "version": "1.0.0",
        "endpoints": {
            "records": "/api/records",
            "officers": "/api/officers",
            "analytics": "/api/analytics",
            "holidays": "/api/holidays",
            "allocation": "/api/allocation/allocate",
            "docs": "/docs"
        }
    }
