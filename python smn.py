from datetime import datetime
import json
import sys
from pathlib import Path
from Analisis_SMN import parsear_fecha_hora, leer_observaciones, separar_viento, cantidad_ciudades, cantidad_ciudades_completas 
def directorio():
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
def procesar(ruta_txt):
    print("Archivo del smn, convirtiendo a json.....")   
    diccionario= leer_observaciones(ruta_txt)
    directorio= Path("obs_json")
    directorio.mkdir(parents= True, exist_ok= True)
    salida= directorio / f"{Path(ruta_txt).stem}.json"
    with open(salida, "w", encoding="utf-8") as salida:
        json.dump(diccionario, salida, indent= 4, ensure_ascii= False)
    print("Calculando la cantidad de ciudades.....")
    cantidad= cantidad_ciudades(diccionario)
    completas= cantidad_ciudades_completas(diccionario)
    print(f"Hay {cantidad} ciudades en el archivo {Path(ruta_txt).name}")
    print(f"Hay {completas} ciudades con observaciones completas en el archivo {Path(ruta_txt).name}")
def procesar_json(ruta_json):
    print("Archivo del smn, leyendo json.....")
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        cargados= json.load(archivo)
    print("Calculando la cantidad de ciudades.....")
    cantidad= cantidad_ciudades(cargados)
    completas= cantidad_ciudades_completas(cargados)
    print(f"Hay {cantidad} ciudades en el archivo {Path(ruta_json).name}")
    print(f"Hay {completas} ciudades con observaciones completas en el archivo {Path(ruta_json).name}")    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        directorio()
    elif len(sys.argv) == 2:
        ruta= sys.argv[1]
        if ruta.endswith(".txt"):
            procesar(ruta)
        elif ruta.endswith(".json"):
            procesar_json(ruta)
    else:
        print("Al parecer alguien ingreso más de un parametro...., muy mal, maxi te juzga desde el espacio, si a vos, pillín,  por pillín voy a mandar a scooby-doo a que te coma toda la comida de tu casa, pillín")
        print(".............")
        print("chau pillín, nos vemos pillín")