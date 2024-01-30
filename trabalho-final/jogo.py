# Biblioteca PyGame
import pygame
# Biblioteca para geracao de numeros pseudoaleatorios
import random
# Modulo da biblioteca PyGame que permite o acesso as teclas utilizadas
from pygame.locals import *

# Classe que representa o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        harry = pygame.image.load('harry_potter.png')
        self.surf = harry
        self.rect = pygame.Rect(random.randint(820, 900), random.randint(0, 600), 80, 46)
        self.rect = harry.get_rect()

    # Determina acao de movimento conforme teclas pressionadas
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -6)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 6)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6, 0)
        if pressed_keys[K_RIGHT]: 
            self.rect.move_ip(6, 0)

        # Mantem o jogador nos limites da tela do jogo
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 448:
            self.rect.bottom = 448

# Classe que representa os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self, dificuldade):
        super(Enemy, self).__init__()
        dementador = pygame.image.load('dementador.png')
        self.surf = dementador
        self.rect = pygame.Rect(random.randint(820, 900), random.randint(0, 600), 48, 48)
        self.rect = dementador.get_rect( #Coloca na extrema direita (entre 820 e 900) e sorteia sua posicao em relacao a coordenada y (entre 0 e 600)
            center=(random.randint(820, 900), random.randint(0, 600))
        )
        self.velocity = random.uniform(3, 8) * dificuldade #Sorteia sua velocidade, entre 3 e 8

    # Funcao que atualiza a posiçao do inimigo em funcao da sua velocidade e termina com ele quando ele atinge o limite esquerdo da tela (x < 0)
    def update(self):
        self.rect.move_ip(-self.velocity, 0)
        if self.rect.right < 0:
            self.kill()
            
game_over_displayed = False
def waiting(screen, running):
    waiting = True
    while waiting:
        tela_inicial(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                waiting = False
                running = False
            if event.type == pygame.KEYUP:
                waiting = False
                running = True

def running(screen, pontos, high_score):

    clock = pygame.time.Clock()
    ADDTIME = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDTIME, 1000)
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 300)
    pontos = 0
    dificuldade = 1
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(-1)
    player = Player()
    background = pygame.Surface(screen.get_size())
    fundo = pygame.image.load('background.jpg')
    background = fundo

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    font_pontos = pygame.font.Font('ThaleahFat.ttf', 32)
    textRect = font_pontos.render("SCORE: " + str(pontos), True, (128, 0, 0))
    textRect = textRect.get_rect()
    textRect.center = (400, 20)

    running = True
    kill = False


    while running == True and kill == False:
        clock.tick(60)
        screen.blit(background, (0, 0))
        text_pontos = font_pontos.render("SCORE: " + str(pontos), True, (128, 0, 0))
        textRect = text_pontos.get_rect()
        textRect.center = (400, 20)
        screen.blit(text_pontos, textRect)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            for sprite in all_sprites:
                sprite.kill()
            kill = True
            gameOver(screen, pontos, high_score, kill)
        
        if pontos > high_score:
            high_score = pontos

        for event in pygame.event.get():
            if event.type == ADDTIME and kill == False:
                pontos += 1
                dificuldade += 0.01

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_SPACE:
                    pontos = 0
                    kill = False
                    game_over_displayed = False
            elif event.type == QUIT:
                pygame.quit()
            elif event.type == ADDENEMY:
                new_enemy = Enemy(dificuldade)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        pygame.display.flip()
    return pontos, high_score

# Define a função `tela_inicial`
def tela_inicial(screen):
    font_init = pygame.font.Font('ThaleahFat.ttf', 32)
    text_init = font_init.render("Harry Python and the Sorcerer's Code", True, (219, 172, 52), (0, 0, 0))
    textRect = text_init.get_rect()
    textRect.midtop = (400, 180)
    screen.blit(text_init, textRect)
    font_init = pygame.font.Font('ThaleahFat.ttf', 28)
    text_init = font_init.render("PRESSIONE UMA TECLA PARA INICIAR", True, (128, 0, 0), (0, 0, 0))
    textRect = text_init.get_rect()
    textRect.midtop = (400, 224)
    screen.blit(text_init, textRect)
    pygame.display.flip()

def gameOver(screen, pontos, high_score, kill):
    screen.fill((0, 0, 0))
    font_game_over = pygame.font.Font('ThaleahFat.ttf', 32)
    text_game_over = font_game_over.render("GAME OVER", True, (128, 0, 0))
    textRect = text_game_over.get_rect()
    screen.blit(text_game_over, (328, 198))

    if pontos > high_score:
        high_score = pontos

    font_restart = pygame.font.Font('ThaleahFat.ttf', 20)
    text_restart = font_restart.render("HIGH SCORE:" + str(high_score), True, (0, 100, 0))
    textRect = text_restart.get_rect()
    screen.blit(text_restart, (345, 227))

    font_restart = pygame.font.Font('ThaleahFat.ttf', 20)
    text_restart = font_restart.render("Pressione SPACE para reiniciar", True, (0, 0, 205))
    textRect = text_restart.get_rect()
    screen.blit(text_restart, (265, 250))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == QUIT:
                pygame.quit()


    return pontos, high_score


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 448))
    pygame.display.set_caption("Harry Python and the Sorcerer's Code")
    kill = False
    high_score = 0
    pontos = 0
    dificuldade = 1
    tela_inicial(screen)
    waiting(screen, running)
    while kill == False and game_over_displayed == False:
        pontos, high_score = running(screen, pontos, high_score)


if __name__ == "__main__":
    main()