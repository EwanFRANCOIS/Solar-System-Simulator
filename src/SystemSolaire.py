'''
@author: Rolgndar
@version: 1.2
@date: 09-08-2026
@Changelog:
    - 1.1 : Changement de la taille des corps célestes pour une meilleurs vissualisation.
    - 1.2 : Ajout des mouvements circulaire des corps célestes (leurs placement ne sont pas réaliste, sera amélioré dans la prochaine version)

'''

'''
Ce code est un simulateur du système solaire.
Il permet de visualiser les orbites des planètes qui tourne autour du soleil en temps réel.
Cela est affiché avec la bibliothèque Pygame et les calculs sont soit effectués à la main où bien fait avec la bibliothèque Numpy et Poliastro.
'''

import pygame
import numpy as np
import poliastro

from poliastro.bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn

# --- VARIABLE GLOBALE ---
"""
Ici sont définies toutes les variables nécessaire pour le bon fonctionnement du simulateur du système solaire.
La plupart des valeurs sont les valeurs réelles des corps célestes, en raison des performances de pygame ainsi que de la visualisation,
j'ai réduit les tailles pour que l'affichage soit plus agréable à l'oeil.
"""


G = 6.67430 * 10**-11  # Constante gravitationnelle

# - MASSES DES PLANETES (en kg) -
MASSE_SOLEIL = 1.989 * 10**30         # Masse du Soleil
MASSE_MERCURE = 3.3 * 10**23          # Masse de Mercure
MASSE_VENUS = 4.87 * 10**24           # Masse de Venus
MASSE_TERRE = 5.972 * 10**24          # Masse de la Terre
MASSE_MARS = 6.42 * 10**23            # Masse de Mars
MASSE_JUPITER = 1.9 * 10**27          # Masse de Jupiter
MASSE_SATURNE = 5.684 * 10**26        # Masse de Saturne
MASSE_URANUS = 8.681 * 10**25         # Masse d'Uranus
MASSE_NEPTUNE = 1.024 * 10**26        # Masse de Neptune

# - COULEURS DES PLANETES (en RGB) -
COLOR_SOLEIL = (255, 255, 0)          # Couleur du Soleil
COLOR_MERCURE = (169, 169, 169)       # Couleur de Mercure
COLOR_VENUS = (255, 165, 0)           # Couleur de Venus
COLOR_TERRE = (0, 0, 255)             # Couleur de la Terre
COLOR_MARS = (255, 0, 0)              # Couleur de Mars
COLOR_JUPITER = (255, 140, 0)         # Couleur de Jupiter
COLOR_SATURNE = (210, 180, 140)       # Couleur de Saturne
COLOR_URANUS = (0, 255, 255)          # Couleur d'Uranus
COLOR_NEPTUNE = (0, 0, 139)           # Couleur de Neptune

# - DIAMETRES DES PLANETES (en km) -
DIAMETRE_SOLEIL = 1392000
DIAMETRE_MERCURE = 4879
DIAMETRE_VENUS = 12104
DIAMETRE_TERRE = 12742
DIAMETRE_MARS = 6794
DIAMETRE_MOYEN_JUPITER = 141403
DIAMETRE_MOYEN_SATURNE = 116464
DIAMETRE_MOYEN_URANUS = 51118
DIAMETRE_MOYEN_NEPTUNE = 49528

# - DISTANCES DES PLANETES AU SOLEIL (en km converties en pixels) -
DISTANCE_MERCURE = 58
DISTANCE_VENUS = 108
DISTANCE_TERRE = 150
DISTANCE_MARS = 228
DISTANCE_JUPITER = 778
DISTANCE_SATURNE = 1427
DISTANCE_URANUS = 2871
DISTANCE_NEPTUNE = 4495


# - VITESSES DES PLANETES (en km/s) -
VITESSE_MERCURE = 47.36
VITESSE_VENUS = 35.02
VITESSE_TERRE = 29.78
VITESSE_MARS = 24.077
VITESSE_JUPITER = 13.07
VITESSE_SATURNE = 9.69
VITESSE_URANUS = 6.81
VITESSE_NEPTUNE = 5.43

# - REDEF DES TAILLES (EN PIXELS) -
TAILLE_SOLEIL = 100
TAILLE_MERCURE = 10
TAILLE_VENUS = 12
TAILLE_TERRE = 13
TAILLE_MARS = 11
TAILLE_JUPITER = 20
TAILLE_SATURNE = 18
TAILLE_URANUS = 16
TAILLE_NEPTUNE = 15


# --- SETUP PYGAME ---

