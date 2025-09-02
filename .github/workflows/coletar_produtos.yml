name: Coletar Produtos do AliExpress

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run Python script
        run: python coletar_produtos.py

      - name: Commit JSON back to repo
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add dados_dos_produtos.json
          git commit -m "Atualiza dados coletados automaticamente" || echo "Sem mudanças para commitar"
          git push

      - name: Upload JSON file
        uses: actions/upload-artifact@v4
        with:
          name: dados-coletados
          path: dados_dos_produtos.json
