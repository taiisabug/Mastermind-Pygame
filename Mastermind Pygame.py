# hello mr. k, i leave lots of comments for you to help you understand what is going on :>
                                                                                        
from pygame import *                                                                                        # these three lines i import pygame, random, sys and math. the first two lines i do 
from random import *                                                                                        # something funky so i don't need to do "pygame.blahblah" every time
import pygame, math, sys

# -------------------------------- V A R I A B L E S --------------------------------------------------------------------------

# c o l o u r s 
RED = [255, 89, 94]                                                                                         # these are all my colour variables. less than halloween house 
ORANGE = [251, 177, 60]
YELLOW = [255, 206, 92]
GREEN = [138, 201, 38]
BLUE = [25, 130, 196]
PURPLE = [106, 76, 147]
BLACK = [15, 15, 15]
WHITE = [247, 244, 243]
LIGHTBROWN = [213, 198, 195]
BROWN = [157, 120, 108]
DARKBROWN = [98, 73, 65]

# g u e s s e s
colors = ["R", "O", "Y", "G", "B", "P"]
GUESS = [WHITE, WHITE, WHITE, WHITE]                                                                        # here are my variables for the guesses and co. i had to switch languages for my variables
SATU = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]                                                     # because it made more sense in my mind. the first 8 variables are in indonesian 
DUA = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]                                                      # (numbers one to eight), then it goes to french
TIGA = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]                                                     # indonesian variables represent the 4 colour guesses entered by user
EMPAT = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]                                                    # french variables represent the 4 colours telling user if they are right or wrong
LIMA = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
ENAM = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
TUJUH = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
DELAPAN = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
UN = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
DEUX = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN] 
TROIS = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
QUATRE = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
CINQ = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
SIX = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
SEPT = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
HUIT = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]

# i f   s t a t e m e n t   v a r i a b l e s
run = True
game = False
rules = False
startmenu = True 
win = False
lose = False
double = False
five = False

# c o u n t e r s
i = 0
message = ''
enter = [0,0,0,0]
counterenter = 0
counterspot = 0
countercorrect = 0
french = 0

# -------------------------------- S T A R T   U P --------------------------------------------------------------------------

pygame.init()                                                                                               # here i start up the game. ignore the title; my original code didn't work so i had to 
pygame.display.set_caption('tls mastermind project || PART TWO I WANT TO RIP OUT MY EYEBALLS')              # restart, hence 'part two || i want to rip out my eyeballs'

SIZE = (400, 600)                                                                                           # more initializing stuff, this line dictates the screen size and further lines dictate
screen = pygame.display.set_mode(SIZE)                                                                      # background colours
pygame.draw.rect(screen, LIGHTBROWN, (0, 0, 400, 700))


# -------------------------------- F U N C T I O N S --------------------------------------------------------------------------

def distance(x, y, xx, yy):                                                                                 # function to calculate distance of the circle button. i took it from your code
    return(math.sqrt((x-xx)**2 + (y-yy)**2))

def menuScreen():                                                                                           # this is my menu screen. all of my other functions include these commands, so i will
    pygame.draw.rect(screen, LIGHTBROWN, (0, 0, 400, 700))                                                  # explain it once here, and when you see it again you can refer back to this.
    pygame.draw.rect(screen, BROWN, (100, 175, 200, 50))
    pygame.draw.rect(screen, BROWN, (100, 250, 200, 50))
    pygame.draw.rect(screen, BROWN, (100, 325, 200, 50))    
    pygame.draw.rect(screen, DARKBROWN, (100, 175, 200, 50), 2)                                             # anything pygame.draw is a shape. this '.rect' draws a rectangle on the 'screen' in the 
    pygame.draw.rect(screen, DARKBROWN, (100, 250, 200, 50), 2)                                             # colour 'DARKBROWN' starting at x = 100, and y = 170 and goes over 200 units right and 
    pygame.draw.rect(screen, DARKBROWN, (100, 325, 200, 50), 2)                                             # 50 units down. if there is another number, it is outlined 
    
    font = pygame.font.Font('fixedsys.ttf', 40)                                                             # this defines my font as 'fixedsys.ttf' in size 40.
    text = font.render('START', False, BLACK)                                                               # then, this defines the text as 'START', turns off anti-aliasing and makes the colour 'BLACK'
    screen.blit(text, (150, 180))                                                                           # finally, the text is 'blitted' on the screen at x = 150, y = 180
    text = font.render('RULES', False, BLACK)
    screen.blit(text, (150, 255))  
    text = font.render('EXIT', False, BLACK)
    screen.blit(text, (150, 330))     
    pygame.display.update()                                                                                 # at the end of every function i refresh the screen in case any variables are changed.
                                                                                                            # this doesn't do much now, but for my message box and gameScreen it is important.


