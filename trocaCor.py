import re

# Caminho do arquivo SVG
caminho_arquivo = r'C:\Users\2902374072\Desktop\Mapa Astral\GustavoCompositeChart.svg'

# Ler o conteúdo do arquivo SVG
with open(caminho_arquivo, 'r') as arquivo:
    svg_code = arquivo.read()

# Defina a cor de substituição
nova_cor = '#6A1B9A'

# Use expressões regulares para encontrar a cor atual e substituí-la
padrao = r'style\s*=\s*\'fill:\s*([^;]+);\s*\''
novo_codigo = re.sub(padrao, f"style='fill: {nova_cor};'", svg_code)

# Salvar o novo SVG em um arquivo
nome_arquivo = caminho_arquivo  # Especifique o nome do arquivo desejado

with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(novo_codigo)

print(f'O novo SVG foi salvo no arquivo {nome_arquivo}.')