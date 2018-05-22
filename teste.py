import os

m1 = str(os.system('free -h | grep -i mem | awk \'{ print $3" "$4 }\''))
delimiter = ' '
memoria = m1.split(delimiter)
print (m1)
print (memoria)

import subprocess

output = subprocess.run("free -h | grep -i mem | awk \'{ print $3 \" \"$4 }\'", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
print (output.stdout)
delimiter = ' '
output.split(delimiter)
