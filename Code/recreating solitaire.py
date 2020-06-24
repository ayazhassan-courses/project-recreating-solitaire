import pygame
pygame.init()
screen = pygame.display.set_mode((800,600)) #creating the surface on which objects can be manipulated
green = [0,130,0]
transparent=(0, 0, 0, 0)
screen.fill(green)
pygame.display.set_caption('Solitaire')
clock = pygame.time.Clock() #checks the frames per second
#_____________________________________________________________________________________________________________________________________
def pop(lst):
    if len(lst)== 0:
        pass
    else:
        return(lst.pop())

def push(lst,item):
    lst.append(item)

def back_to_random1(random_deck2): #push the elements back into random deck to pop again
    while len(random_deck2)!=0:
        element = pop(random_deck2)
        push(random_deck,element)

def check_random(card1): #deck value
    if card1 ==' ': #if no deck value given
        val1 = random_deck2[-1] #last value of random deck2
        return(val1)

def check_next_one(val, val1, length):   #THIS CODE WILL FIND OUT IF THE PARTICULAR CARD CAN BE PLACED OVER 
                                        # THE OTHER CARD
    if 'king' in val1:
        if length == 0:
            return(True)
    if 'queen' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if 'king' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if 'king' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if 'jack' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if 'queen' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if 'queen' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '10' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if 'jack' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if 'jack' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '9' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if '10' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if '10' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '8' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if '9' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if '9' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '7' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if '8' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if '8' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '6' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if '7' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if '7' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '5' in val1:
        if 'diamonds' in val1  or 'hearts'in val1:
            if '6' in val and ('clubs' in val or 'spades' in val):
                return(True)
        if 'clubs' in val1 or 'spades' in val1:
            if '6' in val and ('diamonds' in val or 'hearts' in val):
                return(True)
    if '4' in val1 :
        if 'diamonds' in val1  or 'hearts'in val1 :
            if '5' in val and ('clubs' in val or 'spades' in val) :
                return(True)
        if 'clubs' in val1 or 'spades' in val1 :
            if '5' in val and ('diamonds' in val or 'hearts' in val) :
                return(True)
    if '3' in val1 :
        if 'diamonds' in val1  or 'hearts'in val1 :
            if '4' in val and ('clubs' in val or 'spades' in val) :
                return(True)
        if 'clubs' in val1 or 'spades' in val1 :
            if '4' in val and ('diamonds' in val or 'hearts' in val) :
                return(True)
    if '2' in val1 :
        if 'diamonds' in val1  or 'hearts'in val1 :
            if '3' in val and ('clubs' in val or 'spades' in val) :
                return(True)
        if 'clubs' in val1 or 'spades' in val1 :
            if '3' in val and ('diamonds' in val or 'hearts' in val) :
                return(True)
    if 'ace' in val1 :
        if 'diamonds' in val1  or 'hearts'in val1 :
            if '2' in val and ('clubs' in val or 'spades' in val) :
                return(True)
        if 'clubs' in val1 or 'spades' in val1 :
            if '2' in val and ('diamonds' in val or 'hearts' in val) :
                return(True)
    else :
        return(False)


def check_next_card(final_deck, initial_deck) :   # THIS WILL CALL THE ABOVE FUNCTION. (card, card1)
    if initial_deck ==' ': #if there is no deck value - random-deck
        val1 = check_random(initial_deck)
    else: #if there is a deck value
        val1 = initial_deck[-1] #deck2's last card
    val = final_deck[-1] #deck1's last card
    length = len(final_deck) #length of the deck

    return(check_next_one(val, val1, length)) #checks the alternating colors and values of card1 and card2 


