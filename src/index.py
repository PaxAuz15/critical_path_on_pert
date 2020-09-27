from criticalpath import Node

g = globals()

def crear_variables(numero, cadena='var',lista_valores=None,inicio=1):
    fin=inicio+numero
    for i,j in enumerate(range(inicio,fin)):
        if lista_valores:
            valor=lista_valores[i]
        else:
            valor=None
        g[cadena+str(j)]=valor


print(f'PROGRAMA PARA CALCULAR LA RUTA CRITICA Y LA DURACION DE UN PROYECTO',
        'UTILIZANDO EL METODO PERT')

entrada = None

mensaje_de_ayuda='ESTE VALOR DEBE SER UN NUMERO ENTERO POSITIVO'
espacio="\n"
p = Node('project')
incorrecto="El valor ingresado no es el correcto"

while True:
    try:
        print(espacio)
        print('¿Cuántos nodos contiene el problema?')
        entrada = int(input())
        print(espacio)
        if entrada > 0:
            print(f"Excelente. El",entrada,"es un valor entero positivo.")
            break
        else:
            print("El número de nodos a ingresar no puede ser negativo o cero")
            print(f"TE RECUERDO QUE",mensaje_de_ayuda)
            print(espacio)
            print("Un consejo... SE ACEPTAN SOLO VALORES ENTEROS POSITIVOS")
            continue
    except:
        print(espacio)
        if type(entrada) != int:
            print(f"Revise que sea un entero positivo.",incorrecto)
            print(f"TE RECUERDO QUE",mensaje_de_ayuda)
            print(espacio)
            continue
print(espacio)

cant_nodos = int(entrada)
cant_nodos_mensajes = int(entrada)
contador = 0

identificadores_nodos = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

duracion = []

nodos = []

while cant_nodos > 0 and cant_nodos < 26:
    try:
        print(espacio)
        print(f"Agregar la duración para el Nodo",
                identificadores_nodos[contador])
        entrada = input()
        print(espacio)
        if int(entrada) >= 0:
            print(f"Excelente. El",entrada,"Si es un valor correcto")
            duracion.append(entrada)
            nodos.append(p.add(Node(identificadores_nodos[contador],entrada)))
            cant_nodos -= 1
            contador += 1

        else:
            print(incorrecto,f"Es un valor negativo")
            print(espacio)
            print("AYUDA:")
            print("Te recuerdo que se aceptan valores enteros positivos")
    except:
        print(espacio)
        if type(entrada) != (int):
            print("El valor ingresado no es el correcto")
        continue

print(duracion)
print(nodos)
respuestas = ['Y','y','yes','YES','N','n','no','NO']
print(espacio)
print('Desea agregar conexiones de nodos?')
entrada_respuesta = input()
contador_dos = 0
tupla = tuple()
links =[]

while entrada_respuesta == respuestas[0] or entrada_respuesta == respuestas[1] or entrada_respuesta == respuestas[2] or entrada_respuesta == respuestas[3]:
    try:
        print(espacio)
        print(f'Agregar la conexion #',contador_dos)
        origen=input('Origen:')
        destino=input('Destino:')
        tupla = (origen,destino)
        links.append(tupla)
        print(espacio)
        print('Desea agregar mas conexiones de nodos?')
        entrada_respuesta = input()
    except:
        print('Se acaba el programa')

print(links)


#a = p.add(Node('A', duration=14))
#b = p.add(Node('B', duration=20))
#c = p.add(Node('C', duration=3))
#d = p.add(Node('D',duration=20))
#e = p.add(Node('E', duration=8))
#f = p.add(Node('F', duration=11))
#g = p.add(Node('G', duration=13))
#h = p.add(Node('H', duration=20))

#   links = [(a,d), (a,b), (b,c), (d,g), (c,g), (c,e), (d,e), (e,f), (g,h), (f,h)]

#for link in links:
#    p.link(*link)

#p.update_all()

#print(p.get_critical_path())
#print(p.duration)
