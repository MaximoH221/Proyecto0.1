from datetime import datetime
import json
import sys
from pathlib import Path
from Analisis_SMN import parsear_fecha_hora, leer_observaciones, separar_viento
if len(sys.argv) ==1:
    print("contando los archivos txt en el directorio datos.....")
    datos= Path("datos")
    archivos_txt= list(datos.glob("*.txt"))
    cantidad_txt= len(archivos_txt)
    print(f"Hay {cantidad_txt} archivos txt en el directorio datos")
    obs_json= Path("obs_json")
    if not obs_json.exists():
        print("el directorio obs_json no existe, creandolo.....")
        obs_json.mkdir(parents= True, exist_ok= True)
    else:
        print("al parecer el directorio obs_json ya existe, continuando.....")
        print("contando los archivos json en el directorio obs_json.....")
    obse= Path("obs_json")
    archivos_json= list(obse.glob("*.json"))
    cantidad_json= len(archivos_json)
    print(f"Hay {cantidad_json} archivos json en el directorio obs_json")
elif len(sys.argv) == 2:
    ruta= sys.argv[1]
    if ruta[-4:] == ".txt":
        print("Archivo del smn, convirtiendo a json.....")   
        try: 
            print("Tratando de leer ruta con utf-8.....")
            with open(ruta, "r", encoding= "utf-8") as data: 
                dataso= data.readlines()
        except UnicodeDecodeError:
            print("Tratando de leer ruta con latin-1.....")
            with open(ruta, "r", encoding= "latin-1") as data:
                dataso= data.readlines()
        diccionario_smn= {}
           
else:
    print("Al parecer alguien ingreso más de un parametro...., muy mal, maxi te juzga desde el espacio por haber lanzado más de un parametro....")
    print(".............")
    