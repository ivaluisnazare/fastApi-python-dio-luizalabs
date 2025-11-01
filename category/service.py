from sqlalchemy.orm import Session
from models import CategoryModel, CategoryCreate
from exceptions import CategoryNotFoundException, CategoryAlreadyExistsException


class CategoriaService:
    @staticmethod
    def create_category(db: Session, category: CategoryCreate):
        existing_categoria = db.query(CategoryModel).filter(CategoryModel.c_nome == category.c_nome).first()
        if existing_categoria:
            raise CategoryAlreadyExistsException()

        db_categoria = CategoryModel(c_nome=category.c_nome)
        db.add(db_categoria)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria

    @staticmethod
    def get_categories(db: Session, skip: int = 0, limit: int = 100):
        return db.query(CategoryModel).offset(skip).limit(limit).all()

    @staticmethod
    def get_category_by_id(db: Session, category_id: int):
        category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        if not category:
            raise CategoryNotFoundException()
        return category

    @staticmethod
    def update_category(db: Session, category_id: int, category: CategoryCreate):
        db_category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        if not db_category:
            raise CategoryNotFoundException()

        existing_categoria = db.query(CategoryModel).filter(
            CategoryModel.c_nome == category.c_nome,
            CategoryModel.id != category_id
        ).first()
        if existing_categoria:
            raise CategoryAlreadyExistsException()

        db_category.c_nome = category.c_nome
        db.commit()
        db.refresh(db_category)
        return db_category

    @staticmethod
    def delete_category(db: Session, category_id: int):
        category = db.query(CategoryModel).filter(CategoryModel.id == category_id).first()
        if not category:
            raise CategoryNotFoundException()

        db.delete(category)
        db.commit()
        return {"message": "Category successfully deleted."}