def rulesScreen():                                                                                          # this is my rules screen. if a user presses the rules button, this screen will display
    pygame.draw.rect(screen, LIGHTBROWN, (0, 0, 400, 700))                                                  # showing the user how to play mastermind. very basic, but it's enough to get them to 
    pygame.draw.line(screen, BROWN, (50, 100), (350, 100), 4)                                               # understand the basics. all this function does is print the code for the rules however,
    font = pygame.font.Font('fixedsys.ttf', 40)                                                             # there is no buttons in the function, just the background which the button will lie on.
    text = font.render('Rules', False, BLACK)
    screen.blit(text, (60, 60))    
    font = pygame.font.Font('fixedsys.ttf', 15)
    text = font.render('- The computer picks a sequence of ', False, BLACK)
    screen.blit(text, (40, 120))
    text = font.render('  colors. You are to guess the exact', False, BLACK)
    screen.blit(text, (40, 140))
    text = font.render('  positions of the colors in', False, BLACK)
    screen.blit(text, (40, 160))   
    text = font.render('  the computer sequence.', False, BLACK)
    screen.blit(text, (40, 180))  
    text = font.render('- Each color in the correct position', False, BLACK)
    screen.blit(text, (40, 200))        
    text = font.render('  and color in the sequence,', False, BLACK)
    screen.blit(text, (40, 220))        
    text = font.render('  the computer displays a red color', False, BLACK)
    screen.blit(text, (40, 240))        
    text = font.render('  on the right side of the guess.', False, BLACK)
    screen.blit(text, (40, 260))        
    text = font.render('- Each color that is the correct', False, BLACK)
    screen.blit(text, (40, 280))  
    text = font.render('  color but is not in the correct position,', False, BLACK)
    screen.blit(text, (40, 300)) 
    text = font.render('  the computer displays a white color', False, BLACK)
    screen.blit(text, (40, 320)) 
    text = font.render('  on the right side of the guess.', False, BLACK)
    screen.blit(text, (40, 340)) 
    text = font.render('- You win when you manage to ', False, BLACK)
    screen.blit(text, (40, 360)) 
    text = font.render('  guess all the colors in ', False, BLACK)
    screen.blit(text, (40, 380)) 
    text = font.render('  the right position.', False, BLACK)
    screen.blit(text, (40, 400)) 
    text = font.render('- You lose the game if you ', False, BLACK)
    screen.blit(text, (40, 420))    
    text = font.render('  use all attempts without guessing ', False, BLACK)
    screen.blit(text, (40, 440))     
    text = font.render('  the correct sequence.', False, BLACK)
    screen.blit(text, (40, 460))     
    text = font.render('- GOOD LUCK!!!', False, DARKBROWN)
    screen.blit(text, (40, 480))         
    pygame.draw.rect(screen, BROWN, (275, 520, 75, 40))
    pygame.draw.rect(screen, DARKBROWN, (275, 520, 75, 40), 2)
    font = pygame.font.Font('fixedsys.ttf', 20)
    text = font.render('Return', False, BLACK)
    screen.blit(text, (280, 530))   
    pygame.display.update()
        
        
