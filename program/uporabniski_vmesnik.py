from moja_denarnica import *

import tkinter as tk

denarnica = nalozi_denarnico()

class Vstopna_stran:

    def __init__(self, okno):

        self.okno = okno
        self.okno.title('Moja denarnica')

        self.gumb_1 = tk.Button(okno, text = 'Kupi izdelek', command = self.kupi_izdelek, width = 25).grid(row = 0, column = 0)
        self.gumb_2 = tk.Button(okno, text = 'Plačaj položnico', command = self.placaj_poloznico, width = 25).grid(row = 0, column = 1)
        self.gumb_3 = tk.Button(okno, text = 'Prihodek', command = self.prihodek, width = 25).grid(row = 1, column = 0)
        self.gumb_4 = tk.Button(okno, text = 'Izpis prihodkov in dohodkov' , command = self.izpis_prihodkov_in_dohodkov, width = 25).grid(row = 1, column = 1)
        self.gumb_5 = tk.Button(okno, text = 'Izpis porabe na izdelek', command = self.poraba_na_izdelek, width = 25).grid(row = 2, column = 0)
        self.gumb_6 = tk.Button(okno, text = 'Izpis količine na izdelek', command = self.kolicina_izdelka, width = 25).grid(row = 2, column = 1)
        self.gumb_7 = tk.Button(okno, text = 'Posodobi stanje', command = self.posodobi_stanje, width = 25).grid(row = 3, column = 0)

    
    def kupi_izdelek(self):
        novo_okno = tk.Toplevel(self.okno)
        stran = Kupujem(novo_okno)

    def placaj_poloznico(self):
        novo_okno = tk.Toplevel(self.okno)
        stran = Poloznica(novo_okno)

    def prihodek(self):
        novo_okno = tk.Toplevel(self.okno)
        stran = Prihodki(novo_okno)

    def izpis_prihodkov_in_dohodkov(self):
        novo_okno = tk.Toplevel(self.okno)
        stran = Izpis(novo_okno)

    def poraba_na_izdelek(self):
        novo_okno = tk.Toplevel(self.okno)
        stran = Poraba(novo_okno)

    def kolicina_izdelka(self):
        novo_okno = tk.Toplevel(self.okno)
        stran = Kolicina(novo_okno)

    def posodobi_stanje(self):
        self.label = tk.Label(self.okno, text = '{} €'.format(denarnica.stanje)).grid(row = 3, column = 1)
        

class Kupujem:

    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Kupujem izdelek')
        
        self.izdelek = tk.StringVar()
        self.cena = tk.DoubleVar()
        self.kolicina = tk.IntVar()
        
        self.label_1 = tk.Label(okno, text = 'Vpiši ime izdelka:').grid(row = 0, column = 0)
        self.vhod_1 = tk.Entry(okno, width = 20, textvariable = self.izdelek).grid(row = 0, column = 1)
        
        self.label_2 = tk.Label(okno, text = 'Vpiši ceno izdelka:').grid(row = 1, column = 0)
        self.vhod_2 = tk.Entry(okno, width = 20, textvariable = self.cena).grid(row = 1, column = 1)
        
        self.label_3 = tk.Label(okno, text = 'Vpiši kolicino izdelkov:').grid(row = 2, column = 0)
        self.vhod_3 = tk.Entry(okno, width = 20, textvariable = self.kolicina).grid(row = 2, column = 1)
    
        self.gumb_kupi = tk.Button(okno, text = 'KUPI', command = self.kupi, width = 10).grid(row = 3, column = 1)

        self.gumb_nazaj = tk.Button(okno, text = 'NAZAJ', command = self.nazaj, width = 10).grid(row = 3, column = 2)

        
    def nazaj(self):
        self.okno.destroy()

    def kupi(self):
        self.label_4 = tk.Label(self.okno, text = denarnica.kupi_izdelek(self.izdelek.get(), self.cena.get(), self.kolicina.get())).grid(row = 4, column = 1)
        shrani_denarnico(denarnica)
        
