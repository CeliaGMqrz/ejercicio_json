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

#3. Cuenta cuantas de las escuelas infantiles tiene de servicios la "Educación de 0 a 3 años". Y las lista si el usuario lo indica.

def cuenta_servicio(doc):
    escuelas = []
    for escuela in doc["@graph"]:
        if "Educación de 0 a 3 años" in escuela["organization"]["services"]:
            escuelas.append(escuela["title"])
    return escuelas

#4. Esta función recibe por teclado un servicio extra que pueda dar la escuela 
#(Comedor, Horario ampliado, Educación de 0 a 3 años) y muestra el nombre de la escuela y dirección que tengan ese servicio.

def filtrar_escuelas_servicios(doc,servicio):
    escuelas = []
    direcciones = []
    for escuela in doc["@graph"]:
        if servicio in escuela["organization"]["services"]:
            escuelas.append(escuela["title"])
            direcciones.append(escuela["address"]["street-address"])
    filtro = [escuelas,direcciones]
    return filtro

#5. Esta función recibe un parámetro que es un código postal y muestra el nombre de la escuela y su dirección.

def informacion_relacionada(doc,cp):
    escuelas = []
    direcciones = []
    for escuela in doc["@graph"]:
        if cp in escuela["address"]["postal-code"]:
            escuelas.append(escuela["title"])
            direcciones.append(escuela["address"]["street-address"])
    filtro = [escuelas,direcciones]
    return filtro

#MENU
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

    #Muestra el numero total de escualas con el servicio de educacion de 0 a 3 años. Y lista las escuelas que son si el usuario lo pide.
    elif opcion == "3":
        print("Hay ",len(cuenta_servicio(doc))," escuelas con el servicio de Educación de 0 a 3 años.")
        respuesta = input("¿Quieres saber cuáles son? (S/N): ")
        print()
        if respuesta.upper() == "S":
            for escuela in cuenta_servicio(doc):
                print(escuela)
            limpiar_pantalla_continuar()
        elif respuesta.upper() == "N":
            print("Ok")
            limpiar_pantalla_continuar()
        else:
            print("Valor erróneo.")
            limpiar_pantalla_continuar()

    #Muestra las escuelas y su direccion segun el tipo de servicios ofrecidos
    elif opcion == "4":
        print()
        
        servicios = []
        for i in doc["@graph"]:
            servicios.append(i["organization"]["services"])
        print("Servicios extra registrados:")
        print("-Comedor\n-Horario ampliado\n-Educación de 0 a 3 años")
        print()
        servicio = input("Introduce el servicio deseado:")
        servicio = servicio.capitalize()
        while servicio not in ('Comedor','Horario ampliado','Educación de 0 a 3 años'):
            print("Servicio no registrádo ó no válido.")
            print("\nServicios extra registrados:")
            print("-Comedor\n-Horario ampliado\n-Educación de 0 a 3 años")
            print()
            servicio = input("\nIntroduce el servicio deseado:")
            servicio = servicio.capitalize()

        for escuela,direccion in zip (filtrar_escuelas_servicios(doc,servicio)[0],filtrar_escuelas_servicios(doc,servicio)[1]):
            print("\nESCUELA: ",escuela,"\nDIRECCION: ",direccion)
            
        limpiar_pantalla_continuar()
        
    #Introduciendo un codigo postal muestra las escuelas que hay en ese municipio con su direccion.
    elif opcion == "5":
        cps=[]
        for i in doc["@graph"]:
            cps.append(i["address"]["postal-code"])

        cp = input("Introduce un codigo postal: ")
        #validar cp
        while cp not in cps:
            print("Error. Codigo postal no válido.")
            respuesta= input("¿Desea ver la lista de codigos postales?.(S/N)")
            print()
            if respuesta.upper() == "S":
                for i in set(cps): 
                    print(i)
                cp = input("Introduce un codigo postal: ")
                
            elif respuesta.upper() == "N":
                print("Ok")
                cp = input("Introduce un codigo postal: ")
            else:
                print("Valor erróneo.")
                continue

        for escuela,direccion in zip (informacion_relacionada(doc,cp)[0],informacion_relacionada(doc,cp)[1]):
            print("\nESCUELA: ",escuela,"\nDIRECCIÓN: ",direccion)
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