def gameScreen():                                                                                           # this my game screen. my largest function, i use different languages to organize everything
    
    # g u e s s e s
    pygame.draw.rect(screen, LIGHTBROWN, (0, 0, 400, 700))                                                  # this is where the user will see the 6 colour options, their guess boxes and a check button.
    pygame.draw.rect(screen, BROWN, (25, 500, 350, 75))                                                     # the function does not actually include buttons, just like the rules screen, it is the 
    pygame.draw.rect(screen, DARKBROWN, (25, 500, 350, 75), 2)                                              # image for where the button will be. the button is later on in the game loops.
    pygame.draw.circle(screen, RED, (75, 460), 15)
    pygame.draw.circle(screen, ORANGE, (125, 460), 15)
    pygame.draw.circle(screen, YELLOW, (175, 460), 15)
    pygame.draw.circle(screen, GREEN, (225, 460), 15)
    pygame.draw.circle(screen, BLUE, (275, 460), 15)
    pygame.draw.circle(screen, PURPLE, (325, 460), 15)    
    pygame.draw.circle(screen, GUESS[0], (60, 50), 25)   
    pygame.draw.circle(screen, GUESS[1], (120, 50), 25)    
    pygame.draw.circle(screen, GUESS[2], (180, 50), 25)    
    pygame.draw.circle(screen, GUESS[3], (240, 50), 25)    
    pygame.draw.circle(screen, BLACK, (60, 50), 25, 1)   
    pygame.draw.circle(screen, BLACK, (120, 50), 25, 1)    
    pygame.draw.circle(screen, BLACK, (180, 50), 25, 1)    
    pygame.draw.circle(screen, BLACK, (240, 50), 25, 1)  
    pygame.draw.rect(screen, BROWN, (280, 25, 80, 50))
    pygame.draw.rect(screen, DARKBROWN, (280, 25, 80, 50), 1)
    font = pygame.font.Font('fixedsys.ttf', 25)
    text = font.render('Check', False, BLACK)
    screen.blit(text, (287, 35))
    
    pygame.draw.line(screen, BROWN, (50, 90), (160, 90), 2)
    pygame.draw.line(screen, BROWN, (235, 90), (350, 90), 2)
    pygame.draw.line(screen, BROWN, (50, 430), (160, 430), 2)
    pygame.draw.line(screen, BROWN, (240, 430), (350, 430), 2)
    
    font = pygame.font.Font('fixedsys.ttf', 10)
    text = font.render('Your Guesses', False, BLACK)
    screen.blit(text, (165, 85))    
    text = font.render('Color Options', False, BLACK)
    screen.blit(text, (165, 425))    
    
    # m e s s a g e                                                                                         # this is my message box. im very happy with how it came out :>
    font = pygame.font.Font('fixedsys.ttf', 20)                                                             # like i mentioned earlier, as the screen is refreshed in this function, if the message
    text = font.render(message, False, BLACK)                                                               # variable changes, the message on the screen changes.
    screen.blit(text, (35, 515)) 
    
    # t e b a k                                                                                             # 'tebak' is guess in indonesian. since this category is using my indonesian variables, 
    pygame.draw.circle(screen, SATU[0], (75, 400), 15)                                                      # i figured tebak is a good way to organize this category. after the user inputs guesses
    pygame.draw.circle(screen, SATU[1], (125, 400), 15)                                                     # this is where they're guess gets replayed back to them with the hints on if they are 
    pygame.draw.circle(screen, SATU[2], (175, 400), 15)                                                     # correct or not!
    pygame.draw.circle(screen, SATU[3], (225, 400), 15)
                                                                                                            # as mentioned earlier:
    pygame.draw.circle(screen, UN[0], (270, 393), 5)                                                        # indonesian variables represent the 4 colour guesses entered by user    
    pygame.draw.circle(screen, UN[1], (285, 393), 5)                                                        # french variables represent the 4 colours telling user if they are right or wrong
    pygame.draw.circle(screen, UN[2], (270, 408), 5)
    pygame.draw.circle(screen, UN[3], (285, 408), 5)
    
    pygame.draw.circle(screen, DUA[0], (75, 360), 15)   
    pygame.draw.circle(screen, DUA[1], (125, 360), 15)    
    pygame.draw.circle(screen, DUA[2], (175, 360), 15)    
    pygame.draw.circle(screen, DUA[3], (225, 360), 15)      
    
    pygame.draw.circle(screen, DEUX[0], (270, 353), 5)
    pygame.draw.circle(screen, DEUX[1], (285, 353), 5)
    pygame.draw.circle(screen, DEUX[2], (270, 368), 5)
    pygame.draw.circle(screen, DEUX[3], (285, 368), 5)    
    
    pygame.draw.circle(screen, TIGA[0], (75, 320), 15)   
    pygame.draw.circle(screen, TIGA[1], (125, 320), 15)    
    pygame.draw.circle(screen, TIGA[2], (175, 320), 15)    
    pygame.draw.circle(screen, TIGA[3], (225, 320), 15)    
    
    pygame.draw.circle(screen, TROIS[0], (270, 313), 5)
    pygame.draw.circle(screen, TROIS[1], (285, 313), 5)
    pygame.draw.circle(screen, TROIS[2], (270, 328), 5)
    pygame.draw.circle(screen, TROIS[3], (285, 328), 5)        
    
    pygame.draw.circle(screen, EMPAT[0], (75, 280), 15)   
    pygame.draw.circle(screen, EMPAT[1], (125, 280), 15)    
    pygame.draw.circle(screen, EMPAT[2], (175, 280), 15)    
    pygame.draw.circle(screen, EMPAT[3], (225, 280), 15)    
    
    pygame.draw.circle(screen, QUATRE[0], (270, 273), 5)
    pygame.draw.circle(screen, QUATRE[1], (285, 273), 5)
    pygame.draw.circle(screen, QUATRE[2], (270, 288), 5)
    pygame.draw.circle(screen, QUATRE[3], (285, 288), 5)        
    
    pygame.draw.circle(screen, LIMA[0], (75, 240), 15)   
    pygame.draw.circle(screen, LIMA[1], (125, 240), 15)    
    pygame.draw.circle(screen, LIMA[2], (175, 240), 15)    
    pygame.draw.circle(screen, LIMA[3], (225, 240), 15)    
    
    pygame.draw.circle(screen, CINQ[0], (270, 233), 5)
    pygame.draw.circle(screen, CINQ[1], (285, 233), 5)
    pygame.draw.circle(screen, CINQ[2], (270, 248), 5)
    pygame.draw.circle(screen, CINQ[3], (285, 248), 5)        
    
    pygame.draw.circle(screen, ENAM[0], (75, 200), 15)   
    pygame.draw.circle(screen, ENAM[1], (125, 200), 15)    
    pygame.draw.circle(screen, ENAM[2], (175, 200), 15)    
    pygame.draw.circle(screen, ENAM[3], (225, 200), 15)    
    
    pygame.draw.circle(screen, SIX[0], (270, 193), 5)
    pygame.draw.circle(screen, SIX[1], (285, 193), 5)
    pygame.draw.circle(screen, SIX[2], (270, 208), 5)
    pygame.draw.circle(screen, SIX[3], (285, 208), 5)      
    
    pygame.draw.circle(screen, TUJUH[0], (75, 160), 15)   
    pygame.draw.circle(screen, TUJUH[1], (125, 160), 15)    
    pygame.draw.circle(screen, TUJUH[2], (175, 160), 15)    
    pygame.draw.circle(screen, TUJUH[3], (225, 160), 15)    
    
    pygame.draw.circle(screen, SEPT[0], (270, 153), 5)
    pygame.draw.circle(screen, SEPT[1], (285, 153), 5)
    pygame.draw.circle(screen, SEPT[2], (270, 168), 5)
    pygame.draw.circle(screen, SEPT[3], (285, 168), 5)         
    
    pygame.draw.circle(screen, DELAPAN[0], (75, 120), 15)   
    pygame.draw.circle(screen, DELAPAN[1], (125, 120), 15)    
    pygame.draw.circle(screen, DELAPAN[2], (175, 120), 15)    
    pygame.draw.circle(screen, DELAPAN[3], (225, 120), 15) 
    
    pygame.draw.circle(screen, HUIT[0], (270, 113), 5)
    pygame.draw.circle(screen, HUIT[1], (285, 113), 5)
    pygame.draw.circle(screen, HUIT[2], (270, 128), 5)
    pygame.draw.circle(screen, HUIT[3], (285, 128), 5)           
        
    pygame.display.update()
    
