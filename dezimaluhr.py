import pygame
import time
from datetime import datetime

# Initialisieren von Pygame
pygame.init()

# Bildschirmgröße und Hintergrundfarbe
WIDTH, HEIGHT = 100, 460
BACKGROUND_COLOR = (18, 18, 18)  # Dunkelgrau
LED_OFF_COLOR = (128, 128, 128)  # Grau
LED_ON_COLOR = (50, 205, 50)     # Limegrün

# LED-Einstellungen
LED_RADIUS = 4
LED_SPACING = 10

# Erstellen eines Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dezimaluhr")

# Funktion zum Zeichnen einer LED (aktiviert/deaktiviert)
def draw_led(x, y, active, color=LED_ON_COLOR):
    pygame.draw.circle(screen, color if active else LED_OFF_COLOR, (x, y), LED_RADIUS)

# Funktion zum Zeichnen einer blinkenden LED
def draw_blinking_led(x, y, blink):
    color = BLINK_COLOR if blink else BACKGROUND_COLOR
    pygame.draw.circle(screen, color, (x, y), LED_RADIUS)

# Funktion zum Aktualisieren der LEDs für eine Zifferngruppe
def update_leds(x, y_start, count, value):
    for i in range(count):
        draw_led(x, y_start + i * LED_SPACING, i < value)

# Hauptschleife der Uhr
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # Event-Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Bildschirm aktualisieren
        screen.fill(BACKGROUND_COLOR)

        # Aktuelle Uhrzeit abrufen
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second

        # Stunden-LEDs zeichnen
        update_leds(50, 20, 2, hours // 10)  # Zehnerstellen der Stunden
        update_leds(50, 50, 9, hours % 10)  # Einerstellen der Stunden

        # Minuten-LEDs zeichnen
        update_leds(50, 150, 5, minutes // 10)  # Zehnerstellen der Minuten
        update_leds(50, 210, 9, minutes % 10)  # Einerstellen der Minuten

        # Sekunden-LEDs zeichnen
        update_leds(50, 310, 5, seconds // 10)  # Zehnerstellen der Sekunden
        update_leds(50, 370, 9, seconds % 10)  # Einerstellen der Sekunden

        # Anzeige aktualisieren
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

# Hauptfunktion starten
if __name__ == "__main__":
    main()