class Poloznica:
    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Plačujem položnico')

        self.namen = tk.StringVar()
        self.znesek = tk.DoubleVar()

        self.label_1 = tk.Label(okno, text = 'Vpiši namen položnice:').grid(row = 0, column = 0)
        self.vhod_1 = tk.Entry(okno, width = 20, textvariable = self.namen).grid(row = 0, column = 1)
        
        self.label_2= tk.Label(okno, text = 'Vpiši znesek položnice:').grid(row = 1, column = 0)
        self.vhod_2 = tk.Entry(okno, width = 20, textvariable = self.znesek).grid(row = 1, column = 1)

        self.gumb_placaj = tk.Button(okno, text = 'PLAČAJ', command = self.placaj, width = 10).grid(row = 2, column = 1)

        self.gumb_nazaj = tk.Button(self.okno, text = 'NAZAJ', command = self.nazaj, width = 10).grid(row = 2, column = 2)
        
    def nazaj(self):
        self.okno.destroy()
                       
    def placaj(self):
        self.label_3 = tk.Label(self.okno, text = denarnica.placaj_poloznico(self.namen.get(), self.znesek.get())).grid(row = 4, column = 1)
        shrani_denarnico(denarnica)
        
class Prihodki:
    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Dobil sem prihodek')

        self.opis = tk.StringVar()
        self.velikost = tk.DoubleVar()

        self.label_1 = tk.Label(okno, text = 'Vpiši opis prihodka:').grid(row = 0, column = 0)
        self.vhod_1 = tk.Entry(okno, width = 20, textvariable = self.opis).grid(row = 0, column = 1)
        
        self.Label_2 = tk.Label(okno, text = 'Vpiši velikost prihodka:').grid(row = 1, column = 0)
        self.vhod_2 = tk.Entry(okno, width = 20, textvariable = self.velikost).grid(row = 1, column = 1)

        self.gumb_prihodek = tk.Button(okno, text = 'SHRANI PRIHODEK', command = self.shrani_prihodek).grid(row = 2, column = 1)

        self.gumb_nazaj = tk.Button(self.okno, text = 'NAZAJ', command = self.nazaj, width = 10).grid(row = 2, column = 2)

    def nazaj(self):
        self.okno.destroy()
                       
    def shrani_prihodek(self):
        self.label_3 = tk.Label(self.okno, text = denarnica.prihodek(self.opis.get(), self.velikost.get())).grid(row = 4, column = 2)
        shrani_denarnico(denarnica)

class Poraba:
    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Koliko porabim na izdelek')

        self.izdelek = tk.StringVar()

        self.label = tk.Label(okno, text = 'Vpiši ime izdelka:').grid(row = 0, column = 0)
        self.vhod = tk.Entry(okno, width = 20, textvariable = self.izdelek).grid(row = 0, column = 1)
         
        self.gumb_poraba = tk.Button(okno, text = 'POKAŽI PORABO NA IZDELEK', command = self.pokazi_porabo).grid(row = 2, column = 1)

        self.gumb_nazaj = tk.Button(self.okno, text = 'NAZAJ', command = self.nazaj, width = 10).grid(row = 2, column = 2)
        
    def nazaj(self):
        self.okno.destroy()

    def pokazi_porabo(self):
        self.label_4 = tk.Label(self.okno, text = denarnica.poraba_na_izdelek(self.izdelek.get())).grid(row = 4, column = 2)
        shrani_denarnico(denarnica)


class Kolicina:
    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Koliko izdelka sem kupil')

        self.izdelek = tk.StringVar()

        self.label = tk.Label(okno, text = 'Vpiši ime izdelka:').grid(row = 0, column = 0)
        self.vhod = tk.Entry(okno, width = 20, textvariable = self.izdelek).grid(row = 0, column = 1)
         
        self.gumb_kolicina = tk.Button(okno, text = 'POKAŽI KOLIČINO IZDELKOV', command = self.pokazi_kolicino).grid(row = 1, column = 1)

        self.gumb_nazaj = tk.Button(self.okno, text = 'NAZAJ', command = self.nazaj, width = 10).grid(row = 1, column = 2)

    def nazaj(self):
        self.okno.destroy()
                           
    def pokazi_kolicino(self):
        self.label_4 = tk.Label(self.okno, text = denarnica.kolicina_na_izdelek(self.izdelek.get())).grid(row = 4, column = 2)
        shrani_denarnico(denarnica)

        
class Izpis:
    def __init__(self, okno):
        self.okno = okno
        self.okno.title('Izpis prihodkov in dohodkov')

        self.label = tk.Label(okno, text = izpis_prihodkov_in_dohodkov()).grid(row = 1, column = 0)

        self.gumb_nazaj = tk.Button(self.okno, text = 'NAZAJ', command = self.nazaj, width = 10).grid(row = 0, column = 0)        

    def nazaj(self):
        self.okno.destroy()



def zaganjac():
    okno = tk.Tk()
    dobrodoslica = Vstopna_stran(okno)
    okno.mainloop()
    
zaganjac()
