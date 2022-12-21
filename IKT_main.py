import IKT_modul1
import uj_keplet

lehetosegek = 1

while lehetosegek != 0:
    if lehetosegek == 1:
        lehetosegek = int(input("\nLehetőségek:\n\n"
                           "0 - kilépés\n"
                           "1 - Lehetőségek\n"
                           "2 - új képlet hozzáadása\n"
                           "3 - elérhető képletek\n"
                           "\nVálasszon a menüpontokból: "))

    if lehetosegek == 2:
        if uj_keplet.zzz() == 1:
            lehetosegek = 1

    if lehetosegek == 3:
        print("\nAz elérhető képletek:\n"
              "\n\t 1 - Vissza a lehetőségekhez")
        kepletek = dir(IKT_modul1)
        kepszam = 8
        while kepszam <= len(kepletek):
            if kepletek[kepszam] != "zzz":
                print("\t",kepszam - 6,"-", kepletek[kepszam])
                if kepszam + 1 < len(kepletek):
                    kepszam += 1
                else:
                    break
            else:
                keplet = int(input("\nVálasszon képletet: "))
                if keplet == 1:
                    lehetosegek = 1
                    break
                elif keplet == 9:
                    s = int(input("\nAdja meg s értékét (m): "))
                    t = int(input("Adja meg t értékét (s): "))
                    v = IKT_modul1.sebesseg(s, t)
                    print("A sebesség (v):", round(v, 4), "m/s")