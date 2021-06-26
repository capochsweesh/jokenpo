import random
from time import sleep
import os

def main():

    listajogo = ["Pedra", "Papel", "Tesoura"]

    print("""
    Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura""")
    escolha = int(input('Qual a sua jogada? '))
    
    #tesoura >>> papel
    #pedra >>> tesoura
    #papel >>> pedra
    pcEscolha = random.randint(0,len(listajogo)-1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-='*10)
    print('Computador jogou {}'.format(listajogo[pcEscolha]))
    print('Jogador jogou {}'.format(listajogo[escolha]))
    print('-='*10)
    
    if pcEscolha == escolha:
        print('\033[4;36mEMPATE\033[m')
    elif escolha == 0 and pcEscolha == 2 or escolha == 1 and pcEscolha == 0 or escolha == 2 and pcEscolha == 1:
        print('\033[4;32mJOGADOR VENCE!\033[m')
    else:
        print('\033[4;31mCOMPUTADOR VENCE!\033[m')
    


if __name__ == "__main__":
    while True:
        main()


