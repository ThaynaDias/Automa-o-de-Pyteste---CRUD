from main.services.CRUDServices import CRUDServices

def test_Put_CRUD_endpoint():
    response = CRUDServices.putCRUD("5", "Jam Batista3", "jam.batista@example.com", "43", "+5511987632145", "Alameda Santos, 1010, Belo Horizonte1 , RJ", "QA Senior", "ConstruTech")
    assert (response.status_code == 200)