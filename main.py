# Olá, bem venidos ao jogo_grafos
# PARA INICIAR: digite no terminal do VS Code "python main.py"
# OBJETIVO: levar a bolinha azul (jogador) até a vermelha (destino)
# REGRA: só dá para andar entre vértices ligados por uma linha (aresta)

import random
import tkinter as tk
from tkinter import messagebox

# VÉRTICES: número = nome, (x, y) = posição na tela
vertices = {
    1: (100, 200),
    2: (260, 80),
    3: (260, 320),
    4: (420, 200),
    5: (580, 80),
    6: (580, 320),
    7: (680, 200),
}

# ARESTAS: linhas que ligam os vértices (nós)
arestas = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 7), (6, 7)]

pontos = 0 #começa com estes pontos
jogador = 1 #começa neste ponto (numero 1)


# vertices (nós) vizinhos ex: 1 2 (ligados pela mesma linha)
def vizinhos(v):
    return [b if a == v else a for a, b in arestas if v in (a, b)]


# sorteia um destino que NÃO seja o jogador nem um vizinho dele
def sortear_destino():
    opcoes = [v for v in vertices if v != jogador and v not in vizinhos(jogador)]
    return random.choice(opcoes)


destino = sortear_destino()

janela = tk.Tk()
janela.title("Jogo do Grafo")
janela.resizable(False, False)
messagebox.showinfo("Jogo do Grafo", "Leve a bolinha azul até a vermelha!\nClique nas bolinhas com borda verde.\nA cada acerto, a vermelha muda de lugar!")

tela = tk.Canvas(janela, width=760, height=400, bg="#1e1e2e", highlightthickness=0)
tela.pack()


# O que você ve ao rodar
def desenhar():
    tela.delete("all")
    tela.create_text(380, 25, text=f"Pontos: {pontos}", fill="white", font=("Segoe UI", 18, "bold"))
    tela.create_text(380, 385, text="Clique nas bolinhas com borda verde", fill="#a6adc8", font=("Segoe UI", 11))

    for a, b in arestas:
        tela.create_line(vertices[a], vertices[b], width=4, fill="#585b70")

    for numero, (x, y) in vertices.items():
        cor, borda, largura = "#cdd6f4", "#45475a", 3
        if numero == destino:
            cor = "#f38ba8"                    # vermelho
        if numero == jogador:
            cor = "#89b4fa"                    # azul
        if numero in vizinhos(jogador):
            borda, largura = "#ffffff", 5      # borda verde = pode ir
        tela.create_oval(x - 28, y - 28, x + 28, y + 28, fill=cor, outline=borda, width=largura)
        tela.create_text(x, y, text=str(numero), fill="#1e1e2e", font=("Segoe UI", 16, "bold"))


# roda quando o jogador clica na tela
def clicou(evento):
    global jogador, destino, pontos
    for numero in vizinhos(jogador):
        x, y = vertices[numero]
        if abs(evento.x - x) < 28 and abs(evento.y - y) < 28:
            jogador = numero
            if jogador == destino:
                pontos += 1
                destino = sortear_destino()
                desenhar()
                messagebox.showinfo("Acertou!", f"Pontos: {pontos}\nA vermelha mudou de lugar!")
            else:
                desenhar()
            return


tela.bind("<Button-1>", clicou)
desenhar()
janela.mainloop()