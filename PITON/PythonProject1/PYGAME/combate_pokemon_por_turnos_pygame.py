import pygame
import sys
import random

# Inicializar pygame
pygame.init()
from PIL import Image

im = Image.open("soloLevelingAtaque.gif")
frames = []

try:
    while True:
        frame = im.copy()
        frames.append(frame)
        im.seek(im.tell() + 1)
except EOFError:
    pass

# Guardar frames como PNG
for i, frame in enumerate(frames):
    frame.save(f"ataque_frame_{i}.png")

# ------------------ VARIABLES DE ANIMACIÓN ------------------
attacking = False
current_attack_frames = []
attack_frame_index = 0
attack_frame_delay = 5
attack_position = (0, 0)

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combate Pokémon por Turnos")


attack_frames = [pygame.image.load(f"ataque_frame_{i}.png").convert_alpha() for i in range(len(frames))]
attack_frame_index = 0
attack_frame_delay = 5
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

# ------------------ CLASES ------------------

class Move:
    def __init__(self, name, damage, status_effect=None, status_chance=0):
        self.name = name
        self.damage = damage
        self.status_effect = status_effect
        self.status_chance = status_chance

class Pokemon:
    def __init__(self, name, max_hp, moves):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.moves = moves
        self.status = None  # burn, poison, None

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def apply_status(self, status):
        if self.status is None:
            self.status = status

    def status_damage(self):
        if self.status == "burn":
            dmg = self.max_hp // 40
            self.take_damage(dmg)
            return f"{self.name} sufre daño por quemadura"
        if self.status == "poison":
            dmg = self.max_hp // 29
            self.take_damage(dmg)
            return f"{self.name} sufre daño por veneno"
        return None

# ------------------ MOVIMIENTOS ------------------

placaje = Move("Placaje", 5)
ascuas = Move("Ascuas", 5, status_effect="burn", status_chance=0.3)
latigo = Move("Látigo", 15)
veneno = Move("Tóxico", 10, status_effect="poison", status_chance=0.7)

# ------------------ POKÉMON ------------------

player_pokemon = Pokemon("Charmander", 100, [placaje, ascuas, veneno])
enemy_pokemon = Pokemon("Bulbasaur", 100, [placaje, latigo,veneno])

# ------------------ ESTADOS ------------------

PLAYER_TURN = "player"
ENEMY_TURN = "enemy"
GAME_OVER = "game_over"

state = PLAYER_TURN
message = "¡Elige un movimiento!"

# ------------------ FUNCIONES ------------------

def create_move_buttons(pokemon, sprite_rect):
    """Crea botones de movimientos debajo del sprite del Pokémon"""
    buttons = []
    start_x = sprite_rect.left
    start_y = sprite_rect.bottom + 10

    for i in range(len(pokemon.moves)):
        rect = pygame.Rect(start_x, start_y + i * 55, sprite_rect.width, 45)
        buttons.append(rect)
    return buttons

def reset_battle():
    global state, message, button_rects
    player_pokemon.hp = player_pokemon.max_hp
    enemy_pokemon.hp = enemy_pokemon.max_hp
    player_pokemon.status = None
    enemy_pokemon.status = None
    state = PLAYER_TURN
    message = "¡Elige un movimiento!"
    button_rects = create_move_buttons(player_pokemon, player_rect)

