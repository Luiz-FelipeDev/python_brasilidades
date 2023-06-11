from Cpf_Cnpj import Documento, DocCPF, DocCNPJ
from TelefoneBr import TelefoneBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
from datetime import datetime, timedelta
#objeto_cpf = CpfCnpj('01234567890', 'cpf')
#print(objeto_cpf)

objeto_cnpj = Documento.cria_documento('67685335000161')
#print(objeto_cnpj)

objeto_cpf = Documento.cria_documento('01234567890')
#print(objeto_cpf)


objeto_telefone = TelefoneBr('558898416496')
print(objeto_telefone)

momento_cadastro = DatasBr()
print(momento_cadastro.mes_cadastro())
print(momento_cadastro)

#acessando api de CEP
r = BuscaEndereco('91910450')
print(r.get_informacoes_cep())
# Trabalhando com a formatação do datetime
'''
data_hj = datetime.today()
data_jh_format = data_hj.strftime('%d/%m/%Y %H:%M')
print(data_jh_format)
'''