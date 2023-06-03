import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definindo as dimensões da janela
largura_janela = 800
altura_janela = 600

# Criando a janela do jogo
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Pedra, Papel e Tesoura")

# Definindo as posições dos botões
botao_posicoes = [(125, 400), (325, 400), (525, 400)]
botao_dimensoes = [(100, 100), (100, 100), (100, 100)]
botao_texto = ["Pedra", "Papel", "Tesoura"]

# Definindo o estado inicial do jogo
jogador_escolha = None
ia_escolha = None
resultado = None

# Função para desenhar os botões
def desenhar_botoes():
    for i in range(3):
        pygame.draw.rect(janela, VERMELHO, (botao_posicoes[i], botao_dimensoes[i]))
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(botao_texto[i], True, BRANCO)
        texto_retangulo = texto.get_rect()
        texto_retangulo.center = botao_posicoes[i][0] + botao_dimensoes[i][0] / 2, botao_posicoes[i][1] + botao_dimensoes[i][1] / 2
        janela.blit(texto, texto_retangulo)

# Função para desenhar o resultado na tela
def desenhar_resultado():
    fonte = pygame.font.Font(None, 48)
    if resultado == "Empate":
        texto = fonte.render("Empate!", True, AZUL)
    elif resultado == "Jogador":
        texto = fonte.render("Você venceu!", True, VERDE)
    elif resultado == "IA":
        texto = fonte.render("Você perdeu!", True, VERMELHO)
    texto_retangulo = texto.get_rect()
    texto_retangulo.center = largura_janela / 2, altura_janela / 2
    janela.blit(texto, texto_retangulo)

# Função para verificar quem venceu
def verificar_vencedor(jogador, ia):
    if jogador == ia:
        return "Empate"
    elif (jogador == "Pedra" and ia == "Tesoura") or (jogador == "Papel" and ia == "Pedra") or (jogador == "Tesoura" and ia == "Papel"):
        return "Jogador"
    else:
        return "IA"

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and resultado is None:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(3):
                if botao_posicoes[i][0] <= mouse_pos[0] <= botao_posicoes[i][0] + botao_dimensoes[i][0] and botao_posicoes[i][1] <= mouse_pos[1] <= botao_posicoes[i][1] + botao_dimensoes[i][1]:
                    jogador_escolha = botao_texto[i]
                    ia_escolha = random.choice(botao_texto)
                    resultado = verificar_vencedor(jogador_escolha, ia_escolha)

    janela.fill(BRANCO)
    desenhar_botoes()

    if resultado is not None:
        desenhar_resultado()

    pygame.display.update()

# Encerrando o Pygame
pygame.quit()
