import IKT_modul1

def zzz ():
    nev = input("Adja meg az új képlet nevét: ")
    if nev == "":
        keplet = 1
        return keplet
    eredmeny = input("Adja meg a kiszámolni kívánt érték jelét: ")
    if eredmeny == "":
        keplet = 1
        return keplet
    megyseg = input("Adja meg a kiszámolni kívánt érték mértékegységét: ")
    if megyseg == "":
        keplet = 1
        return keplet
    valtszam = input("Adja meg a változók számát: ")
    if valtszam == "":
        keplet = 1
        return keplet
    valtozok = []
    valtozokmegyseg = []


    while type(valtszam) != int:
        try:
            valtszam = int(valtszam)
            break

        except ValueError:
            print("Rossz adatot adott meg! Próbálja újra")
            valtszam = input("Adja meg a változók számát: ")

    for i in range(valtszam):
        valt = input("Adja meg a következő változó jelét: ")
        valtmegyseg = input("Adja meg a változó mértékegységét: ")
        valtozokmegyseg.append(valtmegyseg)
        valtozok.append(valt)

    ujkeplet = input("Adja meg a képletet: ")
    ujtag = open("IKT_modul1.py", "a")
    ujtag.write("\n\n\ndef " + nev + " (")
    db = 0
    for i in range(len(valtozok)):
        ujtag.write(valtozok[db])
        if db + 1 < len(valtozok):
            ujtag.write(", ")
        db += 1
    ujtag.write("):\n")
    ujtag.write("    " + ujkeplet + "\n")
    ujtag.write("    return " + eredmeny + "\n")
    ujtag.close()


    kepletek = dir(IKT_modul1)
    szam = str(len(kepletek) - 7)
    szamlalo = len(kepletek) - 2
    ujhiv = open("IKT_main.py", "a", encoding="UTF8")
    while szamlalo < len(kepletek):
        ujhiv.write("\n                elif keplet == " + szam + ":\n"
                    + "                    " + valtozok[0] + " = int(input(" + chr(34) + chr(92) + "nAdja meg " + valtozok[0] + " értékét ("
                    + valtozokmegyseg[0] + "): " + chr(34) + "))\n"
                    + "                    " + valtozok[1] + " = int(input(" + chr(34) + "Adja meg " + valtozok[1] + " értékét ("
                    + valtozokmegyseg[1] + "): " + chr(34) + "))\n"
                    + "                    " + eredmeny + " = IKT_modul1." + nev + "(" + valtozok[0] + ", " + valtozok[1] + ")\n"
                    + "                    " + "print(" + chr(34) + "A sebesség (" + eredmeny + "):" + chr(34) + ", round(" + eredmeny + ", 4), " + chr(34) + megyseg + chr(34) + ")")
        szamlalo += 1
        if szamlalo < len(kepletek):
            break

'''
pl.:

elif keplet == 9:
    s = int(input("\nAdja meg s értékét (m): "))
    t = int(input("Adja meg t értékét (s): "))
    v = IKT_modul1.sebesseg(s, t)
    print("A sebesség (v):", round(v, 4), "m/s")'''