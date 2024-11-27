import pygame
import time

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIME = (0, 255, 0)

# Bildschirmgröße
WIDTH, HEIGHT = 400, 400

# LED-Größe und Abstände
LED_RADIUS = 15
X_SPACING = 100
Y_SPACING = 40
MARGIN_TOP = 50
MARGIN_LEFT = 50

# Pygame initialisieren
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binäre Uhr")
clock = pygame.time.Clock()

# Schriftart
font = pygame.font.SysFont("Arial", 20)

def draw_leds(screen, x_offset, y_offset, value):
    """Zeichnet die LEDs in binärer Darstellung."""
    binary = bin(value)[2:].zfill(6)  # Binärdarstellung mit führenden Nullen

    for i, bit in enumerate(binary):
        color = LIME if bit == '1' else GRAY
        y_pos = y_offset + i * Y_SPACING
        pygame.draw.circle(screen, color, (x_offset, y_pos), LED_RADIUS)

        # Wertbeschriftung hinzufügen
        label = font.render(str(2 ** (5 - i)), True, WHITE)
        screen.blit(label, (x_offset + 2 * LED_RADIUS, y_pos - LED_RADIUS // 2))

def update_binary_clock():
    """Aktualisiert die Anzeige der Binäruhr."""
    # Aktuelle Zeit abrufen
    now = time.localtime()
    hours, minutes, seconds = now.tm_hour, now.tm_min, now.tm_sec

    # Bildschirm löschen
    screen.fill(BLACK)

    # Überschrift
    title = font.render("Binäre Uhr", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))

    # Spaltenbeschriftungen
    screen.blit(font.render("H", True, WHITE), (MARGIN_LEFT, MARGIN_TOP + 220))
    screen.blit(font.render("M", True, WHITE), (MARGIN_LEFT + X_SPACING, MARGIN_TOP + 220))
    screen.blit(font.render("S", True, WHITE), (MARGIN_LEFT + 2 * X_SPACING, MARGIN_TOP + 220))

    # LEDs für Stunden, Minuten und Sekunden zeichnen
    draw_leds(screen, MARGIN_LEFT, MARGIN_TOP, hours)
    draw_leds(screen, MARGIN_LEFT + X_SPACING, MARGIN_TOP, minutes)
    draw_leds(screen, MARGIN_LEFT + 2 * X_SPACING, MARGIN_TOP, seconds)

    # Erklärungstext anzeigen
    explanation = font.render(
        f"Stunden: {hours}   Minuten: {minutes}   Sekunden: {seconds}", True, WHITE
    )
    screen.blit(explanation, (10, HEIGHT - 30))

    # Anzeige aktualisieren
    pygame.display.flip()

def main():
    """Hauptprogramm."""
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Uhr aktualisieren
        update_binary_clock()

        # Frame-Rate kontrollieren
        clock.tick(1)

    pygame.quit()

if __name__ == "__main__":
    main()
