import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combate Pokémon por Turnos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
GRAY = (200, 200, 200)

# Fuente
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Pokemon:
    def __init__(self, name, max_hp, moves):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.moves = moves

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

# Crear movimientos
placaje = Move("Placaje", 20)
ascuas = Move("Ascuas", 25)
latigo = Move("Látigo", 15)

# Crear pokémon
player_pokemon = Pokemon("Charmander", 100, [placaje, ascuas])
enemy_pokemon = Pokemon("Bulbasaur", 100, [placaje, latigo])

# Estados del juego
PLAYER_TURN = "player"
ENEMY_TURN = "enemy"
GAME_OVER = "game_over"

state = PLAYER_TURN
message = "¡Elige un movimiento!"

# Botones de movimientos
button_rects = []
for i in range(2):
    rect = pygame.Rect(50, 400 + i * 60, 200, 50)
    button_rects.append(rect)


def draw_hp_bar(x, y, pokemon):
    bar_width = 200
    bar_height = 20
    ratio = pokemon.hp / pokemon.max_hp
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
    pygame.draw.rect(screen, GREEN, (x, y, bar_width * ratio, bar_height))
 # Texto HP actual / HP máximo
    hp_text = f"{pokemon.hp} / {pokemon.max_hp}"
    text_surface = font.render(hp_text, True, BLACK)

    # Centrar el texto sobre la barra
    text_rect = text_surface.get_rect(center=(x + bar_width // 2, y + bar_height // 2))
    screen.blit(text_surface, text_rect)

def draw_text(text, x, y, font=font, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def enemy_turn():
    global state, message
    move = enemy_pokemon.moves[0]
    player_pokemon.take_damage(move.damage)
    message = f"{enemy_pokemon.name} usó {move.name}!"
    if player_pokemon.hp <= 0:
        state = GAME_OVER
    else:
        state = PLAYER_TURN

# Bucle principal

player_sprite = pygame.image.load("sprites/Charmander.png").convert_alpha()
enemy_sprite = pygame.image.load("sprites/bulbasaur.png").convert_alpha()

# Escalar (opcional pero recomendado)
player_sprite = pygame.transform.scale(player_sprite, (110, 110))
enemy_sprite = pygame.transform.scale(enemy_sprite, (120, 120))


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == PLAYER_TURN and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mx, my):
                    move = player_pokemon.moves[i]
                    enemy_pokemon.take_damage(move.damage)
                    message = f"{player_pokemon.name} usó {move.name}!"
                    if enemy_pokemon.hp <= 0:
                        state = GAME_OVER
                    else:
                        state = ENEMY_TURN

    # Turno enemigo automático
    if state == ENEMY_TURN:
        pygame.time.delay(900)
        enemy_turn()

    # Dibujar pantalla
    screen.fill(WHITE)

    # Pokémon (rectángulos de ejemplo)
    screen.blit(player_sprite, (100, 250))
    screen.blit(enemy_sprite, (600, 100))

    # Nombres y HP
    draw_text(player_pokemon.name, 50, 220)
    draw_hp_bar(50, 245, player_pokemon)


    draw_text(enemy_pokemon.name, 550, 70)
    draw_hp_bar(550, 95, enemy_pokemon)

    # Mensaje
    draw_text(message, 50, 350, big_font)

    # Botones
    if state == PLAYER_TURN:
        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, GRAY, rect)
            draw_text(player_pokemon.moves[i].name, rect.x + 10, rect.y + 15)

    # Game Over
    if state == GAME_OVER:
        if player_pokemon.hp <= 0:
            end_text = "¡Has perdido!"
        else:
            end_text = "¡Has ganado!"
        draw_text(end_text, 300, 500, big_font, RED)

    pygame.display.flip()

pygame.quit()
sys.exit()
