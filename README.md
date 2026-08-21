# Solar System Simulator
 
Un simulateur réaliste de notre Système Solaire avec plusieurs fonctionnalités en plus de certaines options configurables pour tester divers évènements.
 
## /!\ CRÉATION EN COURS /!\
 
Le simulateur est pour le moment en cours de création, j'essaye de l'avancer le plus vite possible pour que la "première" vraie version sorte. En attendant, vous aurez juste son évolution au cours du temps. Sachez également que le `README` évoluera également avec le projet.
 
Le code en lui même n'est peut être pas optimisé. Je compte essayer de l'optimiser aussi à l'avenir même si mes talents dans l'optimisation sont plutôt mauvaise, je suis donc pas contre des aides pour cela ^^
 
## Contexte
 
Depuis mon plus jeune âge, j'ai toujours été passionné par l'espace et ses divers événements spectaculaires, mais aussi par l'informatique (deux sujets complètement différents). Lorsque j'ai commencé à apprendre le Python, je me suis dit qu'il serait plutôt sympa de faire un simulateur réaliste. Cela demande beaucoup de temps mais aussi beaucoup de connaissances ainsi que de théories.
 
## Projet
 
Le projet est donc un `.py` qui peut être directement lancé via Visual Studio ou bien via un terminal. Comme indiqué au-dessus, le projet est pour le moment en cours de création tout comme ce `README` et je continue d'avancer dessus. Ce dépôt évoluera donc avec le projet ^^
 
## Comment la simulation fonctionne ?
 
On passe aux choses sérieuses !
 
Pour le moment, le simulateur comporte juste les planètes qui tournent autour du soleil, leurs vitesses ne sont en aucun cas réalistes tout comme leurs distances (les corps célestes sont quand même bien éloignés les uns des autres)

### L’installation :

Vous avez d'abord besoin d'avoir sur votre ordinateur la dernière version de python installé voici le lien pour l'installation de python :

https://www.python.org/downloads/

La simulation utilise les bibliothèques numpy et pygame. Ci-dessous sont présente les commandes à copier coller dans un Terminal / CMD pour faire tourner le simulateur sans problème.

numpy (Windows) :
`pip install numpy`

numpy (MacOS / Linux) :
`pip3 install numpy`

pygame (Windows) :
`pip install pygame`

pygame (MacOS / Linux) :
`pip3 install pygame`

Si pip n'est pas reconnu ou que la commande entrée vous marque une erreur, entrez ceci à la place :

numpy :
`python -m pip install numpy`
pygame :
`python -m pip install pygame` 
 
### Les commandes :
 
- `Z/Q/S/D` : contrôles de la caméra et se déplacer (celle-ci est un peu sensible et vous pouvez très vite voler loin, elle sera améliorée à l'avenir).
 
- `SCROLL` : zoomer ou dézoomer sur l'écran.
 
- `R` : réinitialiser la position et le zoom.
 
D'autres commandes arriveront dans les versions à venir.
