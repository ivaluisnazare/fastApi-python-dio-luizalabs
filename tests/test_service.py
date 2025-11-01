# import pytest
# from unittest.mock import Mock, create_autospec
# from sqlalchemy.orm import Session
# from category.models import CategoryModel, CategoryCreate
# from category.exceptions import CategoryNotFoundException, CategoryAlreadyExistsException
# from category.service import CategoriaService
#
#
# class TestCategoriaService:
#
#     def setup_method(self):
#         """Setup para cada teste"""
#         self.mock_db = create_autospec(Session)
#         self.sample_category_data = CategoryCreate(c_nome="Electronics")
#         self.sample_category_model = CategoryModel(id=1, c_nome="Electronics")
#
#     def test_create_category_success(self):
#         """Testa criação bem-sucedida de categoria"""
#         # Arrange
#         self.mock_db.query.return_value.filter.return_value.first.return_value = None
#         self.mock_db.add = Mock()
#         self.mock_db.commit = Mock()
#         self.mock_db.refresh = Mock()
#
#         # Act
#         result = CategoriaService.create_category(self.mock_db, self.sample_category_data)
#
#         # Assert
#         assert result.c_nome == self.sample_category_data.c_nome
#         # self.mock_db.add.assert_called_once()
#         # self.mock_db.commit.assert_called_once()
#         # self.mock_db.refresh.assert_called_once()
#
#     def test_create_category_already_exists(self):
#         """Testa criação de categoria que já existe"""
#         # Arrange
#         self.mock_db.query.return_value.filter.return_value.first.return_value = self.sample_category_model
#
#         # Act & Assert
#         with pytest.raises(CategoryAlreadyExistsException):
#             CategoriaService.create_category(self.mock_db, self.sample_category_data)
#
#     def test_get_categories_success(self):
#         """Testa obtenção de lista de categorias"""
#         # Arrange
#         expected_categories = [
#             CategoryModel(id=1, c_nome="Electronics"),
#             CategoryModel(id=2, c_nome="Books")
#         ]
#         self.mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = expected_categories
#
#         # Act
#         result = CategoriaService.get_categories(self.mock_db, skip=0, limit=100)
#
#         # Assert
#         assert result == expected_categories
#         self.mock_db.query.return_value.offset.assert_called_once_with(0)
#         self.mock_db.query.return_value.limit.assert_called_once_with(100)
#
#     def test_get_categories_with_pagination(self):
#         """Testa obtenção de categorias com paginação"""
#         # Arrange
#         expected_categories = [CategoryModel(id=3, c_nome="Clothing")]
#         self.mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = expected_categories
#
#         # Act
#         result = CategoriaService.get_categories(self.mock_db, skip=10, limit=5)
#
#         # Assert
#         assert result == expected_categories
#         self.mock_db.query.return_value.offset.assert_called_once_with(10)
#         self.mock_db.query.return_value.limit.assert_called_once_with(5)
#
#     def test_get_category_by_id_success(self):
#         """Testa obtenção de categoria por ID existente"""
#         # Arrange
#         self.mock_db.query.return_value.filter.return_value.first.return_value = self.sample_category_model
#
#         # Act
#         result = CategoriaService.get_category_by_id(self.mock_db, 1)
#
#         # Assert
#         assert result == self.sample_category_model
#         self.mock_db.query.return_value.filter.return_value.first.assert_called_once()
#
#     def test_get_category_by_id_not_found(self):
#         """Testa obtenção de categoria por ID inexistente"""
#         # Arrange
#         self.mock_db.query.return_value.filter.return_value.first.return_value = None
#
#         # Act & Assert
#         with pytest.raises(CategoryNotFoundException):
#             CategoriaService.get_category_by_id(self.mock_db, 999)
#
#     def test_update_category_success(self):
#         """Testa atualização bem-sucedida de categoria"""
#         # Arrange
#         updated_data = CategoryCreate(c_nome="Updated Electronics")
#         existing_category = CategoryModel(id=1, c_nome="Electronics")
#
#         self.mock_db.query.return_value.filter.return_value.first.side_effect = [
#             existing_category,  # Para verificar se a categoria existe
#             None  # Para verificar se não há conflito de nome
#         ]
#         self.mock_db.commit = Mock()
#         self.mock_db.refresh = Mock()
#
#         # Act
#         result = CategoriaService.update_category(self.mock_db, 1, updated_data)
#
#         # Assert
#         assert result.c_nome == updated_data.c_nome
#         self.mock_db.commit.assert_called_once()
#         self.mock_db.refresh.assert_called_once_with(existing_category)
#
#     def test_update_category_not_found(self):
#         """Testa atualização de categoria inexistente"""
#         # Arrange
#         updated_data = CategoryCreate(c_nome="Updated Electronics")
#         self.mock_db.query.return_value.filter.return_value.first.return_value = None
#
#         # Act & Assert
#         with pytest.raises(CategoryNotFoundException):
#             CategoriaService.update_category(self.mock_db, 999, updated_data)
#
#     def test_update_category_name_conflict(self):
#         """Testa atualização com nome que já existe em outra categoria"""
#         # Arrange
#         updated_data = CategoryCreate(c_nome="Existing Category")
#         existing_category = CategoryModel(id=1, c_nome="Electronics")
#         conflicting_category = CategoryModel(id=2, c_nome="Existing Category")
#
#         self.mock_db.query.return_value.filter.return_value.first.side_effect = [
#             existing_category,  # Para verificar se a categoria existe
#             conflicting_category  # Para verificar conflito de nome
#         ]
#
#         # Act & Assert
#         with pytest.raises(CategoryAlreadyExistsException):
#             CategoriaService.update_category(self.mock_db, 1, updated_data)
#
#     def test_delete_category_success(self):
#         """Testa exclusão bem-sucedida de categoria"""
#         # Arrange
#         category_to_delete = CategoryModel(id=1, c_nome="Electronics")
#         self.mock_db.query.return_value.filter.return_value.first.return_value = category_to_delete
#         self.mock_db.delete = Mock()
#         self.mock_db.commit = Mock()
#
#         # Act
#         result = CategoriaService.delete_category(self.mock_db, 1)
#
#         # Assert
#         assert result == {"message": "Category successfully deleted."}
#         self.mock_db.delete.assert_called_once_with(category_to_delete)
#         self.mock_db.commit.assert_called_once()
#
#     def test_delete_category_not_found(self):
#         """Testa exclusão de categoria inexistente"""
#         # Arrange
#         self.mock_db.query.return_value.filter.return_value.first.return_value = None
#
#         # Act & Assert
#         with pytest.raises(CategoryNotFoundException):
#             CategoriaService.delete_category(self.mock_db, 999)