from fastapi import HTTPException

class CategoryNotFoundException(HTTPException):
    def __init__(self, detail: str = "Category not found"):
        super().__init__(status_code=404, detail=detail)

class CategoryAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "Category already exists"):
        super().__init__(status_code=400, detail=detail)