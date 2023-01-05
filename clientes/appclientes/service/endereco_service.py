from ..models import Endereco


def cadastrar_endereco(endereco):
    return Endereco.objects.create(rua=endereco.rua, numero=endereco.numero,bairro=endereco.bairro,
                                   complemento=endereco.complemento, cidade=endereco.cidade, pais=endereco.pais)
