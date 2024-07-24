import requests

from main.commons.BaseClass import ENDPOINT


class CRUDServices():
    def getCRUD():
        header = {"accept": "*/*"}
        data = {}
        return requests.get(ENDPOINT + "/crud", headers=header, json=data)

    def getAllCRUD(id):
        return requests.get(ENDPOINT + "/crud/" + id)

    def postCRUD(nome, email, idade, telefone, endereco, profissao, empresa):
        header = {"accept": "*/*", "Content-Type": "application/json"}
        data = {"nome": nome, "email": email, "idade": idade, "telefone": telefone, "endereco": endereco, "profissao": profissao, "empresa": empresa}
        return requests.post(ENDPOINT + "/crud", json=data, headers=header)

    def putCRUD(id, nome, email, idade, telefone, endereco, profissao, empresa):
        header = {"accept": "application/json"}
        data = {"nome": nome,"email": email,"idade": idade,"telefone": telefone,"endereco": endereco,"profissao": profissao,"empresa": empresa}
        return requests.put(ENDPOINT + "/crud/" + id, json=data, headers=header)

    def deleteCRUD(id):
        return requests.post(ENDPOINT + "/crud/" + id)
