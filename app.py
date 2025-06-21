import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Pasta de saída
PASTA_SAIDA = "output"
os.makedirs(PASTA_SAIDA, exist_ok=True)

# Paleta de cores
COR_PRIMARIA = "#690A22"
COR_FUNDO = "#DDDDDD"
FONTE = "Courier"

class AplicativoProcessamentoImagem:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Trabalho PDI")
        self.raiz.geometry("900x750")
        self.raiz.configure(bg=COR_FUNDO)
        self.caminho_imagem = None
        self.imagem_original = None
        self.imagem_processada = None
        
        self.criar_cabecalho()
        self.criar_botoes()

    def criar_cabecalho(self):
        quadro_cabecalho = tk.Frame(self.raiz, bg=COR_PRIMARIA, height=80)
        quadro_cabecalho.pack(fill=tk.X)

        rotulo_titulo = tk.Label(quadro_cabecalho, text="Trabalho PDI", fg="white", bg=COR_PRIMARIA,
                                font=(FONTE, 26, "bold"))
        rotulo_titulo.place(x=20, y=10)

        rotulo_nome = tk.Label(quadro_cabecalho, text="Lucas Souza e Silva - 7561", fg="white", bg=COR_PRIMARIA,
                                font=(FONTE, 14))
        rotulo_nome.place(x=20, y=50)

        botao_carregar = tk.Button(quadro_cabecalho, text="Carregar imagem", command=self.carregar_imagem,
                                bg="white", fg=COR_PRIMARIA, font=(FONTE, 12, "bold"), padx=10, pady=5)
        botao_carregar.place(x=730, y=20)

    def criar_botoes(self):
        tk.Label(self.raiz, text="Escolha uma das opções:", bg=COR_FUNDO,
                 font=(FONTE, 20, "bold"), fg=COR_PRIMARIA).pack(pady=20)

        quadro_botoes = tk.Frame(self.raiz, bg=COR_FUNDO)
        quadro_botoes.pack()

        funcionalidades = [
            ("Histograma", self.histograma),
            ("Equalização de Histograma", self.equalizacao_histograma),
            ("Filtro da Mediana", self.filtro_mediana),
            ("Alargamento de Contraste", self.alargamento_contraste),
            ("Filtro da Média", self.filtro_media),
            ("Filtro Gaussiano", self.filtro_gaussiano),
            ("Filtro Máximo", self.filtro_maximo),
            ("Filtro Mínimo", self.filtro_minimo),
            ("Filtro Laplaciano", self.filtro_laplaciano),
            ("Filtro Prewitt", self.filtro_prewitt),
            ("Filtro Sobel", self.filtro_sobel),
            ("Filtro Roberts", self.filtro_roberts),
            ("Espectro de Fourier", self.espectro_fourier),
            ("Convolução", self.convolucao_frequencia),
            ("Erosão", self.erosao),
            ("Dilatação", self.dilatacao),
            ("Método de Otsu", self.metodo_otsu),
            ("Visualizar Imagem em Cinza", self.visualizar_imagem)
        ]

        for indice, (texto, comando) in enumerate(funcionalidades):
            linha = indice // 3
            coluna = indice % 3
            botao = tk.Button(quadro_botoes, text=texto, command=comando,
                              bg=COR_PRIMARIA, fg="white", width=25, height=2,
                              font=("Segoe UI", 10, "bold"))
            botao.grid(row=linha, column=coluna, padx=10, pady=10)

        botao_salvar = tk.Button(self.raiz, text="Salvar imagem", command=self.salvar_imagem,
                                  bg="white", fg=COR_PRIMARIA, font=("Segoe UI", 14, "bold"), padx=20, pady=10)
        botao_salvar.pack(pady=30)

    def carregar_imagem(self):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de imagem", "*.jpg;*.png;*.bmp;*.tif")])
        if caminho_arquivo:
            self.caminho_imagem = caminho_arquivo
            imagem = cv2.imread(caminho_arquivo)
            if imagem is None:
                messagebox.showerror("Erro", "Não foi possível carregar a imagem.")
                return
            if len(imagem.shape) == 3:
                imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            self.imagem_original = imagem
            self.imagem_processada = imagem.copy()
            messagebox.showinfo("Imagem carregada", "Imagem carregada com sucesso!")

    def salvar_imagem(self):
        if self.imagem_processada is not None:
            nome_arquivo = os.path.join(PASTA_SAIDA, "imagem_processada.png")
            cv2.imwrite(nome_arquivo, self.imagem_processada)
            messagebox.showinfo("Sucesso", f"Imagem salva em {nome_arquivo}")
        else:
            messagebox.showwarning("Aviso", "Nenhuma imagem processada para salvar!")

    def histograma(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        hist = cv2.calcHist([self.imagem_original], [0], None, [256], [0, 256])
        plt.figure("Histograma")
        plt.title("Histograma da Imagem")
        plt.xlabel("Intensidade (0-255)")
        plt.ylabel("Número de Pixels")
        plt.plot(hist, color='black')
        plt.xlim([0, 256])
        plt.grid()
        plt.show()

    def equalizacao_histograma(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.equalizeHist(self.imagem_original)
        self.visualizar_imagem_processada("Equalização de Histograma")

    def filtro_mediana(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.medianBlur(self.imagem_original, 5)
        self.visualizar_imagem_processada("Filtro Mediana")

    def alargamento_contraste(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        minimo = np.min(self.imagem_original)
        maximo = np.max(self.imagem_original)
        self.imagem_processada = ((self.imagem_original - minimo) * (255 / (maximo - minimo))).astype(np.uint8)
        self.visualizar_imagem_processada("Alargamento de Contraste")

    def filtro_media(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.blur(self.imagem_original, (5,5))
        self.visualizar_imagem_processada("Filtro Média")

    def filtro_gaussiano(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.GaussianBlur(self.imagem_original, (5,5), 0)
        self.visualizar_imagem_processada("Filtro Gaussiano")

    def filtro_maximo(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.dilate(self.imagem_original, np.ones((5,5), np.uint8))
        self.visualizar_imagem_processada("Filtro Máximo")

    def filtro_minimo(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.erode(self.imagem_original, np.ones((5,5), np.uint8))
        self.visualizar_imagem_processada("Filtro Mínimo")

    def filtro_laplaciano(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        self.imagem_processada = cv2.Laplacian(self.imagem_original, cv2.CV_64F)
        self.imagem_processada = cv2.convertScaleAbs(self.imagem_processada)
        self.visualizar_imagem_processada("Filtro Laplaciano")

    def filtro_prewitt(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
        kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        img_prewittx = cv2.filter2D(self.imagem_original, -1, kernelx)
        img_prewitty = cv2.filter2D(self.imagem_original, -1, kernely)
        self.imagem_processada = cv2.addWeighted(img_prewittx, 0.5, img_prewitty, 0.5, 0)
        self.visualizar_imagem_processada("Filtro Prewitt")

    def filtro_sobel(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        sobelx = cv2.Sobel(self.imagem_original, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(self.imagem_original, cv2.CV_64F, 0, 1, ksize=5)
        sobel = cv2.magnitude(sobelx, sobely)
        self.imagem_processada = cv2.convertScaleAbs(sobel)
        self.visualizar_imagem_processada("Filtro Sobel")

    def filtro_roberts(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernelx = np.array([[1, 0], [0, -1]])
        kernely = np.array([[0, 1], [-1, 0]])
        img_robertsx = cv2.filter2D(self.imagem_original, -1, kernelx)
        img_robertsy = cv2.filter2D(self.imagem_original, -1, kernely)
        self.imagem_processada = cv2.addWeighted(img_robertsx, 0.5, img_robertsy, 0.5, 0)
        self.visualizar_imagem_processada("Filtro Roberts")

    def espectro_fourier(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        f = np.fft.fft2(self.imagem_original)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift))
        plt.figure("Espectro de Fourier")
        plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title("Espectro de Fourier")
        plt.axis('off')
        plt.show()

    def convolucao_frequencia(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        # Exemplo de filtro gaussiano no domínio da frequência
        dft = cv2.dft(np.float32(self.imagem_original), flags = cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        rows, cols = self.imagem_original.shape
        crow,ccol = rows//2 , cols//2
        mask = np.zeros((rows, cols, 2), np.uint8)
        r = 30
        center = [crow, ccol]
        x, y = np.ogrid[:rows, :cols]
        mask_area = (x - center[0])**2 + (y - center[1])**2 <= r*r
        mask[mask_area] = 1
        fshift = dft_shift * mask
        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv2.idft(f_ishift)
        img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
        self.imagem_processada = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        self.visualizar_imagem_processada("Convolução no Domínio da Frequência")

    def erosao(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernel = np.ones((5,5), np.uint8)
        self.imagem_processada = cv2.erode(self.imagem_original, kernel, iterations=1)
        self.visualizar_imagem_processada("Erosão")

    def dilatacao(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        kernel = np.ones((5,5), np.uint8)
        self.imagem_processada = cv2.dilate(self.imagem_original, kernel, iterations=1)
        self.visualizar_imagem_processada("Dilatação")

    def metodo_otsu(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        _, self.imagem_processada = cv2.threshold(self.imagem_original, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.visualizar_imagem_processada("Segmentação com Otsu")

    def visualizar_imagem(self):
        if self.imagem_original is None:
            messagebox.showwarning("Aviso", "Carregue uma imagem primeiro!")
            return
        plt.figure("Imagem em Escala de Cinza")
        plt.imshow(self.imagem_original, cmap='gray')
        plt.title("Imagem Carregada (Cinza)")
        plt.axis('off')
        plt.show()

    def visualizar_imagem_processada(self, titulo):
        plt.figure(titulo)
        plt.imshow(self.imagem_processada, cmap='gray')
        plt.title(titulo)
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    raiz = tk.Tk()
    app = AplicativoProcessamentoImagem(raiz)
    raiz.mainloop()
