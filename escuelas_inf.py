import json
import os
with open ('escuelas_infantiles_madrid.json','r') as fichero:
    doc=json.load(fichero)

#FUNCIONES

# Limpiar pantalla

def limpiar_pantalla_continuar():
	continuar = input("...\npulsa Enter para continuar")

#1. Listar(basico): Esta función listará el nombre de todas las escuelas infantiles de madrid.

def listar_escuelas(doc):
    escuelas = []
    for escuela in doc["@graph"]:
        escuelas.append(escuela["title"])
    return escuelas

#2. Lista el nombre "title" de todas las escuelas infantiles y además muestra la dirección "street-address", el código postal "postal-code" y 
# la localidad "locality".

def listar_escuelas_direccion(doc):
    escuelas = []
    calles = []
    cps = []
    localidades = []
    for escuela in doc["@graph"]:
        escuelas.append(escuela["title"])
        calles.append(escuela["address"]["street-address"])
        cps.append(escuela["address"]["postal-code"])
        localidades.append(escuela["address"]["locality"])
    filtro = [escuelas,calles,cps,localidades]
    return filtro
#3. Cuenta cuantas de las escuelas infantiles tiene de servicios la "Educación de 0 a 3 años".

def cuenta_servicio(doc):
    escuelas = []
    for escuela in doc["@graph"]:
        if "Educación de 0 a 3 años" in escuela["organization"]["services"]:
            escuelas.append(escuela["title"])
    return escuelas

while True:
    os.system('clear')
    print ()
    print ("______________________ESCUELAS INFANTILES______________________")
    print()
    print("1. Lista todas las escuelas infantiles de Madrid.")
    print("2. Lista el nombre, direccion, cp y localidad de todas las escuelas infantiles.")
    print("3. Muestra el número de escuelas infantiles que tiene servicio de 0 a 3 años.")
    print("4. Introduce un servicio extra y muestra las escuelas que ofrecen ese servicio.")
    print("5. Introduce el codigo postal y muestra el nombre de la escuela y su dirección")
    print("6. Introduce el nombre de la escuela y muestra el nombre de organización y los servicios que ofrece.")
    print(" Para salir introduzca: 'exit' ")
    print()
    opcion = input("Introduce la opción deseada: ")

    #Listar nombre de escuelas
    if opcion == "1":   
        for escuela in listar_escuelas(doc):
            print(escuela)
        # Tambien muestra cuantas escuelas hay en total
        print()
        print("Hay en total: ",len(listar_escuelas(doc))," escuelas.")
        limpiar_pantalla_continuar()
    
    #Listar escuelas con direccion
    elif opcion == "2":
        for t,d,cp,loc in zip (listar_escuelas_direccion(doc)[0],listar_escuelas_direccion(doc)[1],listar_escuelas_direccion(doc)[2],listar_escuelas_direccion(doc)[3]):
            print ("\nNOMBRE:",t,"\nDIRECCION:",d,"\nCP:",cp,"\nLOCALIDAD:",loc)
        
        limpiar_pantalla_continuar()

    elif opcion == "3":
        print("Hay ",len(cuenta_servicio(doc))," escuelas con el servicio de Educación de 0 a 3 años.")
        respuesta = input("¿Quieres saber cuáles son? (S/N): ")
        print()
        if respuesta.upper() == "S":
            for escuela in cuenta_servicio(doc):
                print(escuela)
            limpiar_pantalla_continuar()
        elif respuesta.upper() == "N":
            limpiar_pantalla_continuar()
        else:
            print("Valor erróneo.")
            limpiar_pantalla_continuar()


    elif opcion == "4":
        None
        limpiar_pantalla_continuar()

    elif opcion == "5":
        None
        limpiar_pantalla_continuar()

    elif opcion == "6":
        None
        limpiar_pantalla_continuar()

    elif opcion == "exit":
        print("Programa terminado.")
        break
    else:
        print("Valor erróneo")
        limpiar_pantalla_continuar()
