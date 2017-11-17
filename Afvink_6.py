# Naam: Janne Knuiman
# Datum: 25 - 10 - 2017
# Versie:1


# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

#aanroepen verschillende functies
#input: zoekwoord intypen om te zoeken
#output: dna of niet van de seq, of het enzym er we of niet in knipt

def main():
    gevonden = False
    while gevonden == False:
        naam = input("Geef naam bestand: ")
        try:
            lees_inhoud(naam)
            gevonden = True
        except FileNotFoundError:
            print ("Oeps! Dit bestand is niet gevonden!")
        except FileNotFoundError:
            print ("Oeps! Dit bestand is niet gevonden!")
        except:
            print ("Oeps! Een onbekende fout, raadpleeg systeembeheerder!")

    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
    
    headers, seq = lees_inhoud(naam) 
    
    
    x = 0
    while x == 0:
        zoekwoord = input("Geef een zoekwoord op: ")
        for regel in headers:
            if zoekwoord in regel:
                print (regel)
                print (seq[x])
                print ("Dit is dna", is_dna(seq[x]))
                print ("Knipt", knipt(seq[x]))
                x += 1
        if x == 0:
            print ("Sorry! Zoekwoord niet gevonden!")
        
   # schrijf hier de rest van de code nodig om de aanroepen te doen

#lees de inhoud van het bestand
#input: lege lijsten
#output: gevulde lijsten met gesplitste data
    
    
def lees_inhoud(naam):

    bestand = open(naam, "r")
    headers = []
    seq = []
    dna = ""
    
    for regel in bestand: #voor elke regel in het bestand
        if ">" in regel:
            headers.append(regel.strip()) #toevoegen aan de lijst met headers
            dna += " "
        else:
            seq.append(regel.strip())
            regel = regel.replace("\n", "")
            dna += regel
       
   

    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """
     
    return headers, seq #geeft terug naar main

    
def is_dna(seq):
    dna = False
    for item in seq:
        if item == "A" or item == "T" or item == "C" or item == "G":
            dna = True
    return dna #geeft terug naar main



    """
    Deze functie bepaald of de sequentie (een element uit seq) DNA is.
    return headers, seqs
    
def is_dna(seq):
   
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """

#zoekt in de seq naar het matchende enzym
#input: lege lijst
#output: True or False dna
    

def knipt(seq):
    #zoek in seq naar een enzym
    bestand = open("enzymen.txt")


    #Maak een lijst van de enzymen
    #file = bestand.readlines()
    #letter = "*"
    lijst = []



    #Verglijk het bestand met de sequentie
    for line in bestand:
        
        line = line.replace("^" ,"")

        lijst.append(line.split())
        
    #print (lijst)
    knipt = False
    for item in lijst:

        if item[1] in seq:
            #index = seq.index(item[1], 10)
            #index -= 1        
            #print (item[0], " Knipt op positie: ",index +1)
            #print (40*"-")
            #print (seq)
            #print (" "*index, item[1])
            knipt = True

    return knipt
#geeft terug naar main()

main()
