'''
@author: Rolgndar
@version: 1.5
@date: 22-08-2026
@Changelog:
    - 1.1 : Changement de la taille des corps célestes pour une meilleurs vissualisation.
    - 1.2 : Correction des distances entre les corps célestes.
    - 1.3 : Correction des vitesses des corps célestes.
    - 1.4 : Ajout des trajectoires de chaques corps célestes pour aider à la visualisation.
    - 1.5 : Changement des touches pour le zoom.
'''

'''
Ce code est un simulateur du système solaire.
Il permet de visualiser les orbites des planètes qui tourne autour du soleil en temps réel.
Cela est affiché avec la bibliothèque Pygame et les calculs sont soit effectués à la main où bien fait avec la bibliothèque Numpy et Poliastro.
'''

import pygame
import numpy as np

import VARIABLE_GLOBAL as VG

# --- VARIABLE GLOBALE ---
"""
Toutes les variables globale sont définis dans le fichier 'VARIABLE_GLOBAL.py' et sont importées ici.
"""

# --- SETUP PYGAME ---

def simulation():

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    VG.pause = not VG.pause

            # - DEPLACEMENT DE LA CAMERA (AXE X ET Y) -
            touches = pygame.key.get_pressed()
            if touches[pygame.K_d]:
                cam_x -= 100
            elif touches[pygame.K_q]:
                cam_x += 100
            elif touches[pygame.K_s]:
                cam_y -= 100
            elif touches[pygame.K_z]:
                cam_y += 100

            # - ZOOMER -
            if touches[pygame.K_UP]:
                zoom *= 1.1

            # - DEZOOMER -
            if touches[pygame.K_DOWN]:
                zoom /= 1.1

            # - RECENTRER -
            if touches[pygame.K_r]:
                cam_x = 0
                cam_y = 0
                zoom = 1.0

            # - PAUSE -
            if touches[pygame.K_p]:
                break

            # - QUITTER -
            if touches[pygame.K_ESCAPE]:
                running = False

        if VG.pause == True:
            continue

        ecran.fill((0, 0, 0))    # Fond noir

        # - POSITION DE LA CAMERA -
        centre_x = 640 + cam_x
        centre_y = 360 + cam_y


        # - PIVOTEMENT DES PLANETES AUTOUR DU SOLEIL -
        angle_mercure = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_MERCURE
        angle_venus = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_VENUS
        angle_terre = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_TERRE
        angle_mars = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_MARS
        angle_jupiter = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_JUPITER
        angle_saturne = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_SATURNE
        angle_uranus = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_URANUS
        angle_neptune = pygame.time.get_ticks() * VG.FACTEUR_TEMPS * VG.nv_VITESSE_NEPTUNE

        # - MISE A JOUR DES POSITIONS DES PLANETES -
        mercure_x = centre_x + VG.DISTANCE_MERCURE * zoom * np.cos(angle_mercure)
        mercure_y = centre_y + VG.DISTANCE_MERCURE * zoom * np.sin(angle_mercure)

        venus_x = centre_x + VG.DISTANCE_VENUS * zoom * np.cos(angle_venus)
        venus_y = centre_y + VG.DISTANCE_VENUS * zoom * np.sin(angle_venus)

        terre_x = centre_x + VG.DISTANCE_TERRE * zoom * np.cos(angle_terre)
        terre_y = centre_y + VG.DISTANCE_TERRE * zoom * np.sin(angle_terre)

        mars_x = centre_x + VG.DISTANCE_MARS * zoom * np.cos(angle_mars)
        mars_y = centre_y + VG.DISTANCE_MARS * zoom * np.sin(angle_mars)

        jupiter_x = centre_x + VG.DISTANCE_JUPITER * zoom * np.cos(angle_jupiter)
        jupiter_y = centre_y + VG.DISTANCE_JUPITER * zoom * np.sin(angle_jupiter)

        saturne_x = centre_x + VG.DISTANCE_SATURNE * zoom * np.cos(angle_saturne)
        saturne_y = centre_y + VG.DISTANCE_SATURNE * zoom * np.sin(angle_saturne)

        uranus_x = centre_x + VG.DISTANCE_URANUS * zoom * np.cos(angle_uranus)
        uranus_y = centre_y + VG.DISTANCE_URANUS * zoom * np.sin(angle_uranus)

        neptune_x = centre_x + VG.DISTANCE_NEPTUNE * zoom * np.cos(angle_neptune)
        neptune_y = centre_y + VG.DISTANCE_NEPTUNE * zoom * np.sin(angle_neptune)


        # - DESSINS DES TRAJECTOIRES DES CORPS CELESTES -
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_MERCURE * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_VENUS * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_TERRE * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_MARS * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_JUPITER * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_SATURNE * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_URANUS * zoom, 1, False, False, False, False)
        pygame.draw.circle(ecran, VG.white, (centre_x, centre_y), VG.DISTANCE_NEPTUNE * zoom, 1, False, False, False, False)

        # - DESSINS DES CORPS CELESTES -
        pygame.draw.circle(ecran, VG.COLOR_SOLEIL, (centre_x, centre_y), VG.TAILLE_SOLEIL * zoom)  # Dessine le Soleil
        pygame.draw.circle(ecran, VG.COLOR_MERCURE, (mercure_x, mercure_y), VG.TAILLE_MERCURE * zoom)  # Dessine Mercure
        pygame.draw.circle(ecran, VG.COLOR_VENUS, (venus_x, venus_y), VG.TAILLE_VENUS * zoom)  # Dessine Venus
        pygame.draw.circle(ecran, VG.COLOR_TERRE, (terre_x, terre_y), VG.TAILLE_TERRE * zoom)  # Dessine la Terre
        pygame.draw.circle(ecran, VG.COLOR_MARS, (mars_x, mars_y), VG.TAILLE_MARS * zoom)  # Dessine Mars
        pygame.draw.circle(ecran, VG.COLOR_JUPITER, (jupiter_x, jupiter_y), VG.TAILLE_JUPITER * zoom) # Dessine Jupiter
        pygame.draw.circle(ecran, VG.COLOR_SATURNE, (saturne_x, saturne_y), VG.TAILLE_SATURNE * zoom) # Dessine Saturne
        pygame.draw.circle(ecran, VG.COLOR_URANUS, (uranus_x, uranus_y), VG.TAILLE_URANUS * zoom) # Dessine Uranus
        pygame.draw.circle(ecran, VG.COLOR_NEPTUNE, (neptune_x, neptune_y), VG.TAILLE_NEPTUNE * zoom) # Dessine Neptune

        # - DESSINS DES LIGNES DES TRAJECTOIRES -
        

        pygame.display.flip()
        clock.tick(60)           # Limite à 60 FPS

    pygame.quit()


if __name__ == "__main__":
    simulation()
