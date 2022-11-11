# -*- coding: utf-8 -*-
"""

Esegue la precedente versione di Monkey



"""
import random
frase = "methinks it is like a wease"
alphabet = "abcdefghijklmnopqrstuvwxyz "


def monkey(stringa):
    s = ''                              # stringa temporanea
    c = 0
    for x, y in zip(stringa, frase):    # loop sui caratteri 
        if x == y:
            s += x                      # aggiorna la stringa
            c += 1
        else:
            s += random.choice(alphabet)# o inserisce un carattere a caso
    return s, c

def probability(c):
    percentuale = c / 27 * 100 
    return percentuale
    
def main():
    tentativo = 0
    count = 0
    stringa = '-' * 27
    percentuale = 0
    for i in range(1000):
        stringa, count = monkey(stringa)
        percentuale = probability(count)
        tentativo += 1
        if int(percentuale) == 100:
            break
    print('Monkey ha scritto \"'+ stringa +'\" al '+ str(tentativo) +'° tentativo')

for i in range(100):
    main()
