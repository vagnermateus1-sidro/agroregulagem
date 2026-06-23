"""Gera icon-180.png para iOS a partir do logo.jpg"""
from PIL import Image
import os

pasta = os.path.dirname(os.path.abspath(__file__))
logo  = os.path.join(pasta, "logo.jpg")
saida = os.path.join(pasta, "icon-180.png")

img = Image.open(logo).convert("RGBA")
img = img.resize((180, 180), Image.LANCZOS)
img.save(saida, "PNG")
print(f"Ícone iOS gerado: {saida}")
