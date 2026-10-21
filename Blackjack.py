import os 
import random
kártyaszám = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bubi", "Dáma", "Király", "Ász",]
kártyaszín = ["Kőr", "Káró", "Treff", "Pikk",]
def kártyagen(szám,szín):
    random.shuffle(szám)
    random.shuffle(szín)
    kártya = (szín[0], szám[0])
    return kártya

def pontozó(pakli):
    pont = 0
    for kártya in pakli:
        if kártya[1] in ["Bubi", "Dáma", "Király", "Ász"]:
            pont += 10
        elif kártya == "---------":
            pass
        else:
            pont += int(kártya[1])
    return pont

def display(jpakli, opakli,jpenz,openz,fogadas):
    os.system("cls")
    print(f"""
    A játékos kártyái:
        {jpakli}
        Összesen:{pontozó(jpakli)}
    A osztó kártyái:
        {opakli}
        Összesen:{pontozó(opakli)}

        Játékos pénze: {jpenz} | Osztó pénze: {openz} | Fel tett összeg: {fogadas}
    """)
Játékos_pont = 0
Osztó_pont = 0
kezdés = True
kilep = False
openz = 1000
jpenz = 1000      
print("BLACKJACK")
input("Nyomj bármit a kezdéshez!")
os.system("cls")
while True:
    if jpenz > 0 and openz > 0:
        if kilep == False:
            if kezdés == True:
                while True:
                    print(f"Ennyi pénzed van: {jpenz}")
                    fogadas = int(input("Mennyit teszel fel:"))
                    if fogadas > jpenz or fogadas > openz:
                        os.system("cls")
                        print("Nincs ennyi pénz")
                    else:
                        break
                Játékos_pakli = []
                Osztó_pakli = []
                kosztó_pakli = ["---------"]
                for i in range(2):
                    Játékos_pakli.append(kártyagen(kártyaszám,kártyaszín))
                    Osztó_pakli.append(kártyagen(kártyaszám,kártyaszín))
                kezdés = False
                kosztó_pakli.insert(0,Osztó_pakli[0])
            else:
                display(Játékos_pakli,kosztó_pakli,jpenz,openz,fogadas)
                while True:
                    Játékos_pont = pontozó(Játékos_pakli)
                    if Játékos_pont>=21:
                        break
                    else:
                        state = input("Kér vagy megáll? ")
                        if state.upper() == "KÉR":
                            Játékos_pakli.append(kártyagen(kártyaszám,kártyaszín))
                            display(Játékos_pakli,kosztó_pakli,jpenz,openz,fogadas)
                        elif state.upper() == "MEGÁLL":
                            break
                        else:
                            print("Hibás parancs.")
                while True:
                    Osztó_pont = pontozó(Osztó_pakli)
                    if Játékos_pont > 21:
                        break
                    else:  
                        if Osztó_pont < 17:
                            Osztó_pakli.append(kártyagen(kártyaszám,kártyaszín))
                            display(Játékos_pakli,Osztó_pakli,jpenz,openz,fogadas)
                        else:
                            break
                if 21>=Játékos_pont>Osztó_pont or Osztó_pont > 21:
                    print("Győztél!")
                    jpenz += fogadas
                    openz -= fogadas
                elif 21>=Osztó_pont>Játékos_pont or Játékos_pont > 21   :
                    print("Vesztettél!")
                    jpenz -= fogadas
                    openz += fogadas
                else:
                    print("Döntetlen")
                kezdés = True
                while True:
                    ujra = input("Szeretnél újra játszani?(I/N) ")
                    if ujra.upper() == "I":
                        break
                    elif ujra.upper() == "N":
                        kilep = True
                        break
                    else:
                        print("Hibás parancs!")
        else:
            break
    else:
        if jpenz == 0:
            print("Elfogyott a pénzed!")
            break
        elif openz == 0:
            print("Az osztó pénze elfogyott!")
            break
print("Köszönjük a játékot!")