def mouse_P(mouse_position): ###  THIS FUNCTION WILL FIND THE COORDINATES OF CARD WHEN MOUSEBUTTON IS CLICKED
    if 30<= mouse_position[0] <=101:  #DECK1, x-value
        if 10<=mouse_position[1]<=196: #y-value
            return('hidden')
        length_of_deck=len(deck1)-1
        val = 150+30*length_of_deck  #this gives the y-value of the last card on the deck which is shown
        tup = (30,val,deck1) #(x,y,deck)
        return(tup)
    elif 130<= mouse_position[0] <=201: #DECK2, x-value
        if 10<=mouse_position[1]<=196: #y-value
            tup = (130,10,' ')
            return(tup)
        else:
            length_of_deck=len(deck2)-1 
            val = 150+30*length_of_deck #this gives the y-value of the last card on the deck which is shown
            tup = (130,val,deck2)
            return(tup)
    elif 230<= mouse_position[0] <301: #DECK3
        length_of_deck=len(deck3)-1
        val = 150+30*length_of_deck #this gives the y-value of the last card on the deck which is shown
        tup = (230,val,deck3)
        return(tup)
    elif 330<= mouse_position[0] <=401: #DECK4
        length_of_deck=len(deck4)-1
        val = 150+30*length_of_deck #this gives the y-value of the last card on the deck which is shown
        tup = (330,val,deck4)
        return(tup)
    elif 430<= mouse_position[0] <=501: #DECK5
        length_of_deck=len(deck5)-1
        val = 150+30*length_of_deck #this gives the y-value of the last card on the deck which is shown
        tup = (430,val,deck5)
        return(tup)
    elif 530<= mouse_position[0] <=601: #DECK6
        length_of_deck=len(deck6)-1
        val = 150+30*length_of_deck #this gives the y-value of the last card on the deck which is shown
        tup = (530,val,deck6)
        return(tup)
    elif 630<= mouse_position[0] <=701: #DECK7
        length_of_deck=len(deck7)-1
        val = 150+30*length_of_deck #this gives the y-value of the last card on the deck which is shown
        tup = (630,val,deck7)
        return(tup)
    else :
        return(False)


def rect_position(rectangle_x):   ## THIS FUNCTION WILL FIND THE COORDINATES OF CARD WHERE MOUSE BUTTON IS RELEASED
    if 30<= rectangle_x <=101 :
        length_of_deck=len(deck1)
        val=150+30*length_of_deck
        tup=(30,val, deck1) #DECK1
        return(tup)
    elif 130<= rectangle_x <=201:
        length_of_deck=len(deck2)
        val=150+30*length_of_deck
        tup=(130,val, deck2) #DECK2
        return(tup)

    elif 230<= rectangle_x <301:
        length_of_deck=len(deck3)
        val=150+30*length_of_deck
        tup=(230,val, deck3) #DECK3
        return(tup)
    elif 330<= rectangle_x <=401:
        length_of_deck=len(deck4)
        val=150+30*length_of_deck
        tup=(330,val, deck4) #DECK4
        return(tup)
    elif 430<= rectangle_x <=501:
        length_of_deck=len(deck5)
        val=150+30*length_of_deck
        tup=(430,val, deck5) #DECK5
        return(tup)
    elif 530<= rectangle_x <=601:
        length_of_deck=len(deck6)
        val=150+30*length_of_deck
        tup=(530,val, deck6) #DECK6
        return(tup)
    elif 630<= rectangle_x <=701:
        length_of_deck=len(deck7)
        val=150+30*length_of_deck
        tup=(630,val, deck7) #DECK7
        #tup = (x,y,deck)
        return(tup)
    else :
        return(False)


def rect_position2(rectangle_x2):
    if 330 <= rectangle_x2 <= 401:
        tup = (330,10, box_1)
        return tup

    if 430 <= rectangle_x2 <= 501:
        tup = (430, 10, box_2)
        return tup
    
    if 530 <= rectangle_x2 <= 601:
        tup = (530, 10, box_3)
        return tup

    if 630 <= rectangle_x2 <= 701:
        tup = (630, 10, box_4)
        return tup
    else:
        return False


# pygame.display.update()
#__________________________________________________________________________________________________________________________________
#MAKE A DICTIONARY
cards = {}

