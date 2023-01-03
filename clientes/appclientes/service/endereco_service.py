from ..models import Endereco


def cadastrar_endereco(endereco):
    Endereco.objects.create(rua=endereco.rua, numero=endereco.numero,
                            complemento=endereco.complemento, cidade=endereco.cidade, pais=endereco.pais)

