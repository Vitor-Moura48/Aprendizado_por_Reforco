from Config import *
import Variaveis_globais as Variaveis_globais


class Colisoes:
    def __init__(self):
        pass

    # função para conferir as colisões com o player
    def colisao_player_inimigo(self):

        # para evitar que um individuo seja atingido por um inimigo e saia do limite da tela ao mesmo tempo (daria erro)
        self.colidiu = False

        # confere se cada inimigo colidiu com o player
        for player in Variaveis_globais.grupo_processadores:
            for inimigo in Variaveis_globais.grupo_inimigos:
              
                if player.rect_player.colliderect(inimigo.rect_inimigo):
                
   
                    # se sim, vai remover o player do grupo de players
                    Variaveis_globais.grupo_processadores.remove(player)

                    # obter o tempo de vida do individuo
                    tempo_de_vida = player.funcao_de_perda()

                    if Variaveis_globais.partida_atual_da_geracao == 0:
                      
                        # enviar os pesos do individuo para a lista da geração
                        pesos_individuo = []
                        pesos_individuo.append([tempo_de_vida])
                        for camada in player.camadas:
                            pesos_individuo.append(camada)

                    # coloca os pesos do individuo no indice escolhido no inicio da geração
                        Variaveis_globais.geracao_atual[player.indice] = pesos_individuo
                    
                    else:
                        Variaveis_globais.geracao_atual[player.indice][0][0] += tempo_de_vida

                    # avisa que o player já colidiu
                    self.colidiu = True

                    # se um inimigo já tiver colidido, não é mais necessario fazer mais verificações
                    break

    def colisao_player_tela(self):

        # confere se o player saiu dos limites da tela
        for player in Variaveis_globais.grupo_processadores:
            if player.rect_player.bottom < 0 or player.rect_player.top > altura or \
                    player.rect_player.left < 0 or player.rect_player.right > largura and not self.colidiu:

                # se saiu, faz a mesma coisa da colisão com um inimigo
                if player in Variaveis_globais.grupo_processadores:
                    Variaveis_globais.grupo_processadores.remove(player)
                    
                    # pune os individuos que colidiram com a tela
                    tempo_de_vida = player.funcao_de_perda() * 0.8

                    if Variaveis_globais.partida_atual_da_geracao == 0:
                       
                        pesos_individuo = []
                        pesos_individuo.append([tempo_de_vida])
                        for camada in player.camadas:
                            pesos_individuo.append(camada)
                        

                        Variaveis_globais.geracao_atual[player.indice] = pesos_individuo

                    else:
                        Variaveis_globais.geracao_atual[player.indice][0][0] += tempo_de_vida

                        

    def update(self):
        self.colisao_player_inimigo()
        self.colisao_player_tela()

