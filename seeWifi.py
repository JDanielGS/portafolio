#!/bin/python3
#se importa la libreria subprocess
import subprocess

#se obtiene la metadata correspondiente de las contraseñas de wifi
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

#Se decodifica los metadatos
data = meta_data.decode('utf-8', errors='backslashreplace')

#se dividen los datos linea por linea
data = data.split('\n')

#Se crean una lista con los perfiles correspondientes
profiles = []

#se realiza la compilacion de todos los datos
for i in data:
    
    #Encontrar 'All User Profile' en cada item
    if 'All User Profile' in i:
        #Si se encuentra
        #Se divide el item
        i = i.split(":")
        
        #EL item en el index se agrega un 1 que será el nombre del wifi
        i = i[1]
        
        #se formate el nombre
        #el primer y el ultimo caractér son menos usados
        i = i[1:-1]
        
        #Se agregan los nombres del wifi a la lista
        profiles.append(i)
        
        #Se imprime las cabecera
        print("{:<30}| {:<}".format("Wifi Name", "Password"))
        print("----------------------------------------------")
        
        #Se realiza una conexion con los perfiles
        
        for i in profiles:
            
            #Se comienza con el bloque try catch
            #bloque de try
            try:
                #Se consiguen los metadatos con la contraseña usando el nombre del wifi
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])
                
                #Decodificando y dividiendo la linea de datos linea por linea
                results = results.decode('utf-8', errors='backslashreplace')
                results = results.split('\n')
                
                #Se encuentra la contraseña de desde la lista de resultados
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                
                "si es una contraseña será impresa dicha contraseña"
                try:
                    print("{:<30}| {:<}".format(i, results[0]))
                except IndexError:
                    print("{:<30}| {:<}".format(i, ""))
            #Se llama este proceso cuando todo haya fallado
            except subprocess.CalledProcessError:
                print("Encoding Error Ocurred")