def winScreen():                                                                                            # win screen. pretty self explanitory, it's like the main menu except it tells you
    pygame.draw.rect(screen, LIGHTBROWN, (0, 0, 400, 700))                                                  # the final correct answer. it also includes a option to play again if you don't want
    font = pygame.font.Font('fixedsys.ttf', 40)                                                             # to go back to the main screen
    text = font.render('YOU WIN!!!', False, BLACK)
    screen.blit(text, (100, 180))  
    pygame.draw.rect(screen, BROWN, (100, 275, 200, 50))
    pygame.draw.rect(screen, BROWN, (100, 350, 200, 50))
    pygame.draw.rect(screen, BROWN, (100, 425, 200, 50))    
    pygame.draw.rect(screen, DARKBROWN, (100, 275, 200, 50), 2)
    pygame.draw.rect(screen, DARKBROWN, (100, 350, 200, 50), 2)    
    pygame.draw.rect(screen, DARKBROWN, (100, 425, 200, 50), 2)
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render('PLAY AGAIN?', False, BLACK)
    screen.blit(text, (110, 285))    
    text = font.render('RETURN MENU', False, BLACK)
    screen.blit(text, (110, 360))  
    text = font.render('EXIT', False, BLACK)
    screen.blit(text, (110, 435))     
    
    font = pygame.font.Font('fixedsys.ttf', 20)
    text = font.render('The answer was:', False, BLACK)
    screen.blit(text, (35, 50)) 
    
    for i in range(0, 3):                                                                                   # another feature i added to both the win and lose screen is the correct answer.
        pygame.draw.circle(screen, answer[0], (60, 110), 25)                                                # if you run out of guesses, it displays the right answer. it's just some qol things
        pygame.draw.circle(screen, answer[1], (120, 110), 25)    
        pygame.draw.circle(screen, answer[2], (180, 110), 25)    
        pygame.draw.circle(screen, answer[3], (240, 110), 25)      
    
    pygame.draw.circle(screen, BLACK, (60, 110), 25, 1)   
    pygame.draw.circle(screen, BLACK, (120, 110), 25, 1)    
    pygame.draw.circle(screen, BLACK, (180, 110), 25, 1)    
    pygame.draw.circle(screen, BLACK, (240, 110), 25, 1)  
    
    pygame.display.update()    

