# Simulation_Banc_poisson

Réalisation D'une simulation pour modéliser un mouvement aléatoire d'un groupe de poisson : 


## Descritpion du projet
Jusqu’à il y a peu, plusieurs études s’intérèssent de plus en plus à la
modélisation des systèmes complexes ,à savoir les bancs de poissons appelés
aussi Boïds .Ce système est constitué d’un grand nombre d’individus dont les
interactions engendrent des dynamiques collectives complexes. Ainsi, pour
étudier leurs mouvements, les scientifiques ont utilisé une approche
pluridisciplinaire combinant à la fois mathématiques appliquées et physique
statistique, ce qui se manifeste par la diversité des modèles abordés dans notre
étude.

Ces modèles ont prouvé qu'il n'est pas nécessaire qu'un chef dirige les autres
poissons dans quelle direction ils doivent nager et à quelle vitesse. Chaque
individu reconnait cela par lui-même, uniquement en observant ses voisins les
plus proches et en ajustant sa réaction à la leur. Il permet alors d’étudier cette
complexité, en simulant des individus virtuels ayant entre eux des règles
d’interactions locales simples. Ces règles fondamentales, proposées par Mr.
Craig Reynolds [1], sont de trois types : répulsion, alignement et attraction. Ce
modèle postule, d’après le travail de Mr. Mirabet Vincent [2], que l’influence de
ces règles se manifeste en trois zones concentriques autour d’un individu. La
présence d’autres poissons dans chacune de ces zones détermine les
comportements de cet individu. La première, qui se situe dans l’environnement
direct du poisson, est la zone de répulsion : lorsque des congénères y
pénètrent, l’individu s’en éloigne en changeant de direction. La deuxième est la
zone d’alignement. Elle tire son nom du fait que le poisson s’aligne avec la
direction moyenne suivie par tous les poissons qui se trouvent dans cette zone.
Enfin, la dernière, et la plus éloignée, est la zone d’attraction. L’individu se dirige
en effet vers la position moyenne occupée par les poissons. On peut meme
parler de la notion de Flocking , un phénomène au cours duquel le groupe des
poissons s’organise pour former un ensemble ayant un mouvement
globalement cohérent et une direction centralisée .

Au début, on s’intéressera au modèle individu-centré (IBM) basé
essentiellement sur des notions de la Physique statistique. Afin de préparer la
solution numérique de notre problème, nous devons d’abord discrétiser les
équations de mouvements proposées par Mr. Letuvee et Mr. Rohmer [3]. Après,
pour atteindre notre modèle final, on utilisera plusieurs tests sur des modèles
intermédiaires. Ainsi on va s’intéresser au début à l’étude de mouvements de
deux poissons et leurs interactions (modèle simple), et à chaque fois on
essayera de modifier ou ajouter des paramètres nécessaires influençant sur le
mouvement pour garantir sa convergence en s’inspirant de [2] afin de respecter
les règles citées par [1] et obtenir ainsi un modèle plus réaliste. Puis on va
généraliser notre simulation pour N Boïds.

Ensuite, on étudiera deux modèles mathématiques qui décrivent chaque
poisson étudiée de la manière suivante : Un individu i ∈ {1,......N} décrit
comme une particule massique, située au temps t ⩾ 0 à la position (xi,yi) et se
déplaçant à la vitesse (Vxi,Vyi). Le premier est basé sur le travail de Mr.
Alexandre Rotolo & Mr. Maydine Ghestin [4] qui ont proposé le modèle de
Champ Moyen (MFM), ce dernier propose un système d’équations de
mouvements qu’on va discrétiser et le simuler selon des cas en modifiant les
paramètres de répulsion et d’attraction. Ce modèle respecte seulement la loi de
répulsion et d’attraction de [1]. Le deuxième modèle de Cucker-Smale (CSM)
proposé par Mr. Felipe Cucker & Steve Smale [5] va s’intéresser au contraire du
(MFM) sur l’alignement des poissons en utilisant aussi un système d’équation
de mouvement dépendant d’un paramètre influant sur la vitesse de
convergence. Donc afin de respecter les trois règles de [1] on va combiner ces
deux approches en un Modèle Mixte (MM). Chaque modèle présenté sera
accompagné d’une simulation 3D.
A ce stade, on a pu réaliser un modèle physique (IBM) et un modèle
Mathématique (MM), il reste enfin de les comparer à la visualisation direct du
phénomène et pouvoir ainsi jugé celui qui est le plus réaliste.


.
