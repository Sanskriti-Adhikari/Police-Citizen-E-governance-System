from pydantic import BaseModel, Field
from typing import List, Optional

class AllocationRequest(BaseModel):
    total_officers: int = Field(..., ge=1)
    areas: Optional[List[str]] = None

class AllocationResult(BaseModel):
    area: str
    officers: int
    crime_rate: int

class AllocationResponse(BaseModel):
    allocation: List[AllocationResult]
    total_allocated: int
    recommendation: str
