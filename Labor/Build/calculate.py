# Modul für die Berechnungen
import os
from tkinter import messagebox as mBox
from datetime import date


class save_data():
    def __init__(self, name, korn, info):
        self.name = name
        self.info = info
        self.data = korn
        file, x = self.test_file()
        if x != 0:
            Daten = [date.today()]
            for Data in self.info:
                Daten.append(Data)
            for Data in self.data:
                Daten.append(Data.get())
            for Eintrag in Daten:
                file.write(str(Eintrag)+"\n")
            file.close()

    def test_file(self):
        x = 1
        if os.path.isfile("storage/"+str(self.name)+".txt"):
            mBox.showinfo("", "Die Datei existiert bereits!")
            x = 0
            file = None
            return file, x
        else:
            file = open("storage/"+str(self.name)+".txt", "w")
            return file, x


class calculate_data():
    def __init__(self, name):
        self.name = name
        file = open("storage/"+str(self.name)+".txt", "r")
        with open("storage/"+str(self.name)+".txt", "r") as file:
            data_raw = file.read().splitlines()
        self.data = []
        for data in data_raw:
            try:
                dataf = float(data)
                self.data.append(dataf)
            except ValueError:
                self.data.append(data)
        self.Einwaage_feucht = [self.data[12], self.data[27], self.data[36],
                                self.data[45], self.data[53]]
        self.Einwaage_trocken = [self.data[13], self.data[28], self.data[37],
                                 self.data[46], self.data[54]]
        self.Eigenfeuchte = []
        self.Eigenfeuchte.append(self.data[12]-self.data[13])
        self.Eigenfeuchte.append(self.data[27]-self.data[28])
        self.Eigenfeuchte.append(self.data[36]-self.data[37])
        self.Eigenfeuchte.append(self.data[45]-self.data[46])
        self.Eigenfeuchte.append(self.data[53]-self.data[54])
        self.Eigenfeuchte_p = []
        for p in range(len(self.Eigenfeuchte)):
            try:
                self.Eigenfeuchte_p.append((self.Eigenfeuchte[p]/self.Einwaage_trocken[p])*100)
            except ZeroDivisionError:
                self.Eigenfeuchte_p.append(0)
        # Hier sind alle Einträge mit berechneten für den Ertrag
        self.Eingabe_Ertrag = []
        for Ertrag in range(14, 27):
            self.Eingabe_Ertrag.append(self.data[Ertrag])
        self.Eingabe_Ertrag.append(self.Einwaage_trocken[0]-sum(self.Eingabe_Ertrag))
        self.Eingabe_Ertrag_p = self.make_percent_sum(self.Eingabe_Ertrag, self.Einwaage_trocken[0])
        # Hier sind alle Einträge mit berechneten für den Sand
        self.Eingabe_Sand = []
        for Ertrag in range(29, 36):
            self.Eingabe_Sand.append(self.data[Ertrag])
        self.Eingabe_Sand.append(self.Einwaage_trocken[1]-sum(self.Eingabe_Sand))
        self.Eingabe_Sand_p = self.make_percent_sum(self.Eingabe_Sand, self.Einwaage_trocken[1])
        # Hier sind alle Einträge mit berechneten für den Sand gewaschen
        self.Eingabe_Sand_w = []
        for Ertrag in range(38, 45):
            self.Eingabe_Sand_w.append(self.data[Ertrag])
        self.Eingabe_Sand_w.append(self.Einwaage_trocken[2]-sum(self.Eingabe_Sand_w))
        self.Eingabe_Sand_w_p = self.make_percent_sum(self.Eingabe_Sand_w, self.Einwaage_trocken[2])
        # Hier sind alle Einträge mit berechneten für den Rücklauf 4/16
        self.Eingabe_4_16 = []
        for Ertrag in range(47, 53):
            self.Eingabe_4_16.append(self.data[Ertrag])
        self.Eingabe_4_16.append(self.Einwaage_trocken[3]-sum(self.Eingabe_4_16))
        self.Eingabe_4_16_p = self.make_percent_sum(self.Eingabe_4_16, self.Einwaage_trocken[3])
        # Hier sind alle Einträge mit berechneten für den Rücklauf 16/32
        self.Eingabe_16_32 = []
        for Ertrag in range(55, len(self.data)):
            self.Eingabe_16_32.append(self.data[Ertrag])
        self.Eingabe_16_32.append(self.Einwaage_trocken[4]-sum(self.Eingabe_16_32))
        self.Eingabe_16_32_p = self.make_percent_sum(self.Eingabe_16_32, self.Einwaage_trocken[4])

    def make_percent_sum(self, liste, einwaage):
        self.liste = liste.copy()
        self.prozent = []
        for n in range(len(self.liste)):
            try:
                self.prozent.append((sum(self.liste)/einwaage)*100)
            except ZeroDivisionError:
                self.prozent.append(0)
            self.liste.pop(0)
        return self.prozent
