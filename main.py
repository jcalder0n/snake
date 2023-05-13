import pygame

# Inicializar Pygame
pygame.init()

# Establecer las dimensiones de la pantalla
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

# Establecer el título de la ventana
pygame.display.set_caption("Snake Game")

# Iniciar el bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la pantalla
    pygame.display.update()
    
# Definir la posición inicial de la serpiente
snake_pos = [100, 50]

# Definir el tamaño de la serpiente
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_size = 10

# Dibujar la serpiente
for pos in snake_body:
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], snake_size, snake_size))

