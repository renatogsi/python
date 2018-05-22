import os

def mem ():
   memoria = os.system('free -h | grep -i mem | awk \'{ print $3,$4 }\'')
   print (memoria)
   return

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

   if ( opcao == 1 ):
        mem() 
   elif (opcao == 2):
        dsk()

   wait = input("Pressione qualquer tecla")
