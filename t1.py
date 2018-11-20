import subprocess

output = subprocess.run("free -h | grep -i mem | awk \'{ print $3 \" \"$4 }\'", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
##t2 = list(output.stdout.split(' '))
##print ('Memoria utilizada: {}\t\tMemoria Livre: {}'.format(t2[0],t2[1]))

print (output.stdout)
