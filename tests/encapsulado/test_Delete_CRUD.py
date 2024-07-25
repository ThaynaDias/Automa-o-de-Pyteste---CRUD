from main.services.CRUDServices import CRUDServices

def test_Delete_CRUD_endpoint():
    response = CRUDServices.getAllCRUD("2")
    assert response.status_code == 200