from fastapi import APIRouter

# This is the variable the error is looking for!
router = APIRouter(prefix="/ml", tags=["Machine Learning"])

@router.get("/eoq-test")
def test_eoq():
    return {
        "status": "online",
        "message": "The EOQ Router is now communicating with main.py"
    }