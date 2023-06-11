import requests

class BuscaEndereco:

    def __init__(self, cep):

        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Quantidade de dígitos incorreta paara um cep')

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def __str__(self):
        return self.format_cep()

    def get_informacoes_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        requisicao = requests.get(url)
        dados = requisicao.json()
        return (dados['bairro'],
                dados['localidade'],
                dados['uf']
        )


