
def config( parametro ):
    fo = open("config", "r")
    data = fo.readlines()

    print (parametro)

    for line in data:
        words = line.split()

        if ( words[0] == parametro ):
            print (words[1])
            valor = words[1]

    fo.close()
    return valor;


config( 'mem_conf' )
print (valor)


config( 'mem_conf1' )
print (valor)

config( 'mem_conf2' )
print (valor)

