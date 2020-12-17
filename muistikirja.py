import time
import pickle

def tallenna(tallennettava):
    tiedosto = open("muistio.dat","wb")
    pickle.dump(tallennettava,tiedosto)
    tiedosto.close()

def lue():
    try:
        tiedosto = open("muistio.dat", "rb")
        luettu = pickle.load(tiedosto)
        tiedosto.close()
        return luettu
    except Exception:
        tiedosto = open("muistio.dat","wb")
        tiedosto.close()
        
def main():

    while True:
        #Valikko
        print("""(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta""")
        #Pyydetään käyttäjän syöte
        try:
            syote = input("Mitä haluat tehdä?: ")
        except Exception:
            print("Virheellinen valinta")
        

        #Syötteen mukainen toiminta
        if syote == "1":
            #luetaan muistikirjan sisältö listaan "sisalto"
            sisalto = lue()
            print(sisalto)
            continue
        
        elif syote == "2":
            #luetaan muistikirjan sisältö listaan "sisalto"
            sisalto = lue()
            lisattava = input("Kirjoita uusi merkintä: ") + ":::" + time.strftime("%X %x") 
            sisalto.append(lisattava)
            try:
                tallenna(sisalto)
            except Exception:
                print("Virheellinen valinta")
            continue
        
        elif syote == "3":
            sisalto = lue()
            print("Listalla on",len(sisalto),"merkintää.")
            muutettava = input("Mitä niistä muutetaan?:")
            #Tulostetaan muutettava teksti
            print(sisalto[int(muutettava)])
            #Otetaan uusi teksti
            uusi_teksti = input("Anna uusi teksti:") + ":::" + time.strftime("%X %x") 
            #Lisätään uusi teksti annetulle paikalle
            sisalto.insert(int(muutettava),uusi_teksti)
            #Poistetaan vanha teksti paikalta +1
            sisalto.pop(int(muutettava)+1)
            try:
                tallenna(sisalto)
            except Exception:
                print("Virheellinen valinta")
            continue
        
        elif syote == "4":
            sisalto = lue()
            print("Listalla on",len(sisalto),"merkintää.")
            poistettava = input("Mitä niistä poistetaan?:")
            print("Poistettiin merkintä", sisalto[int(poistettava)])
            sisalto.pop(int(poistettava))
            try:
                tallenna(sisalto)
            except Exception:
                print("Virheellinen valinta")
            continue   
        
        elif syote == "5":
            print("Lopetetaan.")
            break

    
if __name__ == "__main__":
    main()
    
