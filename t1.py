import subprocess

output = subprocess.run("free -h | grep -i mem | awk \'{ print $3 \" \"$4 }\'", shell=True, stdout=subprocess.PIPE, universal_newlines=True)
print (output.stdout)
print ("xxxxx")
delimiter = ' '
output.split(delimiter)
