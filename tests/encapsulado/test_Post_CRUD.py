import pytest
from main.services.CRUDServices import CRUDServices

def test_post_CRUD_endpoint():
    response = CRUDServices.postCRUD("testdas dias34789", "teste091ll@gmail.com", "28", "99999999", "rua teste alves68km76", "QA", "teste123")
    assert (response.status_code == 201)

@pytest.mark.parametrize("nome, email, idade, telefone, endereco, profissao, empresa",
    [("Inacio", "teste@exemplo.com", "21","9889192193", "rua teste almeida","Back", "BQA"), 
     ("", "teste@exemplo.com", "9889192193", "34", "rua teste almeida","Back", "BQA"),
     ("Inacio", "", "9889192193", "", "rua teste almeida","Back", "BQA")])
def test_post_CRUD_endpoint(nome, email, idade, telefone, endereco, profissao, empresa):
    response = CRUDServices.postCRUD(nome, email, idade, telefone, endereco, profissao, empresa).status_code == 200    