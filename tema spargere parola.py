import hashlib
import sys
import time


HASH_TINTA = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"



def calculeaza_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()



LITERE_MARI = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIFRE = "0123456789"
CARACTERE_SPECIALE = "!@#$"
LITERE_MICI = "abcdefghijklmnopqrstuvwxyz"


cerinte = {"mari": 1, "cifre": 1, "speciale": 1, "mici": 3}
lungime_maxima = 6


numar_apeluri = 0
gasit = False
inceput = time.time()


# Determină categoria unui caracter
def tip_caracter(c):
    if c in LITERE_MARI:
        return "mari"
    elif c in CIFRE:
        return "cifre"
    elif c in CARACTERE_SPECIALE:
        return "speciale"
    elif c in LITERE_MICI:
        return "mici"
    return None



def genereaza(cuvant, cnt_mari, cnt_cifre, cnt_speciale, cnt_mici):
    global numar_apeluri, gasit, inceput
    numar_apeluri += 1

    if numar_apeluri % 1000000 == 0:
        durata = time.time() - inceput
        print(f"Candidați generați: {numar_apeluri}, timp scurs: {durata:.2f} secunde")

    if gasit:
        return

    if len(cuvant) == lungime_maxima:
        if (cnt_mari == cerinte["mari"] and
                cnt_cifre == cerinte["cifre"] and
                cnt_speciale == cerinte["speciale"] and
                cnt_mici == cerinte["mici"]):

            hash_obtinut = calculeaza_hash(cuvant)
            if hash_obtinut == HASH_TINTA:
                print("Parola a fost descoperită:", cuvant)
                print("Total apeluri recursivitate:", numar_apeluri)
                gasit = True
                sys.exit(0)
        return

    pozitii_ramase = lungime_maxima - len(cuvant)
    ramase_mari = cerinte["mari"] - cnt_mari
    ramase_cifre = cerinte["cifre"] - cnt_cifre
    ramase_speciale = cerinte["speciale"] - cnt_speciale
    ramase_mici = cerinte["mici"] - cnt_mici

    if (ramase_mari + ramase_cifre + ramase_speciale + ramase_mici) > pozitii_ramase:
        return

    for caracter in (LITERE_MARI + CIFRE + CARACTERE_SPECIALE + LITERE_MICI):
        tip = tip_caracter(caracter)
        nou_mari = cnt_mari + (tip == "mari")
        nou_cifre = cnt_cifre + (tip == "cifre")
        nou_speciale = cnt_speciale + (tip == "speciale")
        nou_mici = cnt_mici + (tip == "mici")

        if (nou_mari > cerinte["mari"] or
                nou_cifre > cerinte["cifre"] or
                nou_speciale > cerinte["speciale"] or
                nou_mici > cerinte["mici"]):
            continue

        genereaza(cuvant + caracter, nou_mari, nou_cifre, nou_speciale, nou_mici)

        if gasit:
            return



genereaza("", 0, 0, 0, 0)
print("Parola nu a fost identificată.")