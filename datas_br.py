from datetime import datetime, timedelta


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = ['janeiro', 'fevereiro', 'março',
                        'abril', 'maio', 'junho', 'julho',
                        'agosto', 'setembro', 'outubro', 'novembro',
                        'dezembro'
                        ]
        mes_numerico = self.momento_cadastro.month - 1
        return meses_do_ano[mes_numerico]

    def format_datetime(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada

    def calcula_diferenca_data(self):
        momento_cadastro1 = datetime.today()
        return momento_cadastro1 - self.momento_cadastro

    def __str__(self):
        return self.format_datetime()
