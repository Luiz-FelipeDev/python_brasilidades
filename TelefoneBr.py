import re

class TelefoneBr:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('O número passado está inválido')

    def valida_telefone(self, telefone):
        pattern = re.compile('([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})')
        respostas = re.findall(pattern, telefone)

        if respostas:
            return True
        else:
            return False

    def format_telefone(self):
        padrao = re.compile('([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})')
        resposta = re.search(padrao, self.numero)
        numero_formatado = '+{}({}){}-{}'.format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado

    def __str__(self):
        return self.format_telefone()
