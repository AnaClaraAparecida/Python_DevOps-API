import requests

url = 'https://viacep.com.br/ws/{}/json/'

ceps = [
    '04101300',
    '80530230',
    '23575460',
    '40160650',
    '35460000'
]

cabec = "cep; logradouro; complemento; bairro; localidade; uf; ibge; gia; ddd; siafi;"
registros = []

registros.append(cabec)

for cep in ceps:
    resposta = requests.get(url.format(cep))
    if resposta.status_code == 200:
        payload = resposta.json()
        registros.append(
    f"{payload.get('cep','')};" +
    f"{payload.get('logradouro','')};" +
    f"{payload.get('complemento','')};" +
    f"{payload.get('bairro','')};" +
    f"{payload.get('localidade','')};" +
    f"{payload.get('uf','')};" +
    f"{payload.get('ibge','')};" +
    f"{payload.get('gia','')};" +
    f"{payload.get('ddd','')};" +
    f"{payload.get('siafi','')};\n"
)

with open('arquivo_saida.csv', 'w') as arquivo:
    arquivo.writelines(registros)