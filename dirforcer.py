import requests 
import time
import argparse
import random 

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

colors = [Green,Blue,Grey,Red]

arg = argparse.ArgumentParser(description="Herramienta para hacer buscar directorios de una pagina web")

arg.add_argument("-d",dest="domain",help='Pon un dominio para buscar sus directorios',required=True)
arg.add_argument("-w",dest="wordlist",help='Agrega una wordlist para hacer la FuerzaBruta',required=True)
args = arg.parse_args()
url = args.domain 
directory = open(args.wordlist, "r")

print(random.choice(colors) + "DirForcer" + Reset)

print(Blue + "Target : "+ args.domain + Reset)

for i in directory.readlines():
    req = requests.get(url+ "/" + i.strip())
    if req.status_code == 200:
        print(Green + "Directorio encontrado :"+ url + "/" + i.strip() + "\nStatusCode : "+ str(req.status_code) + Reset)
    else:
        print(Red + "No existe : "+ url + "/" + i.strip() + "\nStatusCode : "+ str(req.status_code) + Reset)


