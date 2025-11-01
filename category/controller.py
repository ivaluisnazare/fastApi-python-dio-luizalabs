from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import get_db, CategoryCreate, CategoryResponse
from service import CategoriaService

app = FastAPI(title="Category Service", version="1.0.0")

@app.post("/categories/", response_model=CategoryResponse)
def create_categoria(categoria: CategoryCreate, db: Session = Depends(get_db)):
    return CategoriaService.create_category(db, categoria)

@app.get("/categories/", response_model=list[CategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return CategoriaService.get_categories(db, skip, limit)

@app.get("/categories/{category_id}", response_model=CategoryResponse)
def read_categoria(category_id: int, db: Session = Depends(get_db)):
    return CategoriaService.get_category_by_id(db, category_id)

@app.put("/categories/{category_id}", response_model=CategoryResponse)
def update_categoria(categoria_id: int, categoria: CategoryCreate, db: Session = Depends(get_db)):
    return CategoriaService.update_category(db, categoria_id, categoria)

@app.delete("/categories/{category_id}")
def delete_categoria(category_id: int, db: Session = Depends(get_db)):
    return CategoriaService.delete_category(db, category_id)

@app.get("/health")
def health_check():
    return {"status": "healthy"}