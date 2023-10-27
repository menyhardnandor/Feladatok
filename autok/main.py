class Adatok():
    def __init__(self, orszag:str,rendszam:str,meropont:str,tipus:str,sebesseg:int,ido:str)-> None:
        self.orszag = orszag
        self.rendszam = rendszam
        self.meropont = meropont
        self.tipus = tipus
        self.sebesseg = sebesseg
        self.ido = ido


sokasag: list[Adatok] = []
    

with open ("D22.txt","r") as f: 
    act = None

    running = True

    while running:
        act = f.readline()
    

        if act == "":
            running = False
            continue

        act = act.split(",")

        if act[1].endswith("\n"): act[1] = act[1][0:len(act[1])-1]

        (Adatok(str(act[0]),str(act[1]),str(act[2]),str(act[3]),int(act[4]),str(act[5])))


print(act)