def draw_hp_bar(pokemon, sprite_rect):
    """Dibuja nombre, barra de vida y estado adaptados al sprite"""
    bar_width = sprite_rect.width
    bar_height = 15
    ratio = pokemon.hp / pokemon.max_hp

    # Posición de la barra sobre el sprite
    x = sprite_rect.left
    y = sprite_rect.top - 25  # barra debajo del nombre

    # Barra de fondo roja
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))
    # Barra verde proporcional
    pygame.draw.rect(screen, GREEN, (x, y, bar_width * ratio, bar_height))

    # Texto del HP actual / máximo centrado en la barra
    hp_text = f"{pokemon.hp}/{pokemon.max_hp}"
    hp_surface = font.render(hp_text, True, BLACK)
    hp_rect = hp_surface.get_rect(center=(x + bar_width // 2, y + bar_height // 2))
    screen.blit(hp_surface, hp_rect)

    # Nombre del Pokémon encima de la barra
    name_surface = font.render(pokemon.name, True, BLACK)
    name_rect = name_surface.get_rect(center=(x + bar_width // 2, y - 12))
    screen.blit(name_surface, name_rect)

    # Estado si existe encima de la barra
    if pokemon.status:
        status_surface = font.render(pokemon.status.upper(), True, RED)
        status_rect = status_surface.get_rect(center=(x + bar_width // 2, y - 25))
        screen.blit(status_surface, status_rect)

def draw_text(text, x, y, font=font, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def enemy_turn():
    global state, message
    # Daño por estado del jugador antes del turno enemigo
    status_msg = player_pokemon.status_damage()
    if status_msg:
        message = f"{status_msg}"

    if player_pokemon.hp > 0:
        # Elegir un movimiento aleatorio
        move = random.choice(enemy_pokemon.moves)
        player_pokemon.take_damage(move.damage)
        message += f" | {enemy_pokemon.name} usó {move.name}!"

        # Aplicar efectos de estado del movimiento
        if move.status_effect and random.random() < move.status_chance:
            player_pokemon.apply_status(move.status_effect)
            message += f" ¡{player_pokemon.name} fue {move.status_effect}!"

        # Daño por estado del enemigo (si tiene burn o poison)
        status_msg_enemy = enemy_pokemon.status_damage()
        if status_msg_enemy:
            message += f" | {status_msg_enemy}"

        # Verificar si el jugador murió
        if player_pokemon.hp <= 0:
            state = GAME_OVER
        else:
            state = PLAYER_TURN

# ------------------ SPRITES ------------------

player_sprite = pygame.image.load("sprites/Charmander.png").convert_alpha()
enemy_sprite = pygame.image.load("sprites/bulbasaur.png").convert_alpha()

player_sprite = pygame.transform.scale(player_sprite, (110, 110))
enemy_sprite = pygame.transform.scale(enemy_sprite, (120, 120))

player_rect = player_sprite.get_rect(topleft=(100, 250))
enemy_rect = enemy_sprite.get_rect(topleft=(600, 100))

# Botones iniciales
button_rects = create_move_buttons(player_pokemon, player_rect)
revenge_button = pygame.Rect(300, 500, 200, 50)

# ------------------ BUCLE PRINCIPAL ------------------

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # BOTÓN REVANCHA
        if state == GAME_OVER and event.type == pygame.MOUSEBUTTONDOWN:
            if revenge_button.collidepoint(event.pos):
                reset_battle()

        # TURNO JUGADOR
        if state == PLAYER_TURN:
            # Antes de atacar, aplicar daño por estado del jugador
            status_msg_player = player_pokemon.status_damage()
            if status_msg_player:
                message = status_msg_player

        if state == PLAYER_TURN and event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(mx, my):
                    move = player_pokemon.moves[i]

                    # Configurar animación
                    attacking = True
                    current_attack_frames = attack_frames  # todos los frames de tu GIF
                    attack_frame_index = 0
                    attack_position = enemy_rect.topleft  # sobre el enemigo

                    # Guardamos el movimiento para aplicar daño al final de la animación
                    pending_move = move

                    # Efectos de estado
                    if move.status_effect and random.random() < move.status_chance:
                        enemy_pokemon.apply_status(move.status_effect)
                        message += f" ¡{enemy_pokemon.name} fue {move.status_effect}!"
                        status_msg = enemy_pokemon.status_damage()
                        if status_msg:
                            message += f" | {status_msg}"

                    if enemy_pokemon.hp <= 0:
                        state = GAME_OVER
                    else:
                        state = ENEMY_TURN

    # TURNO ENEMIGO
    if state == ENEMY_TURN:
        pygame.time.delay(900)
        enemy_turn()

    # ------------------ DIBUJADO ------------------
    screen.fill(BLUE)
    # ------------------ ANIMACIÓN DE ATAQUE ------------------
    if attacking and player_pokemon.moves[0]:
        # Mostrar frame actual
        frame = current_attack_frames[attack_frame_index // attack_frame_delay]
        screen.blit(frame, attack_position)
        attack_frame_index += 1

        # Verificar si la animación terminó
        if attack_frame_index >= len(current_attack_frames) * attack_frame_delay:
            attacking = False

            # Aplicar daño y estado después de la animación
            enemy_pokemon.take_damage(pending_move.damage)
            message = f"{player_pokemon.name} usó {pending_move.name}!"

            if pending_move.status_effect and random.random() < pending_move.status_chance:
                enemy_pokemon.apply_status(pending_move.status_effect)
                message += f" ¡{enemy_pokemon.name} fue {pending_move.status_effect}!"
                status_msg = enemy_pokemon.status_damage()
                if status_msg:
                    message += f" | {status_msg}"

            # Revisar si el enemigo murió
            if enemy_pokemon.hp <= 0:
                state = GAME_OVER
            else:
                state = ENEMY_TURN

    # Sprites
    screen.blit(player_sprite, player_rect)
    screen.blit(enemy_sprite, enemy_rect)

    # Nombres

    # Barras de vida
    draw_hp_bar(player_pokemon, player_rect)
    draw_hp_bar(enemy_pokemon, enemy_rect)

    # Botones de movimiento
    if state == PLAYER_TURN:
        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, GRAY, rect)
            draw_text(player_pokemon.moves[i].name, rect.x + 10, rect.y + 10)

    # Mensaje dinámico debajo de los botones
    draw_text(message, player_rect.left, player_rect.bottom + len(button_rects)*55 + 20, big_font)

    # Game Over
    if state == GAME_OVER:
        end_text = "¡Has perdido!" if player_pokemon.hp <= 0 else "¡Has ganado!"
        draw_text(end_text, 300, 450, big_font, RED)
        pygame.draw.rect(screen, BLUE, revenge_button)
        draw_text("Revancha", revenge_button.x + 50, revenge_button.y + 15, big_font, WHITE)

    pygame.display.flip()

pygame.quit()
sys.exit()
