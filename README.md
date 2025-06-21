# Trabalho de Processamento Digital de Imagens (PDI)

### Autor: Lucas Souza e Silva - 7561

---

## Descrição do Projeto

Este projeto foi desenvolvido como atividade acadêmica para a disciplina de **Processamento Digital de Imagens (PDI)**. Trata-se de um sistema com interface gráfica completa que permite o carregamento e processamento de imagens em tons de cinza, com múltiplas técnicas de pré-processamento, filtragem e segmentação.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x  
- **Interface Gráfica:** Tkinter  
- **Bibliotecas:**
  - `OpenCV` (opencv-python, opencv-contrib-python): para processamento digital de imagens.
  - `Pillow`: suporte para imagens no Tkinter.
  - `Matplotlib`: visualização gráfica (histogramas, espectro de Fourier, visualização de imagens).

---

## Funcionalidades Implementadas

- ✅ Carregamento de imagem (RGB ou Tons de Cinza)
- ✅ Conversão automática para Tons de Cinza (se necessário)
- ✅ Visualização da imagem carregada
- ✅ Exibição de Histograma
- ✅ Equalização de Histograma
- ✅ Alargamento de Contraste
- ✅ Filtros Passa-Baixa:
  - Filtro da Média
  - Filtro Gaussiano
  - Filtro da Mediana
  - Filtro Máximo
  - Filtro Mínimo
- ✅ Filtros Passa-Alta:
  - Filtro Laplaciano
  - Filtro Prewitt
  - Filtro Sobel
  - Filtro Roberts
- ✅ Transformada de Fourier (visualização do espectro)
- ✅ Convolução no Domínio da Frequência (Exemplo Gaussiano)
- ✅ Morfologia Matemática:
  - Erosão
  - Dilatação
- ✅ Segmentação com **Método de Otsu**
- ✅ Salvar imagem processada

---

## Como Executar o Projeto

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd nome-do-repositorio
```

### 2️⃣ Criar o ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Projeto

```bash
python nome_do_arquivo.py
```

> Obs: `nome_do_arquivo.py` é o nome do seu arquivo principal (provavelmente `app.py` ou `pdi.py`, ou como você nomeou).

---

## Arquivo de Dependências (`requirements.txt`)

Exemplo de conteúdo para o arquivo:

```
opencv-python==4.9.0.80
opencv-contrib-python==4.9.0.80
Pillow==10.3.0
matplotlib==3.8.4
```

---

## Observações

- O sistema suporta imagens nos formatos `.jpg`, `.png`, `.bmp`, `.tif`.
- Todas as operações são realizadas em imagens monocromáticas (tons de cinza).
- A pasta `output/` será criada automaticamente para salvar as imagens processadas.
