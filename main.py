class Biblioteka:
    limit_wypozyczen = 20
    egzemplarze = []
    czytelnicy = []
    
    def dostepne_egz(self, tytul):
        dostepne_egz = []
        for egzemplarz in self.egzemplarze:
            if egzemplarz.tytul == tytul:
                if egzemplarz.wypozyczony == False:
                    dostepne_egz.append(egzemplarz)
        return dostepne_egz
    
    def wypozycz(self, nazwisko, tytul):
        czytelnik_w_bazie = False

        for czytelnik in self.czytelnicy:
            if czytelnik.nazwisko == nazwisko:
                czytelnik_w_bazie = czytelnik
        
        if czytelnik_w_bazie == False:
            czytelnik_w_bazie = Czytelnik(nazwisko,[])
            self.czytelnicy.append(czytelnik_w_bazie)
        
        if len(czytelnik_w_bazie.lista_wypozyczen) == self.limit_wypozyczen:
            return False

        for egzemplarz in self.egzemplarze:
            if egzemplarz.tytul == tytul:
                if egzemplarz.wypozyczony == nazwisko:
                    return False

        for egzemplarz in self.dostepne_egz(tytul):
            czytelnik_w_bazie.lista_wypozyczen.append(egzemplarz)
            egzemplarz.wypozyczony = nazwisko
            return True
        
        return False

    def oddaj(self, nazwisko, tytul):
        czytelnik_w_bazie = False

        for czytelnik in self.czytelnicy:
            if czytelnik.nazwisko == nazwisko:
                czytelnik_w_bazie = czytelnik
        
        if czytelnik_w_bazie == False:
            return False

        for egzemplarz in self.egzemplarze:
            if egzemplarz.tytul == tytul and egzemplarz.wypozyczony == nazwisko:
                czytelnik_w_bazie.lista_wypozyczen.remove(egzemplarz)
                egzemplarz.wypozyczony = False
                return True
        
        return False

    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):
        self.egzemplarze.append(Egzemplarz(tytul, autor, rok_wydania, False))

        return True

class Czytelnik:
    def __init__(self, nazwisko, lista_wypozyczen):
        self.nazwisko = nazwisko
        self.lista_wypozyczen = lista_wypozyczen

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz:
    def __init__(self, tytul, autor, rok_wydania, wypozyczony):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony

liczba_akcji = int(input())
lista_akcji = [input() for akcja in range(liczba_akcji)]
biblioteka = Biblioteka()

for akcja in lista_akcji:
    dzialania = akcja.replace(' ', '').replace('(', '').replace(')', '').replace('"', '').replace('\'', '').split(",")
    dzialanie = dzialania[0]
    if dzialanie == 'dodaj':
        print(biblioteka.dodaj_egzemplarz_ksiazki(dzialania[1],dzialania[2],dzialania[3]))
    if dzialanie == 'oddaj':
        print(biblioteka.oddaj(dzialania[1],dzialania[2]))
    if dzialanie == 'wypozycz':
        print(biblioteka.wypozycz(dzialania[1],dzialania[2]))
