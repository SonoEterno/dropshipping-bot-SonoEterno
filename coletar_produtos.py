import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import os

def coletar_produto_aliexpress(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Nome do produto
        nome = soup.find('h1', class_='product-title-text').get_text(strip=True) if soup.find('h1', class_='product-title-text') else 'N/A'
        
        # Preço
        preco_element = soup.find('div', class_='price--current--J_tA2Jt')
        if preco_element:
            preco_span = preco_element.find('span', class_='price--symbol--H2L3_kK')
            preco_value = preco_element.find('span', class_='price--amount--E7kL74t')
            if preco_span and preco_value:
                preco = preco_span.get_text(strip=True) + preco_value.get_text(strip=True)
            else:
                preco = 'N/A'
        else:
            preco = 'N/A'

        # Descrição (simplificado para o primeiro parágrafo)
        descricao = 'N/A'
        descricao_element = soup.find('div', class_='product-detail--content--2u4Ew_B')
        if descricao_element:
            paragraphs = descricao_element.find_all('p')
            if paragraphs:
                descricao = ' '.join([p.get_text(strip=True) for p in paragraphs])

        # Imagens
        imagens = []
        img_elements = soup.find_all('img', class_='image--image--3TfP7m_')
        for img in img_elements:
            if 'src' in img.attrs:
                imagens.append(img['src'])

        return {
            'nome': nome,
            'preco': preco,
            'descricao': descricao,
            'imagens': ', '.join(imagens)
        }
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a URL {url}: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro ao analisar a página {url}: {e}")
        return None

def main():
    try:
        with open("links.txt", "r", encoding="utf-8") as f:
            links = [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print("❌ Crie um arquivo 'links.txt' com um link do AliExpress por linha.")
        return

    produtos = []
    for link in links:
        print(f"🔍 Coletando: {link}")
        produto = coletar_produto_aliexpress(link)
        if produto:
            produtos.append(produto)
        time.sleep(2)  # evitar bloqueio

    if not produtos:
        print("❌ Nenhum produto coletado.")
        return

    with open("aliexpress_dropshipping.csv", "w", newline="", encoding="utf-8") as csvfile:
        campos = ["nome", "preco", "descricao", "imagens"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        writer.writerows(produtos)

    print("✅ Arquivo pronto: aliexpress_dropshipping.csv")

if __name__ == "__main__":
    main()