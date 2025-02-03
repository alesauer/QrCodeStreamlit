# 🚀 Gerador de QR Code com Streamlit

![QR Code Example](https://img.icons8.com/color/96/000000/qr-code--v1.png) 

Um aplicativo web simples para gerar QR Codes a partir de URLs, construído com Python e Streamlit.

## 🌟 Funcionalidades

- 🔗 Conversão instantânea de URLs em QR Codes
- 📥 Download do QR Code gerado em formato PNG
- 🎨 Personalização de cores e tamanho do QR Code
- 📱 Compatível com dispositivos móveis e desktop

## 🛠️ Como Usar

1. **Instalação das dependências**:
```bash
pip install streamlit qrcode[pil] Pillow
```

2. **Executar o aplicativo**:
```bash
streamlit run app.py
```

3. **No navegador**:
   - Cole sua URL no campo de texto
   - O QR Code será gerado automaticamente
   - Clique em "Baixar QR Code" para salvar a imagem

## ⚙️ Personalização
No código `app.py` você pode alterar:
```python
# Cores (altere "black" e "white")
qr.make_image(fill_color="black", back_color="white")

# Tamanho dos blocos (box_size=10)
# Borda (border=4)
```

## 🧩 Tecnologias Utilizadas
- 🐍 Python 3
- 🎈 Streamlit (Interface Web)
- 🔳 QRCode (Geração de QR Codes)
- 🖼️ Pillow (Manipulação de imagens)

## 📄 Licença
Este projeto está sob licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes
