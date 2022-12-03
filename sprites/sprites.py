import pygame

#different animations for coconut lady
cocolady1 = pygame.image.load('sprites\cocolady1.png')
cocolady2 = pygame.image.load('sprites\cocolady2.png')
cocolady4heart = pygame.image.load('sprites\four hearts.png')
cocolady3heart = pygame.image.load('Csprites\cocolady3heart.png')
cocolady2heart = pygame.image.load('sprites\cocolady2heart.png')
cocolady1heart = pygame.image.load('sprites\cocolady1heart.png')
cocoladydamage1 = pygame.image.load('sprites\cocoladydamage1.png')
cocoladydamage2 = pygame.image.load('sprites\cocoladydamage2.png')

#Sprites for the Gringo(which is the enemy)
gringo1 = pygame.image.load('sprites\gringo1.png')
gringo2 = pygame.image.load('sprites\gringo2.png')

#sprite for Fat Joe
joe = pygame.image.load('sprites\fatjoe.png')

coconut_lady_list = [cocolady1, cocolady2]
coconut_damage_list = [cocoladydamage1, cocoladydamage2]
gringo_list = [gringo1, gringo2]


karen = pygame.image.load('sprites\karen.png')

icon = pygame.image.load('sprites\icon.png')
background = pygame.image.load('sprites\background.png')
crab = pygame.image.load('sprites\crab.png')

all_sprites = [cocolady1, cocolady2, cocoladydamage1, cocoladydamage2, gringo1,
               gringo2, cocolady4heart, cocolady3heart, cocolady2heart, cocolady1heart,
               joe, karen, icon, background, crab]  