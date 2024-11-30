import pgzrun
import random
WIDTH=500
HEIGHT=500
sCORE=0
GAME_OVER=False
Cat=Actor("C:/Users/17657/OneDrive/Desktop/game dev/images/cat.png")
Cat.pos=(100,100)
Mouse=Actor("C:/Users/17657/OneDrive/Desktop/game dev/images/rat.png")
Mouse.pos=(200,200)
def draw():
    screen.blit("C:/Users/17657/OneDrive/Desktop/game dev/images/background.png",(0,0))
    Mouse.draw()
    Cat.draw()
    screen.draw.text("SCORE:"+str(sCORE),color="blue",topleft=(10,10))
    if GAME_OVER:
        screen.fill("pink")
        screen.draw.text("Time up! Your final score is"+str(sCORE),midtop=(WIDTH/2,10),fontsize=40,color="red")
def place_mouse():
    Mouse.x=random.randint(70,(WIDTH-70))
    Mouse.y=random.randint(70,(HEIGHT-70))
def time_up():
    global GAME_OVER
    GAME_OVER=True
def update():
    global sCORE
    if keyboard.left:
        Cat.x=Cat.x-2
    if keyboard.right:
        Cat.x=Cat.x+2
    if keyboard.up:
        Cat.y=Cat.y-2
    if keyboard.down:
        Cat.y=Cat.y+2
    Mouse_collected=Cat.colliderect(Mouse)
    if Mouse_collected:
        sCORE=sCORE+10
        place_mouse()
clock.schedule(time_up,100)
pgzrun.go()