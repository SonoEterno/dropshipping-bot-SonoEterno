
import json
import os
from datetime import datetime

ARQUIVO = "dados_dos_produtos.json"

def carregar_produtos():
    """Carrega produtos do arquivo JSON ou retorna lista vazia."""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_produtos(produtos):
    """Salva lista de produtos no arquivo JSON."""
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, indent=4, ensure_ascii=False)

def salvar_dados_produto(id_produto, nome_produto, preco_venda, custo_produto, taxa_plataforma):
    """Salva dados de um produto no arquivo JSON."""
    try:
        preco_venda = float(preco_venda)
        custo_produto = float(custo_produto)
        taxa_plataforma = float(taxa_plataforma)
    except ValueError:
        print("Erro: Preços e taxas devem ser números.")
        return
    
    lucro_bruto = preco_venda - custo_produto - taxa_plataforma
    momento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    produto = {
        "id_do_produto": id_produto,
        "data_registro": momento,
        "nome": nome_produto,
        "precos": {
            "preco_venda_shopee": preco_venda,
            "custo_fornecedor": custo_produto,
            "taxa_plataforma": taxa_plataforma,
            "lucro_bruto": lucro_bruto
        }
    }

    produtos = carregar_produtos()
    produtos.append(produto)
    salvar_produtos(produtos)

    print(f"✅ Produto '{nome_produto}' salvo com sucesso!")

# Exemplo de uso
if __name__ == "__main__":
    salvar_dados_produto("ID_EXEMPLO", "Produto Exemplo", 10.00, 5.00, 1.50)
    print("Automação concluída!")
