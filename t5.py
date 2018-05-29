import os
import subprocess

import config


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def mem ():
    output = subprocess.run("free | grep -i mem | awk \'{ print $3 \" \"$4 }\'", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    t2 = list(output.stdout.split(' '))

    cor_utilizada = color.BOLD

    if ( int(t2[1]) < config.mem_conf ):
        cor_utilizada = color.RED

    print (color.BOLD+'Memoria utilizada: {}\t\tMemoria Livre: {}'.format(t2[0],cor_utilizada+t2[1])+color.END)

def dsk ():
   disco = os.system('df -h')
   print (disco)


opcao = 1
while (opcao != 0):

   os.system('clear')
   print ("--------- MENU ----------")
   print (" 1 - Uso memoria")
   print (" 2 - Uso disco")
   print ("")
   opcao = int(input ("Opcao[0=Fim]: "))

   print ('')

   if ( opcao == 1 ):
        mem() 
   elif (opcao == 2):
        dsk()

   wait = input("Pressione qualquer tecla")

fo = open("config", "r")

##for line in fo:
##    print (line)

##print (fo.readlines())
##print (fo.read())


data = fo.readlines()

for line in data:
    words = line.split()

    if ( words[0] == 'mem_conf'):
        print (words[1])

fo.close()
