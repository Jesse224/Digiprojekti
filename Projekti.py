import math
import sys
import pygame

# Alustetaan Pygame
pygame.init()

# Ruudun asetukset
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RTS Prototyyppi - Yksikön liikkuminen")
clock = pygame.time.Clock()

# Värit
BG_COLOR = (30, 30, 35)
UNIT_COLOR = (70, 130, 180)
SELECTED_COLOR = (255, 215, 0)
TARGET_COLOR = (220, 20, 60)

# Unitti-luokka
class Unit:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.radius = 20
        self.speed = 250  # pikseliä sekunnissa
        self.is_selected = False
        self.target_x = self.x
        self.target_y = self.y

    def update(self, dt):
        # Lasketaan etäisyys kohteeseen
        dx = self.target_x - self.x
        dy = self.target_y - self.y
        distance = math.hypot(dx, dy)

        # Jos ollaan kaukana kohteesta, liikutetaan unittia sitä kohti
        if distance > 2:
            move_distance = self.speed * dt
            if move_distance >= distance:
                self.x = self.target_x
                self.y = self.target_y
            else:
                self.x += (dx / distance) * move_distance
                self.y += (dy / distance) * move_distance

    def draw(self, surface):
        # Piirretään kohdemerkki, jos unitti on matkalla
        if math.hypot(self.target_x - self.x, self.target_y - self.y) > 2:
            pygame.draw.circle(
                surface, TARGET_COLOR, (int(self.target_x), int(self.target_y)), 5
            )

        # Piirretään valintarengas, jos unitti on valittuna
        if self.is_selected:
            pygame.draw.circle(
                surface,
                SELECTED_COLOR,
                (int(self.x), int(self.y)),
                self.radius + 4,
                2,
            )

        # Piirretään itse unitti
        pygame.draw.circle(
            surface, UNIT_COLOR, (int(self.x), int(self.y)), self.radius
        )


# Luodaan yksi unitti ruudun keskelle
unit = Unit(WIDTH // 2, HEIGHT // 2)

# Pelisilmukka
running = True
while running:
    # DT (Delta Time) varmistaa, että liike on yhtä nopeaa ruudunpäivitysnopeudesta riippumatta
    dt = clock.tick(60) / 1000.0

    # Tapahtumien käsittely
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Vasen hiiren painike
            if event.button == 1:
                # Tarkistetaan, klikattiinko unittia
                dist_to_unit = math.hypot(
                    mouse_pos[0] - unit.x, mouse_pos[1] - unit.y
                )

                if dist_to_unit <= unit.radius:
                    unit.is_selected = True
                else:
                    # Jos unitti oli jo valittuna, uusi klikkaus asettaa kohdepisteen
                    if unit.is_selected:
                        unit.target_x, unit.target_y = mouse_pos
                    else:
                        unit.is_selected = False

            # Oikea hiiren painike (vaihtoehtoinen tapa liikkua RTS-tyyliin)
            elif event.button == 3 and unit.is_selected:
                unit.target_x, unit.target_y = mouse_pos

    # Päivitetään pelilogiikka
    unit.update(dt)

    # Piirretään ruutu
    screen.fill(BG_COLOR)
    unit.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()