cards['ace_clubs'] = pygame.image.load("ace_clubs.png")
cards['ace_spades'] = pygame.image.load("ace_spades.png")
cards['ace_hearts'] = pygame.image.load("ace_hearts.png")
cards['ace_diamonds'] = pygame.image.load("ace_diamonds.png")

cards['king_clubs'] = pygame.image.load("king_clubs.png")
cards['king_spades'] = pygame.image.load("king_spades.png")
cards['king_hearts'] = pygame.image.load("king_hearts.png")
cards['king_diamonds'] = pygame.image.load("king_diamonds.png")

cards['queen_clubs'] = pygame.image.load("queen_clubs.png")
cards['queen_spades'] = pygame.image.load("queen_spades.png")
cards['queen_hearts'] = pygame.image.load("queen_hearts.png")
cards['queen_diamonds'] = pygame.image.load("queen_diamonds.png")

cards['jack_clubs'] = pygame.image.load("jack_clubs.png")
cards['jack_spades'] = pygame.image.load("jack_spades.png")
cards['jack_hearts'] = pygame.image.load("jack_hearts.png")
cards['jack_diamonds'] = pygame.image.load("jack_diamonds.png")

cards['clubs_2'] = pygame.image.load("2_clubs.png")
cards['spades_2'] = pygame.image.load("2_spades.png")
cards['hearts_2'] = pygame.image.load("2_hearts.png")
cards['diamonds_2'] = pygame.image.load("2_diamonds.png")

cards['clubs_3'] = pygame.image.load("3_clubs.png")
cards['spades_3'] = pygame.image.load("3_spades.png")
cards['hearts_3'] = pygame.image.load("3_hearts.png")
cards['diamonds_3'] = pygame.image.load("3_diamonds.png")

cards['clubs_4'] = pygame.image.load("4_clubs.png")
cards['spades_4'] = pygame.image.load("4_spades.png")
cards['hearts_4'] = pygame.image.load("4_hearts.png")
cards['diamonds_4'] = pygame.image.load("4_diamonds.png")

cards['clubs_5'] = pygame.image.load("5_clubs.png")
cards['spades_5'] = pygame.image.load("5_spades.png")
cards['hearts_5'] = pygame.image.load("5_hearts.png")
cards['diamonds_5'] = pygame.image.load("5_diamonds.png")

cards['clubs_6'] = pygame.image.load("6_clubs.png")
cards['spades_6'] = pygame.image.load("6_spades.png")
cards['hearts_6'] = pygame.image.load("6_hearts.png")
cards['diamonds_6'] = pygame.image.load("6_diamonds.png")

cards['clubs_7'] = pygame.image.load("7_clubs.png")
cards['spades_7'] = pygame.image.load("7_spades.png")
cards['hearts_7'] = pygame.image.load("7_hearts.png")
cards['diamonds_7']  = pygame.image.load("7_diamonds.png")

cards['clubs_8'] = pygame.image.load("8_clubs.png")
cards['spades_8'] = pygame.image.load("8_spades.png")
cards['hearts_8'] = pygame.image.load("8_hearts.png")
cards['diamonds_8'] = pygame.image.load("8_diamonds.png")

cards['clubs_9'] = pygame.image.load("9_clubs.png")
cards['spades_9'] = pygame.image.load("9_spades.png")
cards['hearts_9'] = pygame.image.load("9_hearts.png")
cards['diamonds_9'] = pygame.image.load("9_diamonds.png")

cards['clubs_10'] = pygame.image.load("10_clubs.png")
cards['spades_10'] = pygame.image.load("10_spades.png")
cards['hearts_10'] = pygame.image.load("10_hearts.png")
cards['diamonds_10'] = pygame.image.load("10_diamonds.png")
hidden=pygame.image.load("hidden1.jpg")


