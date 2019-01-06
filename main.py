from tkinter import *
from tkinter import font
import random
import time

Largeur = 1000
Hauteur = 666
b_size = 30
j_size = 140
point1 = 0
point2 = 0
reset = 0
timer = 0 
j_color = "white"

pong = Tk()
fenetre = Canvas(pong, width=Largeur, height=Hauteur, bg="black")

    ######## Police ########
pjeu = font.Font(family="Controwell", size=20, weight="bold")
pmenu = font.Font(family="Pricedown Normal", size=22, weight="bold")

    ######## Balle ########
class Balle:
    def __init__(self, canvas, color):
        global starts
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, b_size, b_size, fill = color)
        self.canvas.move(self.id, 489, 322.5)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
  
    def mouvement(self):
        global pos, point1, point2, reset
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        initialx = -(pos[0])+489
        initialy = -(pos[1])+322.5

        if pos[1] <= 0:
            self.y = 3
        elif pos[3] >= self.canvas_height:
            self.y = -3
        ### Retour au centre ###
        elif pos[0] <= 0:
            self.canvas.move(self.id, initialx, initialy)
            random.shuffle(starts)
            self.x = starts[0]
            score2()
            reset = 1
        elif pos[2] >= 1000:
            self.canvas.move(self.id, initialx, initialy)
            random.shuffle(starts)
            self.x = starts[0]
            score1()
            reset = 1
        elif reset == 1:
            time.sleep(1)
            reset = 0
        

    def collision(self):
        if (pos[2] > j_pos[0]) and (pos[0] < j_pos[2]) and (pos[3] > j_pos[1]) and (pos[3] < j_pos[3]):
            self.x = -(self.x)
        #print(len(joueur1.find_overlapping(j_pos[0],j_pos[1],j_pos[2],j_pos[3])))
        if (pos[2] > j_pos2[0]) and (pos[0] < j_pos2[2]) and (pos[3] > j_pos2[1]) and (pos[3] < j_pos2[3]):
            self.x = -(self.x)



    ######## Joueur ########
class player1:
    def __init__(self, canvas, color):
        global j_pos, joueur1
        joueur1 = canvas
        self.id = canvas.create_rectangle(10, 10, 30, j_size, fill = color)
        joueur1.move(self.id, 10, 250)
        joueur1_height = joueur1.winfo_height()
        joueur1_width = joueur1.winfo_width()
        j_pos = (1,1,1,1)
    
        
        def Up(haut):
            global j_pos
            v = -5
            haut = v+v
            if j_pos[1] > 0:
                joueur1.move(self.id, 0, haut)
                j_pos = joueur1.coords(self.id)
            
            
        pong.bind("z", Up) # Haut
                
        def Down(bas):
            global j_pos
            v1 = 5
            bas = v1+v1
            if j_pos[1] < 540:
                joueur1.move(self.id, 0, bas)
                j_pos = joueur1.coords(self.id)
            
        pong.bind("s", Down) # Bas


class player2:
    def __init__(self, canvas, color):
        global j_pos2, joueur2
        joueur2 = canvas
        self.id = canvas.create_rectangle(10, 10, 30, j_size, fill = color)
        joueur2.move(self.id, 955, 250)
        joueur2_height = joueur2.winfo_height()
        joueur2_width = joueur2.winfo_width()
        j_pos2 = (1,1,1,1)
    
        
        def Up(haut):
            global j_pos2
            v = -5
            haut = v+v
            if j_pos2[1] > 0:
                joueur2.move(self.id, 0, haut)
                j_pos2 = joueur2.coords(self.id)
            
            
        pong.bind("<Up>", Up) # Haut
                
        def Down(bas):
            global j_pos2
            v1 = 5
            bas = v1+v1
            if j_pos2[1] < 540:
                joueur2.move(self.id, 0, bas)
                j_pos2 = joueur2.coords(self.id)
            
        pong.bind("<Down>", Down) # Bas
        



    ######## Paramètres ########
def param():
    pong.withdraw() # Réduit
    def rejouer():
        param.destroy() # Détruit
        pong.deiconify() # Remet la fenetre pong

    param = Toplevel()

    # bmenu = Button(param, text = 'Menu', command=menu)
    # bmenu.pack(side =BOTTOM)
    bparam = Label(param, text='Paramètres', bg='black', fg='Grey', font=pmenu)
    bparam.pack()

    taille = Label(param, text="Choisissez la taille des Joueurs: (petit, moyen, grand)", bg="black", fg="white")
    taille.place(x="10", y="60")
    s_j = StringVar()
    size_j = Entry(param, textvariable=s_j).place(x="30", y="80")
    def t_config():
        global j_size
        test = s_j.get()
        if test == "petit":
            j_size = 120
        if test == "moyen":
            j_size = 140
        if test == "grand":
            j_size == 160
    
    coloration = Label(param, text="Leurs couleurs: (blanc, bleu, vert) ", bg="black", fg="white")
    coloration.place(x="10", y="110")
    c_j = StringVar()
    color_j = Entry(param, textvariable=c_j).place(x="30", y="130")
    def c_config():
        global j_color
        test = c_j.get()
        if test == "blanc":
            j_color = "white"
        if test == "bleu":
            j_color = "blue"
        if test == "vert":
            j_color = "green"


    param.title("Paramètres by Tibiscuit")
    param.configure(background="black")
    param.resizable(0,0)
    param.geometry("300x400")
    param.update()

    save = Button(param, text="Sauvegarder les réglages", command=t_config)
    save.pack(side = BOTTOM)
    retour = Button(param, text='Reprendre', command=rejouer)
    retour.pack(side = BOTTOM)


    ######## Score ########
def score1():
    global point1
    point1 += 1
    sc1.config(text=point1)

def score2():
    global point2
    point2 += 1
    sc2.config(text=point2)

    ######## Temps ########
def timer_label(temps):
    def time():
        global timer
        timer += 1
        temps.config(text=str(timer)+"s.")
        temps.after(1000, time)
    time()



    ######## Fenetre De Jeu ########
    
Bparam = Button(pong, text="Paramètres", command=param)
Bparam.pack(padx=10)
temps = Label(pong, font=pmenu, bg="black", fg="white")
temps.pack()
timer_label(temps)
sc1 = Label(pong, text="0", font=pmenu, bg="#0B3042")
sc1.place(x="400", y="80")
sc2 = Label(pong,text="0", font=pmenu, bg="#0B3042")
sc2.place(x="575", y="80")

pong.title("Pong by Tibiscuit")
pong.configure(background="black")
pong.resizable(0,0)
img = PhotoImage(file='fond.png')
fenetre.create_image(Largeur/2, Hauteur/2, image=img)
fenetre.pack()
pong.update()

balle = Balle(fenetre, "red")
j1 = player1(fenetre, j_color)
j2 = player2(fenetre, j_color)

while 1:
    balle.mouvement()
    balle.collision()
    pong.update_idletasks()
    pong.update()
    time.sleep(0.01)

pong.mainloop()
