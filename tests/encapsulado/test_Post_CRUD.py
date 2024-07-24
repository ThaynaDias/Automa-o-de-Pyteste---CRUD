from main.services.CRUDServices import CRUDServices

def test_post_CRUD_endpoint():
    response = CRUDServices.postCRUD("testdas dias34789", "teste091ll@gmail.com", "28", "99999999", "rua teste alves68km76", "QA", "teste123")
    assert (response.status_code == 201)
