
import json
import os
import random
import pygame

playerhpmax = 10
playerhp = 10
playeratk = 1
playerdef = 7
playerxp = 0
playerlvl = 1
cur_enemy = None
black = (0, 0, 0)


def render():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((480,480))
    pygame.display.set_caption('Adventure Time')
    

    
  
    #for event in pygame.event.get():
     # if event.type == pygame.QUIT:
              #pygame.quit()
              #quit()
    going = True
    while(going):

        screen.fill((black))
        font = pygame.font.SysFont("comicsansms", 72)

        text = font.render("Hello, World", True, (0, 128, 0))
	print(123)
      
        pygame.display.update()
       
    
render()

def choices():
  choice = input(data)
  type(choice)

def roll(pips):
  rand = random.randint(1,pips)
  return rand
  
def lvlup():
  if(playerxp >= playerlvl*playerlvl + 9):
    playerxp = 0
    playerlvl += 1
    playerhpmax += 2
    playerhp = playerhpmax
    if(playerlvl % 2 == 0):
      playeratk += 13
    if(playerlvl % 5 == 0):
      playerdef += 1
    
    
def battol(playerhpx,state):
  clear = lambda: os.system('cls')
 
  cur_enemy = enemie[data[state]["enemytype"]][data[state]["enemy"]]
  if cur_enemy["hp"] <= 0:
      clear()
      print("You already defeated " + data[state]["enemy"])
  else:  
    render(cur_enemy["img"])
    clear()
    #print(playerhpx)
    while(cur_enemy["hp"] > 0 and playerhpx > 0):
        #print(playerhpx)
        tempdef = playerdef
        print(data[state]["choices"][0]["prompt"])
        btlchoice = input()
        clear()
        tempdef = playerdef
        if(btlchoice == "1"):
            print("You swing your fist at "+data[state]["enemy"])
            rand = roll(20)
            if(rand > (cur_enemy["def"]-playeratk) and rand != 20 and rand != 1):
              print("You hit "+ data[state]["enemy"])
              cur_enemy["hp"] -= playeratk
              print("")
            elif(rand >= 20):
              print("You hit "+data[state]["enemy"]+" with a strong blow.")
              cur_enemy["hp"] -= 2*playeratk
              print("")
            elif(rand != 1):
              print("You miss " +data[state]["enemy"])
              print("")
            else:
                print("You swing too hard and trip yourself.")
                print("")
                playerhpx = playerhpx - 1
        #print(rand)
        elif(btlchoice == "2"):
            print("You prepare for an incoming attack.")
            print("")
            tempdef = playerdef*2
        elif(btlchoice == "3"):
            print("You Take a Fine Look at The Enemy, Then Yourself")
            print("The Enemy looks to have around "+str(cur_enemy["hp"]) +"hp")
            print("You have around "+str(playerhpx)+"hp")
            print("")
    
        print(data[state]["enemy"]+" attacks!")
    
        if(data[state]["enemytype"] == "basic"):
            enemierol = roll(20)
     
            if(enemierol+cur_enemy["atk"] > tempdef):
                  playerhpx = playerhpx - cur_enemy["atk"]
                  print("")
            else:
             print(data[state]["enemy"]+" misses you!")
             print("")

  pygame.quit()
  return playerhpx

#with open("States.json","r") as f:
  #data = json.loads(f.read())
  
#with open("enemies.json","r") as e:
  #enemie = json.loads(e.read())
#for x in data["characters"]:
#   print(x["name"])


#choices()
def maingame(state):
    while state != "win" and state != "dead":
        if(len (data[state]["choices"]) <= 1 and "specialtype" not in(data[state])):
            print(data[state]["choices"][0]["prompt"])
            choice = input()
            if(choice in data["yeses"]):
                state = data[state]["choices"][0]["state"]
        elif("specialtype" not in data[state]):
            for choice in data[state]["choices"]:
                print(choice["prompt"])
            choicemulti = input()
            if(choicemulti =="3"):
                state = data[state]["choices"][2]["state"]
            elif(choicemulti== "2"):
                state = data[state]["choices"][1]["state"]
            elif(choicemulti =="1"):
                state = data[state]["choices"][0]["state"]
        else:
            if(data[state]["specialtype"] == "battle"):
           
          
                resultshp = battol(playerhp,state)
                if(resultshp > 0):
                    print("You defeat the "+data[state]["enemy"])
                    state = "crossroads"
           
                else:
                    state = "dead"
            
            elif(data[state]["specialtype"] == "dead"):
                print(data[state]["choices"][0]["prompt"])
                state = "dead"
            
        if(state == "dead"):
            print("You died!")
        elif(state == "win"):
            print("You have gotten the treasure and won!")

#maingame("entrance")