def loseScreen():                                                                                           # my lose screen is the exact same code for my win screen, except the wording is different.
    pygame.draw.rect(screen, LIGHTBROWN, (0, 0, 400, 700))                                                  # next time, i would like to add an if statement so i don't need to repeat code, and can 
    font = pygame.font.Font('fixedsys.ttf', 40)                                                             # instead print the words different. just another thing to optomize the code.
    text = font.render('YOU LOST :( ', False, BLACK)
    screen.blit(text, (90, 150)) 
    text = font.render('GG GO NEXT?', False, BLACK)
    screen.blit(text, (90, 190))      
    pygame.draw.rect(screen, BROWN, (100, 275, 200, 50))
    pygame.draw.rect(screen, BROWN, (100, 350, 200, 50))
    pygame.draw.rect(screen, BROWN, (100, 425, 200, 50))    
    pygame.draw.rect(screen, DARKBROWN, (100, 275, 200, 50), 2)
    pygame.draw.rect(screen, DARKBROWN, (100, 350, 200, 50), 2)    
    pygame.draw.rect(screen, DARKBROWN, (100, 425, 200, 50), 2)
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render('PLAY AGAIN?', False, BLACK)
    screen.blit(text, (110, 285))    
    text = font.render('RETURN MENU', False, BLACK)
    screen.blit(text, (110, 360))  
    text = font.render('EXIT', False, BLACK)
    screen.blit(text, (110, 435))     
    
    font = pygame.font.Font('fixedsys.ttf', 20)
    text = font.render('The answer was:', False, BLACK)
    screen.blit(text, (35, 50)) 
    
    for i in range(0, 3):
        pygame.draw.circle(screen, answer[0], (60, 110), 25)   
        pygame.draw.circle(screen, answer[1], (120, 110), 25)    
        pygame.draw.circle(screen, answer[2], (180, 110), 25)    
        pygame.draw.circle(screen, answer[3], (240, 110), 25)       
    
    pygame.draw.circle(screen, BLACK, (60, 110), 25, 1)   
    pygame.draw.circle(screen, BLACK, (120, 110), 25, 1)    
    pygame.draw.circle(screen, BLACK, (180, 110), 25, 1)    
    pygame.draw.circle(screen, BLACK, (240, 110), 25, 1)  
    
    pygame.display.update()    


