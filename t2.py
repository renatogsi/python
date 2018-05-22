import subprocess

##p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
p = subprocess.run(['free', '-h', '|', 'grep', '-i', 'mem', '|', 'awk', ' \'', '{', 'print', '$3', '$4', '}', '\'], stdout=subprocess.PIPE)
print (p)
