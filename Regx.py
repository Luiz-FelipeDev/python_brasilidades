import re

pattern = re.compile('[0-9]{2,3}[0-9]{4}[0-9]{4}')
text = 'meus numeros de telefone são 5599998888 e 4455556666'
respostas = re.findall(pattern, text)
for resposta in respostas:
    print(resposta)




