import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 400, 500  # Aumentamos la altura para acomodar el mensaje
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rompecabezas")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Tamaño y cantidad de piezas del rompecabezas
piece_size = 100
pieces_per_row = 2

# Crear piezas del rompecabezas con disposición inicial específica
pieces = [(0, 0), (0, 1), (1, 1), (1, 0)]

# Mezclar las piezas
random.shuffle(pieces)

# Función para dibujar las piezas en la pantalla
def draw_puzzle():
    for i, (row, col) in enumerate(pieces):
        pygame.draw.rect(screen, BLACK, (col * piece_size, row * piece_size, piece_size, piece_size), 2)
        pygame.draw.rect(screen, WHITE, (col * piece_size + 2, row * piece_size + 2, piece_size - 4, piece_size - 4))
        font = pygame.font.Font(None, 36)
        text = font.render(str(i + 1), True, BLACK)
        screen.blit(text, (col * piece_size + piece_size // 2 - text.get_width() // 2,
                           row * piece_size + piece_size // 2 - text.get_height() // 2))

# Función para verificar si el rompecabezas está resuelto
def is_puzzle_solved():
    sorted_pieces = [(i % pieces_per_row, i // pieces_per_row) for i in range(pieces_per_row ** 2)]
    return pieces == sorted_pieces

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            clicked_piece = (mouse_y // piece_size, mouse_x // piece_size)
            if clicked_piece in pieces:
                # Mezclar las piezas cercanas a la pieza clickeada
                adjacent_pieces = [(clicked_piece[0] + 1, clicked_piece[1]),
                                   (clicked_piece[0] - 1, clicked_piece[1]),
                                   (clicked_piece[0], clicked_piece[1] + 1),
                                   (clicked_piece[0], clicked_piece[1] - 1)]
                valid_adjacent_pieces = [piece for piece in adjacent_pieces if piece in pieces]
                if valid_adjacent_pieces:
                    random_adjacent_piece = random.choice(valid_adjacent_pieces)
                    pieces[pieces.index(clicked_piece)] = random_adjacent_piece
                    pieces[pieces.index(random_adjacent_piece)] = clicked_piece

    # Dibujar el rompecabezas en la pantalla
    screen.fill(WHITE)
    draw_puzzle()

    # Verificar si el rompecabezas está resuelto
    if is_puzzle_solved():
        font = pygame.font.Font(None, 24)
        text = font.render("¡FELICITACIONES, GANASTE!", True, RED)
        screen.blit(text, (width // 2 - text.get_width() // 2, height - 50))  # Ubicar debajo del rompecabezas

        

    pygame.display.flip()
