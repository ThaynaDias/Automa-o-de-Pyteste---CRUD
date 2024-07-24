from main.services.CRUDServices import CRUDServices

def test_Delete_CRUD_endpoint():
    response = CRUDServices.getAllCRUD("10")
    assert response.status_code == 200