def simulation():

    """"
    echelle_taille_init = 1 / 700          # Echelle pour réduire la taille des corps célestes
    echelle_distance_init = 1 / 9000      # Echelle pour réduire les distances entre les corps célestes  
    """

    pygame.init()
    ecran = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    zoom = 1.0

    cam_x = 0
    cam_y = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    zoom *= 1.1  # Zoom avant
                    
                elif event.y < 0:
                    zoom /= 1.1  # Zoom arrière
                    

            # - DEPLACEMENT DE LA CAMERA (AXE X ET Y) -
            touches = pygame.key.get_pressed()
            if touches[pygame.K_q]:
                cam_x -= 100
            elif touches[pygame.K_d]:
                cam_x += 100
            elif touches[pygame.K_z]:
                cam_y -= 100
            elif touches[pygame.K_s]:
                cam_y += 100

            # - RECENTRER -
            if touches[pygame.K_r]:
                cam_x = 0
                cam_y = 0
                zoom = 1.0

        ecran.fill((0, 0, 0))    # Fond noir

        # - POSITION DE LA CAMERA -
        centre_x = 640 + cam_x
        centre_y = 360 + cam_y


        # - PIVOTEMENT DES PLANETES AUTOUR DU SOLEIL -
        angle_mercure = pygame.time.get_ticks() * 0.0001 * VITESSE_MERCURE
        angle_venus = pygame.time.get_ticks() * 0.0001 * VITESSE_VENUS
        angle_terre = pygame.time.get_ticks() * 0.0001 * VITESSE_TERRE
        angle_mars = pygame.time.get_ticks() * 0.0001 * VITESSE_MARS
        angle_jupiter = pygame.time.get_ticks() * 0.0001 * VITESSE_JUPITER
        angle_saturne = pygame.time.get_ticks() * 0.0001 * VITESSE_SATURNE
        angle_uranus = pygame.time.get_ticks() * 0.0001 * VITESSE_URANUS
        angle_neptune = pygame.time.get_ticks() * 0.0001 * VITESSE_NEPTUNE

        # - MISE A JOUR DES POSITIONS DES PLANETES -
        mercure_x = centre_x + DISTANCE_MERCURE * zoom * np.cos(angle_mercure)
        mercure_y = centre_y + DISTANCE_MERCURE * zoom * np.sin(angle_mercure)

        venus_x = centre_x + DISTANCE_VENUS * zoom * np.cos(angle_venus)
        venus_y = centre_y + DISTANCE_VENUS * zoom * np.sin(angle_venus)

        terre_x = centre_x + DISTANCE_TERRE * zoom * np.cos(angle_terre)
        terre_y = centre_y + DISTANCE_TERRE * zoom * np.sin(angle_terre)

        mars_x = centre_x + DISTANCE_MARS * zoom * np.cos(angle_mars)
        mars_y = centre_y + DISTANCE_MARS * zoom * np.sin(angle_mars)

        jupiter_x = centre_x + DISTANCE_JUPITER * zoom * np.cos(angle_jupiter)
        jupiter_y = centre_y + DISTANCE_JUPITER * zoom * np.sin(angle_jupiter)

        saturne_x = centre_x + DISTANCE_SATURNE * zoom * np.cos(angle_saturne)
        saturne_y = centre_y + DISTANCE_SATURNE * zoom * np.sin(angle_saturne)

        uranus_x = centre_x + DISTANCE_URANUS * zoom * np.cos(angle_uranus)
        uranus_y = centre_y + DISTANCE_URANUS * zoom * np.sin(angle_uranus)

        neptune_x = centre_x + DISTANCE_NEPTUNE * zoom * np.cos(angle_neptune)
        neptune_y = centre_y + DISTANCE_NEPTUNE * zoom * np.sin(angle_neptune)


        # - DESSINS DES CORPS CELESTES -
        pygame.draw.circle(ecran, COLOR_SOLEIL, (centre_x, centre_y), TAILLE_SOLEIL * zoom)  # Dessine le Soleil
        pygame.draw.circle(ecran, COLOR_MERCURE, (mercure_x, mercure_y), TAILLE_MERCURE * zoom)  # Dessine Mercure
        pygame.draw.circle(ecran, COLOR_VENUS, (venus_x, venus_y), TAILLE_VENUS * zoom)  # Dessine Venus
        pygame.draw.circle(ecran, COLOR_TERRE, (terre_x, terre_y), TAILLE_TERRE * zoom)  # Dessine la Terre
        pygame.draw.circle(ecran, COLOR_MARS, (mars_x, mars_y), TAILLE_MARS * zoom)  # Dessine Mars
        pygame.draw.circle(ecran, COLOR_JUPITER, (jupiter_x, jupiter_y), TAILLE_JUPITER * zoom) # Dessine Jupiter
        pygame.draw.circle(ecran, COLOR_SATURNE, (saturne_x, saturne_y), TAILLE_SATURNE * zoom) # Dessine Saturne
        pygame.draw.circle(ecran, COLOR_URANUS, (uranus_x, uranus_y), TAILLE_URANUS * zoom) # Dessine Uranus
        pygame.draw.circle(ecran, COLOR_NEPTUNE, (neptune_x, neptune_y), TAILLE_NEPTUNE * zoom) # Dessine Neptune

        pygame.display.flip()
        clock.tick(60)           # Limite à 60 FPS

    pygame.quit()


if __name__ == "__main__":
    simulation()
