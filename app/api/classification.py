import json
from typing import Optional, Dict, Any
from fastapi import APIRouter, HTTPException, Query
from app.api.data_loader import load_classification_data, filter_data

router = APIRouter()

@router.get("/")
async def get_classification_records(
    search: Optional[str] = Query(None, description="field:value filter string"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, description="Number of records to return"),
):
    """Search and paginate through classification records."""
    try:
        records = load_classification_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    filtered = list(filter_data(records, search))
    total_count = len(filtered)
    paginated = filtered[skip : skip + limit]
    return {
        "meta": {
            "total_count": total_count,
            "skip": skip,
            "limit": limit,
            "returned_count": len(paginated),
        },
        "results": paginated,
    }
