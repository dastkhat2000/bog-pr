from fastapi import HTTPException, status
NotFoundException = HTTPException(
    status_code=404, detail="User Not Found!" )



