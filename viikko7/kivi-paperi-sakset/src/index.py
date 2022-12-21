from peli import Peli
from pelaaja import Pelaaja
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = None
        match vastaus:
            case "a":
                peli = Peli(Pelaaja())
            case "b":
                peli = Peli(Tekoaly(), True)
            case "c":
                peli = Peli(TekoalyParannettu(), True)
            case _:
                break
        peli.pelaa()

if __name__ == "__main__":
    main()
