import sys


# Creation de la classe Joueur
class Joueur :
    name = None
    point = 0 
    win_departement =0

# Initialisation des joueurs
def init_player():    
    player = []
    nb_player = int (input(" Quel est le nombre de joueur ? \n"))
    for i in range(0 , nb_player):
        player.append(Joueur())
        player[i].name = input(" Comment t'appelles-tu joueur "+ str(i+1)+"?\n")

    print ("--- INIT FINI ---")
    return player 

# Initialisation de la partie a jouer
def init_game():
    game_ok = 0
    while game_ok ==0:
        type_jeu = input(" A quel jeu jouons-nous ? \n\t 501 - 301 - perso \n\t horloge \n\t count \n\t departement \n\t monde \n\t cricket (N.O) \n\n\t quit \n\n help (Pour avoir l'explication des jeux) \n")
        if type_jeu == 'help' :
            fiche_help()
        elif type_jeu == 'quit' :
            in_game = 0
            game_ok = 1
        else :
            in_game = 1
            game_ok =1
    return in_game, type_jeu

# Explication de toute les regles
def fiche_help():
    print("Explcation des regles des différents jeux :\n Tout les jeux se font par jet de 3 fleches par tour \n")
    print("\n\t 501 - 301 - perso \
    \n\t\t\t  Commencer avec un nombre de point, lobjectif est d'atteindre 0 sans le dépasser \
    \n\t horloge \
    \n\t\t\t Le but est de réussir dans un même tour un maximum de points sur une valeur. \n\t\t\t On commence avec le 1 et on passe au 2 dès le tour suivant  \
    \n\t count \
    \n\t\t\t  Choisir un nombre de touret faire un maximum de points  \
    \n\t departement \
    \n\t\t\t  Le but est de choisir un numéro et d'effectuer le nombre de point correspondant \
    \n\t  monde \
    \n\t\t\t le but est de mettre une fleche dans l'ordre croissant des points \n\t\t\t le jeu commence par un 1 et fini par un centre \
    \n\t cricket \
    \n\t\t\t  En cours  \n" )
    input("press ENTER to continue..")
        
# Comptage point pour jeu undred one
def count_jet_undred_one(point_joueur):
    point_restant = point_joueur

    for j in range(1,4):
        score_fleche =0
        print (" Point restant : ", point_restant)
        score_fleche = int(input("score fleche "+ str(j)+ ":"))
        if score_fleche < 21 or score_fleche == 25 or score_fleche == 50 :
            # Gestion score
            if score_fleche < 21:
                multi = int(input("1. simple , 2.double, 3.triple ?"))  
                score_fleche = score_fleche * int(multi)
                if multi == 2 :
                    print("---       DOUBLE !!!!")
                if multi == 3 : 
                    print("---       TRIPLE !!!!")
            if score_fleche == 50 :
                print("---       BULL'S EYES !!!!")
            point_restant -= score_fleche
            if point_restant < 0 :
                print ("---       BUST retour à", point_joueur)
                point_restant = point_joueur
                break
            if point_restant == 0:  
                break
        else :
            print("---       ERROR COMPTAGE POINT _ Passage a la prochaine fleche")
    return point_restant

# Verification point undred oui
def verification_point_undred_one(player):
    if (player.point == 0):
        verif = 1
    else :
        verif = 0
    return verif

# main jeu undred one 
def undred_one_game(gamers, point_to_win):
    print("--- DEBUT DE LA PARTIE _ ", point_to_win," ---")
    nb_gamers = int(len(gamers))
    for k in range(0,nb_gamers):
        gamers[k].point = point_to_win 

    run_game = 0
    while run_game == 0:
        for i in range(0,nb_gamers):
            print("-------   "+ str(gamers[i].name)+" a toi de jouer   -------")
            gamers[i].point = count_jet_undred_one(gamers[i].point) 
            print ("Score apres jet" + str(gamers[i].point))
            win = verification_point_undred_one(gamers[i])
            if win== 1 :
                print ("---\t\t"+gamers[i].name +" a gagné")
                run_game = 1
                break

