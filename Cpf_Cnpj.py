from validate_docbr import CPF, CNPJ

class Documento:
    ''' class utilizada para Refatoração do código de acordo com o tipo de documento.
    Foi feita através da lógica do número de caracteres de cada tipo de documento
                                                                                    '''
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError(
                'Quantidade de digitos inválida para os tipos de documentos trabalhados'
            )

class DocCPF:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('Cpf inválido!!')


    def valida(self, documento):
        ''' Valida o CPF de acordo com os algoritmos da biblioteca e através do method validate'''
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    def format(self):
        ''' formata o CPF com o method mask da class CPF da biblioteca importada'''
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)

    def __str__(self):
        ''' Retorna a instância para o user já com a formatação'''
        return self.format()


class DocCNPJ:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ inválido!!')

    def valida(self, documento):
        ''' Valida o CNPJ de acordo com os algoritmos da biblioteca e através do method validate'''
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    def format(self):
        ''' formata o CNPJ com o method mask da class CNPJ da biblioteca importada'''
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)

    def __str__(self):
        ''' Retorna a instância para o user já com a formatação '''
        return self.format()