deck = ['ace_clubs','ace_spades', 'ace_hearts', 'ace_diamonds', 'king_clubs', 'king_spades', 'king_hearts', 'king_diamonds', 'queen_clubs', 'queen_spades', \
    'queen_hearts', 'queen_diamonds', 'jack_clubs', 'jack_spades', 'jack_hearts', 'jack_diamonds', 'clubs_10', 'clubs_9', 'clubs_8', 'clubs_7', 'clubs_6', \
    'clubs_5', 'clubs_4', 'clubs_3', 'clubs_2', 'spades_10', 'spades_9', 'spades_8', 'spades_7', 'spades_6', 'spades_5', 'spades_4', 'spades_3', 'spades_2', \
    'hearts_10', 'hearts_9', 'hearts_8', 'hearts_7', 'hearts_6', 'hearts_5', 'hearts_4', 'hearts_3', 'hearts_2', 'diamonds_10', 'diamonds_9', 'diamonds_8',\
    'diamonds_7', 'diamonds_6', 'diamonds_5', 'diamonds_4', 'diamonds_3', 'diamonds_2']

#_______________________________________________________________________________________________________________________________________
black = (0,0,0)

import random
random.shuffle(deck)

random_deck2 = []
random_deck = []
for x in range(1,25):
    # random.shuffle(deck)
    v = pop(deck)
    push(random_deck,v)



pygame.draw.rect(screen, black, (30,150,71,96),2)
pygame.draw.rect(screen, black, (130,150,71,96),2)
pygame.draw.rect(screen, black, (230,150,71,96),2)
pygame.draw.rect(screen, black, (330,150,71,96),2)
pygame.draw.rect(screen, black, (430,150,71,96),2)
pygame.draw.rect(screen, black, (530,150,71,96),2)
pygame.draw.rect(screen, black, (630,150,71,96),2)

box_1 = pygame.draw.rect(screen, black, (330,10,71,96),2)
box_2 = pygame.draw.rect(screen, black, (430,10,71,96),2)
box_3 = pygame.draw.rect(screen, black, (530,10,71,96),2)
box_4 = pygame.draw.rect(screen, black, (630,10,71,96),2)
box_1 = []
box_2 = []
box_3 = []
box_4 = []


deck1=[]
val=pop(deck)
push(deck1, val)
screen.blit(cards[val], (30, 150))

deck2=[]
for i in range(2):
    val=pop(deck)
    push(deck2, val)
screen.blit(hidden, (130, 150))
screen.blit(cards[val], (130, 180))


deck3=[]
for i in range(3):
    val=pop(deck)
    push(deck3, val)
screen.blit(hidden, (230, 150))
screen.blit(hidden, (230, 180))
screen.blit(cards[val], (230, 210))

deck4=[]
for i in range(4):
    val=pop(deck)
    push(deck4, val)
    screen.blit(hidden, (330, 150))
screen.blit(hidden, (330, 180))
screen.blit(hidden, (330, 210))
screen.blit(cards[val], (330, 240))


deck5=[]
for i in range(5):
    val=pop(deck)
    push(deck5, val)
screen.blit(hidden, (430, 150))
screen.blit(hidden, (430, 180))
screen.blit(hidden, (430, 210))
screen.blit(hidden, (430, 240))
screen.blit(cards[val], (430, 270))


deck6=[]
for i in range(6):
    val=pop(deck)
    push(deck6, val)
screen.blit(hidden, (530, 150))
screen.blit(hidden, (530, 180))
screen.blit(hidden, (530, 210))
screen.blit(hidden, (530, 240))
screen.blit(hidden, (530, 270))
screen.blit(cards[val], (530, 300))

deck7=[]
for i in range(7):
    val=pop(deck)
    push(deck7, val)
screen.blit(hidden, (630, 150))
screen.blit(hidden, (630, 180))
screen.blit(hidden, (630, 210))
screen.blit(hidden, (630, 240))
screen.blit(hidden, (630, 270))
screen.blit(hidden, (630, 300))
screen.blit(cards[val], (630, 330))

screen.blit(hidden, (30, 10))


#__________________________________________________________________________________________________________________________________