# comptage point horloge
def count_jet_horloge(name,tour):
    score_final = 0
    for j in range(1,4):
        print("Fleche: "+str(j))
        score_fleche = 0
        if tour ==21 :
            bonne_fleche = input("Avez-vous touché le centre? \n\t o \n\t n \n")
        else :
            bonne_fleche = input("Avez-vous touché le " + str(tour) + "? \n\t o \n\t n \n")
        if bonne_fleche == "o":
            if tour ==21 :
                score_fleche = 25
                multi = int(input("1. simple , 2.double ?"))       
            else :
                score_fleche = int(tour)
                multi = int(input("1. simple , 2.double, 3.triple ?"))
                if multi > 3 :
                    print("Erreur multiple, la fleche compte pour simple")
            score_final += score_fleche * int(multi)
            if multi == 2 :
                print("---       DOUBLE !!!!")
            if multi == 3 : 
                print("---       TRIPLE !!!!")
        if bonne_fleche  == "n":
            print("Dommage, vous ne marquez pas de points.")
    print ("---   "+name + " a marqué : "+str(score_final)+" points.")
    return  score_final

# main jeu horloge
def horloge_game(gamers):
    for k in range(0,int(len(gamers))): 
        gamers[k].point = 0 

    for tour in range(1,22):
        print(gamers[k].name + ", a vous!Vous avez"+ str(gamers[k].point) +"point. Vous devez cibler le : " + str(tour))
        gamers[k].point += count_jet_horloge(gamers[k].name,tour) 
        print(gamers[k].name + ", vous avez maintenant : "+str(gamers[k].point)+" points.")
    point_winner = 0
    winner = 0
    for k in range(0,int(len(gamers))): 
        print ("Parti fini :")
        print(gamers[k].name + ", vous avez : "+str(gamers[k].point)+" points.") 
        if (gamers[k].point > point_winner):
            winner = k
    print ("--- le vainqueur est : "+ str(gamers[winner].name)+ " avec : "+str(gamers[k].point))

# main jeu monde 
def monde_game(gamers):
    for k in range(0,int(len(gamers))): 
        gamers[k].point = 1
    win_game = 0 
    while win_game == 0:
        for k in range(0,int(len(gamers))):
            for j in range(1,4):
                if (gamers[k].point < 21):
                    print(gamers[k].name +", vous devez cibler  le "+str(gamers[k].point))
                else :
                    print(gamers[k].name +", vous devez cibler  le centre")
                print ("Fleche"+str(j)+" :\n" )
                if (gamers[k].point < 21):
                    result = input("Avez-vous touché le " + str(gamers[k].point)+ " ? \n\t o \n\t n \n")
                    if  result == 'o' :
                        gamers[k].point +=1
                    else : 
                        print ("Dommage !\n")
                else :
                    result = input("Avez-vous touché le centre ?\n\t o \n\t n \n")
                    if  result == 'o' :
                        print ("---BULL'EYES!")
                        print ("--- le vainqueur est : "+ str(gamers[k].name))
                        win_game =1
                        break
                    else : 
                        print ("Dommage !\n")

# Comptage point departement
def count_jet_departement():
    point_total = 0
    for j in range(1,4):
        score_fleche =0
        score_fleche = int(input("score fleche "+ str(j)+ ":"))
        if score_fleche < 21 or score_fleche == 25 or score_fleche == 50 :
            # Gestion score
            if score_fleche < 21:
                multi = int(input("1. simple , 2.double, 3.triple ?"))  
                score_fleche = score_fleche * int(multi)
                if multi == 2 :
                    print("---       DOUBLE !!!!")
                if multi == 3 : 
                    print("---       TRIPLE !!!!")
            if score_fleche == 50 :
                print("---       BULL'S EYES !!!!")
            point_total += score_fleche
        else :
            print("---       ERROR COMPTAGE POINT _ passage a la prochaine fleche")
        print ("les point total du jet", point_total)
    return point_total

