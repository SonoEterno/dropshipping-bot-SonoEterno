import json
import os
from datetime import datetime
import requests # Adicionado para corrigir o erro

# Esta é a função que você vai chamar para cada produto
def salvar_dados_produto(id_produto, nome_produto, preco_venda, custo_produto, taxa_plataforma):
    
    # Calcular o lucro
    lucro_bruto = preco_venda - custo_produto - taxa_plataforma

    # Adicionar um registro de data e hora
    momento_do_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Criar um dicionário com os dados
    dados_do_produto = {
        "id_do_produto": id_produto,
        "data_registro": momento_do_registro,
        "nome": nome_produto,
        "precos": {
            "preco_venda_shopee": preco_venda,
            "custo_fornecedor": custo_produto,
            "taxa_plataforma": taxa_plataforma,
            "lucro_bruto": lucro_bruto
        }
    }

    nome_do_arquivo = "dados_dos_produtos.json"
    
    # Verificar se o arquivo já existe
    if not os.path.exists(nome_do_arquivo):
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump([], arquivo_json) # Cria o arquivo como uma lista vazia

    # Ler os dados existentes, adicionar os novos e salvar novamente
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo_json:
        lista_produtos = json.load(arquivo_json)

    lista_produtos.append(dados_do_produto)

    with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(lista_produtos, arquivo_json, indent=4, ensure_ascii=False)

    print(f"Dados do produto '{nome_produto}' salvos no arquivo {nome_do_arquivo}")

# Exemplo de como você chamaria a função no seu script
# Esta linha abaixo é a que precisa ser ativada, removendo o #
salvar_dados_produto("ID_EXEMPLO", "Nome do Produto Exemplo", 10.00, 5.00, 1.50)

print('Automação concluída!')
