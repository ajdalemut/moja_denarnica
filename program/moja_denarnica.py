import datetime
        
class Denarnica:
    
    def __init__(self, stanje = 0):
        self.stanje = stanje
        self.slovar = {}
        
    def __repr__(self):
        return 'Denarnica(stanje = {})'.format(self.stanje)

    def __str__(self):
        return 'Denarnica z {}€ '.format(self.stanje)

    def dodaj_v_slovar(self, ime_izdelka, cena, kolicina):
        if self.slovar.get(ime_izdelka) == None :
            self.slovar[ime_izdelka] = [kolicina * cena, kolicina]
        else:
            self.slovar[ime_izdelka][0] += kolicina * cena
            self.slovar[ime_izdelka][1] += kolicina

    def kupi_izdelek(self, ime_izdelka, cena, kolicina):
        if ime_izdelka == '':
            return 'Ups, prišlo je do napake, ime izdelka mora vsebovati vsaj en znak.'
        elif cena <= 0 or kolicina <= 0:
            return 'Ups, prišlo je do napake, cena in količina morata biti večji od 0.'
        elif kolicina * cena > self.stanje:
            return 'Žal nimate dovolj denarja za ta nakup!'
        else:
            self.stanje -= kolicina * cena
            x = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            self.dodaj_v_slovar(ime_izdelka, cena, kolicina)
            with open('denarnica.txt', 'a') as dat:
                print(ime_izdelka, '-' +  str(kolicina * cena) + '€', x, sep = ', ', file = dat)
            return 'Izdelek ste uspešno kupili.'

    def placaj_poloznico(self, namen_poloznice, znesek):
        if namen_poloznice == '':
            return 'Ups, prišlo je do napake, namen položnice mora vsebovati vsaj en znak.'
        elif znesek <= 0:
            return 'Ups, prišlo je do napake, znesek položnice mora biti večji od 0 €.'
        elif znesek > self.stanje:
            return 'Ups, te položnice pa ne morete plačati!'
        else:
            self.stanje -= znesek
            x = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            self.dodaj_v_slovar(namen_poloznice, znesek, 1)
            with open('denarnica.txt', 'a') as dat:
                print(namen_poloznice, '-' +  str(znesek) + '€', x, sep = ', ', file = dat)
            return 'Položnico ste uspešno plačali.'
        
    def prihodek(self, opis_prihodka, velikost_prihodka):
        if opis_prihodka == '':
            return 'Ups, prišlo je do napake, opis prihodka mora vsebovati vsaj en znak.'
        elif velikost_prihodka <= 0:
            return 'Ups, prišlo je do napake, velikost prihodka mora biti večja od 0 €.'
        self.stanje += velikost_prihodka
        x = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        with open('denarnica.txt', 'a') as dat:
            print(opis_prihodka,'+' + str(velikost_prihodka) + '€', x, sep = ', ', file = dat)
        return 'Vaše stanje se je povišalo na {}€'.format(self.stanje)

    def poraba_na_izdelek(self, ime_izdelka):
        if self.slovar.get(ime_izdelka) == None:
            return 'Tega izdelka še niste kupili.'
        else:
            return 'Za ta izdelek ste porabili {} €.'.format(self.slovar[ime_izdelka][0])

    def kolicina_na_izdelek(self, ime_izdelka):
        if self.slovar.get(ime_izdelka) == None:
            return 'Tega izdelka še niste kupili.'
        else:
            return 'Kupili ste {} izdelkov.'. format(self.slovar[ime_izdelka][1])

def izpis_prihodkov_in_dohodkov():
    izpis = ''
    with open('denarnica.txt') as dat:
        for vrstica in dat:
            izpis += vrstica
    return izpis
        

import pickle

def shrani_denarnico(denarnica):
    '''shrani podatke denarnice za prihodno uporabo'''
    with open('denarnice_podatki.pkl', 'wb') as output:
        pickle.dump(denarnica,output)
    
def nalozi_denarnico():
    '''nalozi podatke denarnice od predhodnje uporabe'''
    with open('denarnice_podatki.pkl', 'rb') as input:
        denarnica = pickle.load(input)
    return denarnica




        