# Main jeu departement
def departement_game(gamers):
    for k in range(0,int(len(gamers))): 
        gamers[k].point = 0
    nb_to_win  = input(" sur combien de point ce joue la partie ?\n")
    win = 1
    while win == 1:
        for k in range(0,int(len(gamers))):
            objectif_departement = input (gamers[k].name + " Choisez un score : \n")
            gamers[k].point = count_jet_departement()
            if int(gamers[k].point) == int(objectif_departement) : 
                gamers[k].win_departement += 1 
                if int(gamers[k].win_departement) == int(nb_to_win) :
                    print(gamers[k].name+", vous avez gagné !! ")
                    win = 0
                    break
                else  :
                    point_restant = int(int(nb_to_win) - int(gamers[k].win_departement))
                    print(gamers[k].name +", vous gagné un points vous etes à "+str(gamers[k].win_departement)+ " il vous reste "+str(point_restant)+" point a avoir.")
            else :
                print(gamers[k].name+", vous avez raté votre score. Vous ne marquez pas de points")

# Comptage jeu count
def count_jet_count():
    point_total = 0
    for j in range(1,4):
        score_fleche =0
        score_fleche = int(input("score fleche "+ str(j)+ ":"))
        if score_fleche < 21 or score_fleche == 25 or score_fleche == 50 :
            # Gestion score
            if score_fleche < 21:
                multi = int(input("1. simple , 2.double, 3.triple ?"))  
                score_fleche = score_fleche * int(multi)
                if multi == 2 :
                    print("---       DOUBLE !!!!")
                if multi == 3 : 
                    print("---       TRIPLE !!!!")
            if score_fleche == 50 :
                print("---       BULL'S EYES !!!!")
            point_total += score_fleche
        else :
            print("---       ERROR COMPTAGE POINT _ passage a la prochaine fleche")
        print ("les point total du jet", point_total)
    return point_total

# Mains jeu count
def count_game(gamers):
    for k in range(0,int(len(gamers))): 
        gamers[k].point = 0
    nb_tours = input("En combien de tours se fait la partie? \n")
    for i in range(1,int(nb_tours)):
        print(" --- TOUR "+str(i)+ " ---")
        for k in range(0,int(len(gamers))):
            print(gamers[k].name + ", a ton tour")
            gamers[k].point += count_jet_count()
            print (gamers[k].name +", vous avez "+str(gamers[k].point))
    id_winner = 0
    point_winner = 0
    for k in range(0,int(len(gamers))):
        if int(gamers[k].point) > int(point_winner):
            point_winner = int(gamers[k].point)
            id_winner = k
        print (gamers[id_winner].name+" à "+str(gamers[k].point)+" points!")
    print("Le vainqueur est : "+ gamers[id_winner].name+" avec "+str(point_winner)+" points!")

# restart
def restart():
    response = input(" Voulez vous rejouez ?\n\t oui \n\t non \n")
    if response == "oui":
        return True
    if response == "non":
        return False

gamers= init_player()
in_game = 1
while in_game == 1:
    in_game, game = init_game()
    if game == '301' or game == '501' :
        print(" ---___DEBUT D'UN ONE HUNDRED___---")
        undred_one_game(gamers, int(game))
    if game == 'perso' :
        print(" ---___DEBUT D'UN ONE HUNDRED PERSO___---")
        perso_point = input(" Sur combien de point jouons-nous ?\n")
        undred_one_game(gamers, int(perso_point))
    if game == 'horloge':
        print(" ---___DEBUT D'UNE HORLOGE___---")
        horloge_game(gamers)
    if game == 'monde':
        print(" ---___DEBUT D'UN MONDE___---")
        monde_game(gamers)
    if game == 'departement':
        print(" ---___DEBUT D'UN DEPARTEMENT___---")
        departement_game(gamers)
    if game == 'count':
        print(" ---___DEBUT D'UN COUNT___---")
        count_game(gamers)
    play = 0
    if game == 'quit':
        play == 1

    print(play)

    if play == 0 :
        test_restast = restart()
        if test_restast == True:
            in_game = 1
        else :
            in_game = 0
