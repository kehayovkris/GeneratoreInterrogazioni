#librerie interne
from Generatore import Generatore
from Classe import Class

#librerie esterne
from colorama import Fore
from colorama import Style


print(Style.BRIGHT + Fore.GREEN + " « Programmatore di interrogazioni » ")
print(Fore.WHITE + "[?] Usa 'help' per una lista di comandi, __classe 4F inf default", Fore.WHITE)

gener = Generatore(Class.QUARTA_F)
ase=True
while ase:
    choice = input(Fore.WHITE + f"{'4F' if gener.classe() == Class.QUARTA_F else '4MI'} > ").split(" ")
    if choice[0] == "help":
        print(Fore.CYAN + Style.BRIGHT +
             "help:" + Style.NORMAL + " Fa vedere i comandi disponibili\n" + Style.BRIGHT +
             "extract:" + Style.NORMAL + " Estrae uno studente dalla __classe selezionata\n" + Style.BRIGHT +
             "list:" + Style.NORMAL + " Mostra tutti gli studenti della __classe selezionata\n" + Style.BRIGHT +
             "f:" + Style.NORMAL + " Cambia a quarta F\n" + Style.BRIGHT +
             "mi:" + Style.NORMAL + " Cambia a quarta MI\n" + Style.BRIGHT +
             "q:"  + Style.NORMAL + " Esce dal programma")
    elif choice[0] == "extract":
        gener.tab().clear()
        gener.genera()
    elif choice[0] == "mi":
        gener = Generatore(Class.QUARTA_MI)
    elif choice[0] == "f":
        gener = Generatore(Class.QUARTA_F)
    elif choice[0] == "list":
        print(gener.l())
    elif choice[0] == "q":
        ase = False
    else:
        print(Fore.RED + Style.BRIGHT + f"ma tutt'aapost???\n   cos pensavi di fare con \"{choice}\" \n" + Fore.YELLOW + "ma ce la fai")