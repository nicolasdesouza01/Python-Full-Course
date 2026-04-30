import urllib.request

# Definindo as cores (padrão ANSI)
verde = '\033[32m'
vermelho = '\033[31m'
amarelo = '\033[33m'
limpa = '\033[m'

try:
    # O "disfarce" para o servidor aceitar a conexão
    header = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request('http://www.pudim.com.br', headers=header)
    
    print(f"{amarelo}Verificando disponibilidade do site...{limpa}")
    site = urllib.request.urlopen(req)

except Exception as erro:
    # Se der erro, exibe em vermelho
    print(f"{vermelho}O site Pudim não está acessível no momento.{limpa}")
    print(f"Detalhe do erro: {erro}")

else:
    # Se der certo, exibe em verde
    print(f"{verde}Consegui acessar o site Pudim com sucesso!{limpa}")
    # Opcional: ler o conteúdo (HTML) do site
    # print(site.read())

#desafio 114 estava indisponivel então usei um modelo pronto apenas de exemplo.