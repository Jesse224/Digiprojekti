import math
import sys
import pygame

# Alustetaan Pygame
pygame.init()
pygame.font.init()

# Ruudun asetukset
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RTS Prototyyppi - Valinnan poisto ESC:llä")
clock = pygame.time.Clock()

# Fontti resurssien näyttämiseen
font = pygame.font.SysFont(None, 28)

# Värit
BG_COLOR = (30, 30, 35)
UNIT_COLOR = (70, 130, 180)
SELECTED_COLOR = (255, 215, 0)
TARGET_COLOR = (220, 20, 60)
MINERAL_COLOR = (0, 200, 150)
TEXT_COLOR = (240, 240, 240)


# Resurssiluokka (Mineraali)
class Mineral:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 12
        self.amount = 50


# Unitti-luokka
class Unit:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.radius = 20
        self.speed = 220
        self.is_selected = False
        self.target_x = self.x
        self.target_y = self.y

    def update(self, dt, minerals):
        # Lasketaan etäisyys liikkumiskohteeseen
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.hypot(dx, dy)

        # Liikkuminen kohteeseen
        if distance > 2:
            move_distance = self.speed * dt
            if move_distance >= distance:
                self.x = self.target_x
                self.y = self.target_y
            else:
                self.x += (dx / distance) * move_distance
                self.y += (dy / distance) * move_distance

        # Tarkistetaan törmäys mineraaleihin
        global player_minerals
        for m in minerals[:]:
            if math.hypot(self.x - m.x, self.y - m.y) <= self.radius + m.radius:
                minerals.remove(m)
                player_minerals += m.amount

    def draw(self, surface):
        # Piirretään kohdemerkki vain, jos unitti on valittuna ja liikkuu
        if self.is_selected and math.hypot(self.target_x - self.x, self.target_y - self.y) > 2:
            pygame.draw.circle(
                surface, TARGET_COLOR, (int(self.target_x), int(self.target_y)), 5
            )

        # Piirretään valintarengas
        if self.is_selected:
            pygame.draw.circle(
                surface,
                SELECTED_COLOR,
                (int(self.x), int(self.y)),
                self.radius + 4,
                2,
            )

        # Piirretään unitti
        pygame.draw.circle(
            surface, UNIT_COLOR, (int(self.x), int(self.y)), self.radius
        )


# Peliin liittyvät muuttujat
player_minerals = 0
unit = Unit(WIDTH // 4, HEIGHT // 2)

# Luodaan mineraaleja kentälle
minerals = [
    Mineral(400, 200),
    Mineral(550, 150),
    Mineral(600, 400),
    Mineral(500, 300),
    Mineral(350, 450)
]

# Pelisilmukka
running = True
while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Kuunnellaan näppäimistön painalluksia
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Jos painetaan ESC, poistetaan valinta ja pysäytetään liike nykyiseen sijaintiin
                if unit.is_selected:
                    unit.is_selected = False
                    unit.target_x = unit.x
                    unit.target_y = unit.y

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Vasen hiiren painike
            if event.button == 1:
                dist_to_unit = math.hypot(mouse_pos[0] - unit.x, mouse_pos[1] - unit.y)
                if dist_to_unit <= unit.radius:
                    unit.is_selected = True
                else:
                    if unit.is_selected:
                        unit.target_x, unit.target_y = mouse_pos
                    else:
                        unit.is_selected = False

            # Oikea hiiren painike liikkumiseen
            elif event.button == 3 and unit.is_selected:
                unit.target_x, unit.target_y = mouse_pos

    # Päivitetään pelilogiikka
    unit.update(dt, minerals)

    # Piirretään näkymä
    screen.fill(BG_COLOR)

    # Piirretään mineraalit
    for m in minerals:
        pygame.draw.circle(screen, MINERAL_COLOR, (m.x, m.y), m.radius)
        pygame.draw.circle(screen, (255, 255, 255), (m.x - 3, m.y - 3), 3)

    # Piirretään unitti
    unit.draw(screen)

    # Piirretään käyttöliittymä (Resurssilaskuri yläkulmaan)
    score_text = font.render(f"Mineraalit: {player_minerals}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()