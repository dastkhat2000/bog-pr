from fastapi import HTTPException

NotFoundException = HTTPException(status_code=404, detail="User Not Found!")

