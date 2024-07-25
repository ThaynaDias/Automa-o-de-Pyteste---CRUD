from main.services.CRUDServices import CRUDServices

def test_get_CRUD_endpoint():
    response = CRUDServices.getCRUD()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    

def test_get__all_CRUD_endpoint():
    response = CRUDServices.getAllCRUD("4")
    json_response = response.json()
    assert response.status_code == 200
    assert json_response["nome"] == "Jam Batista"

