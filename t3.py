
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
