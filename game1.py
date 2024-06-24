import pygame
import random
import time

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Teka Warna Bunga")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "purple": (128, 0, 128)
}

# Font
font = pygame.font.SysFont(None, 55)

# Fungsi untuk menampilkan pesan
def show_message(message, color, y_offset=0):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2 + y_offset))
    screen.blit(text, text_rect)

# Fungsi untuk permainan utama
def game():
    score = 0
    running = True

    while running:
        screen.fill(white)
        
        # Pilih warna acak
        color_name = random.choice(list(colors.keys()))
        color_value = colors[color_name]

        # Gambar bunga (lingkaran) dengan warna acak
        pygame.draw.circle(screen, color_value, (screen_width//2, screen_height//2 - 50), 50)

        # Tampilkan pesan untuk menebak warna
        show_message("Teka warna bunga ini!", black, -100)
        pygame.display.flip()

        # Ambil input dari pemain
        start_time = time.time()
        guess = None

        while time.time() - start_time < 5:  # Pemain punya waktu 5 detik untuk menebak
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        guess = "red"
                    elif event.key == pygame.K_g:
                        guess = "green"
                    elif event.key == pygame.K_b:
                        guess = "blue"
                    elif event.key == pygame.K_y:
                        guess = "yellow"
                    elif event.key == pygame.K_p:
                        guess = "purple"

            if guess:
                break

        # Periksa jawaban pemain
        if guess == color_name:
            score += 1
            show_message("Betul!", black)
        else:
            show_message(f"Salah! Jawapannya: {color_name}", black)

        pygame.display.flip()
        time.sleep(2)

        # Bersihkan layar
        screen.fill(white)
        show_message(f"Skor: {score}", black)
        pygame.display.flip()
        time.sleep(2)

    pygame.quit()

# Mulai permainan
game()