# -------------------------------- G A M E --------------------------------------------------------------------------
    
while run == True:                                                                                          # finally at line 351, my game starts with this run loop
    while startmenu == True:                                                                                # the start menu starts true, so the start menu is the first screen you see.
        menuScreen()                                                                                        # all the buttons are in for/if statements below
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if mousex >= 100 and mousex <= 300 and mousey >= 175 and mousey <= 225:
                    startmenu = False
                    game = True
                if mousex >= 100 and mousex <= 300 and mousey >= 250 and mousey <= 300:
                    startmenu = False
                    rules = True  
                if mousex >= 100 and mousex <= 300 and mousey >= 325 and mousey <= 375:
                    pygame.quit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()                                 
                    
    while rules == True:                                                                                    # this is the rules screen. it only triggers if the rules button is pressed.   
        rulesScreen()                                                                                       # the user can return to menu from this screen
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if mousex >= 275 and mousex <= 350 and mousey >= 520 and mousey <= 560:
                    rules = False        
                    startmenu = True
        
    shuffle(colors)                                                                                         # once the menu screen is done with, the loop goes to choose the 4 colours for the game
    order = colors[:4]
    print (order)                                                                                          # if you want to always win, remove the '#' and it'll print the answer for you
    counterround = 0
    answer = []
    
    for x in range(len(order)):                                                                             # all this does is prepare the answer for the end screen
        if order[x] == "R":
            answer += [RED]
        elif order[x] == "O":
            answer += [ORANGE]
        elif order[x] == "Y":
            answer += [YELLOW]
        elif order[x] == "G":
            answer += [GREEN]
        elif order[x] == "B":
            answer += [BLUE]
        elif order[x] == "P":
            answer += [PURPLE]
        
    while game == True:                                                                                     # this is the actual game game, it's all my buttons to go overtop the display
        gameScreen()     
        for event in pygame.event.get():      
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos   
                
                # c o l o u r   c i r c l e   b u t t o n s
                if (distance(mousex, mousey, 75, 460) < 15):
                    if i == 4:
                        five = True                        
                    else:
                        GUESS[i] = RED
                        enter[i] = "R"
                        i += 1  
                    if 0 in enter:
                        i = (enter.index(0))
                    else:
                        i = 4      
                elif (distance(mousex, mousey, 125, 460) < 15):
                    if i == 4:
                        five = True   
                    else:
                        GUESS[i] = ORANGE
                        enter[i] = "O"
                        i += 1
                    if 0 in enter:
                        i = (enter.index(0))
                    else:
                        i = 4      
                elif (distance(mousex, mousey, 175, 460) < 15):
                    if i == 4:
                        five = True     
                    else:
                        GUESS[i] = YELLOW
                        enter[i] = "Y"
                        i += 1      
                    if 0 in enter:
                        i = (enter.index(0))
                    else:
                        i = 4      
                elif (distance(mousex, mousey, 225, 460) < 15):
                    if i == 4:
                        five = True      
                    else:
                        GUESS[i] = GREEN
                        enter[i] = "G"
                        i += 1  
                    if 0 in enter:
                        i = (enter.index(0))
                    else:
                        i = 4      
                elif (distance(mousex, mousey, 275, 460) < 15):
                    if i == 4:
                        five = True       
                    else:
                        GUESS[i] = BLUE
                        enter[i] = "B"
                        i += 1  
                    if 0 in enter:
                        i = (enter.index(0))
                    else:
                        i = 4      
                elif (distance(mousex, mousey, 325, 460) < 15):
                    if i == 4:
                        five = True   
                    else:
                        GUESS[i] = PURPLE
                        enter[i] = "P"
                        i += 1   
                    if 0 in enter:
                        i = (enter.index(0))
                    else:
                        i = 4      
                        
                # c o r r e c t i o n   b u t t o n s
                elif (distance(mousex, mousey, 60, 50) < 25):                                               # this is if you need to correct something, this is the buttons that do it.
                    i = 0                                                                                   # just click on the circle you want to correct, and then the colour you want to change it to
                elif (distance(mousex, mousey, 120, 50) < 25):
                    i = 1
                elif (distance(mousex, mousey, 180, 50) < 25):
                    i = 2
                elif (distance(mousex, mousey, 240, 50) < 25):
                    i = 3   
                    
                # c h e c k   b u t t o n 
                elif mousex >= 280 and mousex <= 360 and mousey >= 25 and mousey <= 75 and i == 4:          # this is the check button. it wont work unless 4 colours are inputed

                    # d o u b l e   c o l o u r s
                    if enter[0] == enter [1]:                                                               # all of these if statements check to see if any colours are repeated. if they are
                        double = True                                                                       # the guess gets reset and a message pops up
                    elif enter[0] == enter [2]:
                        double = True
                    elif enter[0] == enter [3]:
                        double = True
                    elif enter[1] == enter [2]:
                        double = True
                    elif enter[1] == enter [3]:
                        double = True
                    elif enter[2] == enter [3]:
                        double = True
                    if double == True:
                        message = 'You cannot enter double colors'
                        GUESS = [WHITE, WHITE, WHITE, WHITE]                            
                        enter = [0,0,0,0]
                        i = 0
                        double = False
                        break
                    
                    # w i n
                    if (list(enter)) == (list(order)):                                                      # if the entered guess is the order selected by the code, the game ends and win screen pops up
                        game = False
                        win = True
                    
                    # c o l o u r   s p o t s
                    for m in order:                                                                         # this counts how many colors entered by the user are the same as the code order
                        for n in enter:                                                                     # this does not take into account spots
                            if m == n:
                                countercorrect += 1
                
                    for i in range(4):                                                                      # this counts how many colours are in the same spot as the code order
                        if enter[i] == order[i]:
                            counterspot += 1
                
                    countercorrect -= counterspot                                                           # now taking the colours that are correct, i subtract all those in the right spot to get
                    counterround += 1                                                                       # the right colours in the wrong spot and increase the round up one
                    
                    # r o u n d s
                    if counterround == 1:                                                                   # all my codes for the round is the same. they start with detecting which round it is.
                        SATU = GUESS                                                                        # first it takes the guess and prints it out on the screen using the indonesian number.
                        message = 'You have 7 guesses left'                                                 # then it tells the user how many guesses they have left.
                        for count in range(counterspot):                                                    # next my loops use the french variables to dictate how many colours are in the right spot and
                            UN[french] = RED                                                                # correct colour. any extras go brown to not leave any blank spots.
                            french += 1
                        for count in range(countercorrect):
                            UN[french] = WHITE
                            french += 1     
                        while french != 4:
                            UN[french] = BROWN
                            french += 1
                    elif counterround == 2:                                                                 # just like i stated above, it repeats for the next 8 rounds
                        DUA = GUESS
                        message = 'You have 6 guesses left'
                        for count in range(counterspot):
                            DEUX[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            DEUX[french] = WHITE
                            french += 1                                 
                        while french != 4:
                            DEUX[french] = BROWN
                            french += 1                                  
                    elif counterround == 3:
                        message = 'You have 5 guesses left'                            
                        TIGA = GUESS
                        for count in range(counterspot):
                            TROIS[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            TROIS[french] = WHITE
                            french += 1     
                        while french != 4:
                            TROIS[french] = BROWN
                            french += 1                             
                    elif counterround == 4:
                        message = 'You have 4 guesses left'                            
                        EMPAT = GUESS
                        for count in range(counterspot):
                            QUATRE[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            QUATRE[french] = WHITE
                            french += 1     
                        while french != 4:
                            QUATRE[french] = BROWN
                            french += 1                             
                    elif counterround == 5:
                        message = 'You have 3 guesses left'                            
                        LIMA = GUESS
                        for count in range(counterspot):
                            CINQ[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            CINQ[french] = WHITE
                            french += 1     
                        while french != 4:
                            CINQ[french] = BROWN
                            french += 1                             
                    elif counterround == 6:
                        message = 'You have 2 guesses left'                            
                        ENAM = GUESS
                        for count in range(counterspot):
                            SIX[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            SIX[french] = WHITE
                            french += 1     
                        while french != 4:
                            SIX[french] = BROWN
                            french += 1                             
                    elif counterround == 7:
                        message = 'This is your last guess'                            
                        TUJUH = GUESS
                        for count in range(counterspot):
                            SEPT[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            SEPT[french] = WHITE
                            french += 1     
                        while french != 4:
                            SEPT[french] = BROWN
                            french += 1                             
                    elif counterround == 8:
                        DELAPAN = GUESS   
                        for count in range(counterspot):
                            HUIT[french] = RED
                            french += 1
                        for count in range(countercorrect):
                            HUIT[french] = WHITE
                            french += 1     
                        while french != 4:
                            HUIT[french] = BROWN
                            french += 1  
                            
                        if (list(enter)) != (list(order)):                                                  # if by round 8, the guess does not equal the code order, the lose screen is prompted
                            game = False
                            lose = True        
                            
                    # r e s e t
                    GUESS = [WHITE, WHITE, WHITE, WHITE]                                                    # at the end of the round, all the variables are reset to get a new input for the next round
                    enter = [0,0,0,0]
                    i = 0      
                    french = 0
                    counterspot = 0
                    countercorrect = 0
                        
            # f i v e   c o l o u r s
            if five == True:                                                                                # incase someone tries to enter 5 colours, this message is prompted and the guesses are reset
                i = 0
                enter = [0,0,0,0]
                message = 'Enter no more than 4 colours'
                GUESS = [WHITE, WHITE, WHITE, WHITE]
                five = False 
            
            # q u i t
            if event.type == QUIT:                                                                          # should the game crash or quit, this is in place to close the program properly
                pygame.quit()
                sys.exit() 
    
    if win == True or lose == True:                                                                         # this is a giant reset for all my variables, so if the user chooses to play again, 
        GUESS = [WHITE, WHITE, WHITE, WHITE]                                                                # they are reset for the next round
        SATU = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        DUA = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        TIGA = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        EMPAT = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        LIMA = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        ENAM = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        TUJUH = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        DELAPAN = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        UN = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        DEUX = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN] 
        TROIS = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        QUATRE = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        CINQ = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        SIX = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        SEPT = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]
        HUIT = [LIGHTBROWN, LIGHTBROWN, LIGHTBROWN, LIGHTBROWN]  
        i = 0
        message = ''
        enter = [0,0,0,0]
        counterenter = 0
        counterspot = 0
        countercorrect = 0
        french = 0        
                
    while win == True:                                                                                      # win screen. just like the main screen loop, it's all buttons to return to main screen,
        winScreen()                                                                                         # play again or quit
        for event in pygame.event.get():                                                                    
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if mousex >= 100 and mousex <= 300 and mousey >= 275 and mousey <= 325:    
                    win = False
                    game = True
                if mousex >= 100 and mousex <= 300 and mousey >= 350 and mousey <= 400: 
                    win = False
                    startmenu = True
                if mousex >= 100 and mousex <= 300 and mousey >= 425 and mousey <= 475: 
                    pygame.quit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
                    
    while lose == True:                                                                                     # exact same as the win screen, except for losers
        loseScreen()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if mousex >= 100 and mousex <= 300 and mousey >= 275 and mousey <= 325:    
                    lose = False
                    game = True
                if mousex >= 100 and mousex <= 300 and mousey >= 350 and mousey <= 400: 
                    lose = False
                    startmenu = True
                if mousex >= 100 and mousex <= 300 and mousey >= 425 and mousey <= 475: 
                    pygame.quit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
                
                
# finally... it's over... please level 4+ 100% :,>