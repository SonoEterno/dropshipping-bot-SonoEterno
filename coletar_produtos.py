import json
import time

# Simulação de coleta de produtos (substitua com scraping real depois)
produtos = [
    {"nome": "Produto 1", "preco": 19.99, "link": "https://exemplo.com/p1"},
    {"nome": "Produto 2", "preco": 29.99, "link": "https://exemplo.com/p2"},
    {"nome": "Produto 3", "preco": 39.99, "link": "https://exemplo.com/p3"},
]

# Salvar em arquivo JSON
with open("dados_dos_produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos, f, ensure_ascii=False, indent=4)

print("✅ Produtos coletados e salvos com sucesso!")
time.sleep(1)