pressed = False
done = False
dragging = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
            
        if event.type == pygame.MOUSEBUTTONDOWN: #mouse is pressed
            pressed = True
            mouse_position = pygame.mouse.get_pos() #gets the mouse co-ordinates
            tup = mouse_P(mouse_position) #finds which card the cursor is on based on the mouse co-ordinates
            #tup = (x,y,deck)
            if 10 <= mouse_position[1] <=110 and 30<= mouse_position[0]<=101: #clicking anywhere besides the random deck and bottom decks
                rect = False
            else:
                rect = True
                rectangle = pygame.rect.Rect(tup[0], tup[1], 71, 96) #if card is not hidden then it will create a rectangle on it to make it move

            if mouse_position[0]<100 and mouse_position[1]<105:
                if len(random_deck)!=0:    #BLIT RANDOM DECK UNTIL THE DECK IS EMPTY
                    a = pop(random_deck)
                    screen.blit(cards[a], [130, 10])
                    push(random_deck2,a)
                    screen.blit(hidden, (30, 10))

                else: #if the random deck is empty
                    pygame.draw.rect(screen,green,(30,10,71,96))
                    back_to_random1(random_deck2) #push the cards back into random_deck

            if event.button == 1 and rect!=False:  #drag function         
                if rectangle.collidepoint(mouse_position): #cursor position is inside the rectangle boundaries
                    dragging = True
                    mouse_x, mouse_y = mouse_position #the mouse co-ordinates
                    x_new = rectangle.x - mouse_x
                    y_new = rectangle.y - mouse_y



        elif event.type == pygame.MOUSEBUTTONUP: #mouse is not being pressed anymore
            pressed = False
            if event.button == 1 and rect!=False: #there is a rectangle being moved           
                dragging = False
                val = rectangle.x #rectangle x-value
                
                final_position = rect_position(val) #returns the co-ordinates of where you want to drag the card to. returns the position of that card
                initial_position = mouse_P(mouse_position) #returns initial card co-ordinates. the card which you wanted to move
                #(x,y,deck)
                if final_position!= False and initial_position!= False: 
                    lst = initial_position[2][-1] #deck's last value
                    # call a function which checks eligibility 
                    check = check_next_card(final_position[2], initial_position[2]) #checks the sorting. can the card be dragged or not. checks based on deck value 
                    #ans[2] = deck
                    print(check)
                    if check == True: #ans card can be moved on ans1
                        if initial_position[2]==' ': #no deck value given #FOR THE RANDOM DECK CARD BEING DRAGGED
                            a = pop(random_deck2)  ##THIS WILL POP THE DRAGGED CARD FROM ITS DECK
                            # print(random_deck2)
                            screen.blit(cards[a],(final_position[0], final_position[1])) ## THIS WILL BLIT THE DRAGGED CARD on top of the card you want to drag to
                            #screen.blit(surface, (x,y))
                            final_position[2].append(a) #append random card into deck
                            pygame.draw.rect(screen,green,(initial_position[0], initial_position[1],71,96)) #draw a green rectangle after moving the random deck card to show the area is empty
                            is_random = True
                        else: #BOTTOM DECK
                            screen.blit(cards[lst], (final_position[0], final_position[1])) #blit the card on top of the card you want to drag to
                            print(final_position[0], final_position[1])
                            next_card = pop(initial_position[2]) #pop the iniial card from the deck
                            final_position[2].append(next_card) #append into the deck you dragged the card onto
                            print(final_position[2])
                            pygame.draw.rect(screen,green,(initial_position[0], initial_position[1],71,96)) #draw a rectangle where the card intially was to show it's empty
                            is_random = False
                        if len(initial_position[2])!=0  and final_position[2]!= initial_position[2]: #if there is a deck value and if the 2 deck values are not the same
                            if is_random == False: 
                                screen.blit(cards[initial_position[2][-1]], (initial_position[0], initial_position[1]-30)) #show the new top value
                    else:
                        print('False')

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + x_new
                rectangle.y = mouse_y + y_new


    pygame.display.flip()
    clock.tick(60) #a higher value increase the fps rate

pygame.display.update()
pygame.quit()
