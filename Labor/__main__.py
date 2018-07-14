#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from Build import *
from datetime import date
from tkinter import messagebox as mBox


class OOP():

    def __init__(self):

        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title("Kieswerk Oberbrunn Labor")
        # statisch
        self.win.resizable(0, 0)
        # Schriftgrößen
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(size=14)
        # Brecheroptionen
        Texteintrag(self.win, 'Brecheroptionen:', 0, 0)
        self.Schleudertisch = Auswahlkasten(self.win, 'Schleudertisch:',
                                            0, 1, ('5', '4'))
        self.Schleuderplatten = Auswahlkasten(self.win, 'Schleuderplatten:',
                                              0, 2, ("QCA102", "QCA064"))
        self.Motor = Auswahlkasten(self.win, 'Motorauslastung:', 0, 3,
                                   ('Volllast', 'Halblast'))
        self.Testgeschwindigkeit = EingabeZahl(self.win, 'Testgeschwindigkeit',
                                               0, 4)
        # Aufgaben
        self.Aufgabe = UAuswahlkasten(self.win, 'Aufgabe:', 2, 0,
                                      ("16-32_gebrochen", "16-32_rund",
                                       "16-32_gemischt"))
        Texteintrag(self.win, 'Aufgabenmenge:', 3, 0)
        self.AufgabenM = EingabeZahl(self.win, 'Masse pro Meter:', 3, 1)
        self.AufgabenV = EingabeZahl(self.win, 'Bandgeschwindigkeit:', 3, 2)
        Texteintrag(self.win, 'Ertrag Brecher', 3, 3)
        self.BrecherErtragM = EingabeZahl(self.win, 'Masse pro Meter:', 3, 4)
        self.BrecherErtragV = EingabeZahl(self.win, 'Bandgeschwindigkeit:', 3, 5)
        # Zeitlinge Angaben
        Texteintrag(self.win, 'Datum:', 5, 0)
        self.datum = date.today()
        Texteintrag(self.win, self.datum, 5, 1)
        self.Probennummer = UEingabeZahl(self.win, 'Probennummer:', 5, 2)
        self.Uhrzeit = UEingabeString(self.win, 'Uhrzeit:', 5, 4)
        # EingabeFeld für Sieblinie
        Texteintrag(self.win, 'Sieblinien Eingabe:', 1, 6)
        # Korneingabe hinzufügen
        self.KornEingabe = Korn_Eingabe(self.win, 3, 1)
        self.KornEingabe.create('Ertrag 0/32', [">32", "22-32", "16-22", "11-16", "8-11",
                                                "5.6-8", "4-5.6", "2-4", "1-2", "0,5-1",
                                                "0,25-0,5", "0,125-0,25", "0,063-0,125"])
        self.KornEingabe.create('Sand 0/4', [">4", "2-4", "1-2", "0,5-1",
                                             "0,25-0,5", "0,125-0,25", "0,063-0,125"])
        self.KornEingabe.create('Sand 0/4w', [">4", "2-4", "1-2", "0,5-1",
                                              "0,25-0,5", "0,125-0,25", "0,063-0,125"])
        self.KornEingabe.create('Kies 4/16', [">16", "11-16", "8-11",
                                              "5.6-8", "4-5.6", "<4"])
        self.KornEingabe.create('Kies 16/32', [">32", "22-32", "16-22", "<16"])
        Dict = self.KornEingabe.__dict__
        self.KornData = Dict['data']

        # Check für die Erstellung der Sieblinien
        # als Ausfwahlmöglichkeit

        self.check_Ertrag = Check(self.win, 'Ertrag 0/32', 0, 8)
        self.check_Sand = Check(self.win, 'Sand 0/4', 1, 8)
        self.check_Sand_w = Check(self.win, 'Sand gewaschen 0/4', 2, 8)
        self.check_4_16 = Check(self.win, 'Rücklauf 4/16', 3, 8)
        self.check_16_32 = Check(self.win, 'Rücklauf 16/32', 4, 8)

        self.Siebline = ttk.Button(self.win, text='Siebline erstellen',
                                   command=self.create_file)
        self.Siebline.grid(column=4, row=7)

    def create_file(self):
        if self.Testgeschwindigkeit.get() < 45:
            mBox.showinfo('', 'Testgeschwindigkeit zu niedrig!')
        elif self.Testgeschwindigkeit.get() > 70:
            mBox.showinfo('', 'Testgeschwindigkeit zu hoch!')
        else:
            if self.check_Ertrag.get() == 1 and self.KornData[1].get() == 0:
                mBox.showinfo('', 'Keine Einwaage für Ertrag 0/32!')
            elif self.check_Sand.get() == 1 and self.KornData[16].get() == 0:
                mBox.showinfo('', 'Keine Einwaage für Sand 0/4!')
            elif self.check_Sand_w.get() == 1 and self.KornData[25].get() == 0:
                mBox.showinfo('', 'Keine Einwaage für Sand 0/4 gewaschen!')
            elif self.check_4_16.get() == 1 and self.KornData[34].get() == 0:
                mBox.showinfo('', 'Keine Einwaage für Rücklauf 4/16!')
            elif self.check_16_32.get() == 1 and self.KornData[42].get() == 0:
                mBox.showinfo('', 'Keine Einwaage für Rücklauf 16/32!')
            elif self.check_Ertrag.get() + self.check_Sand.get() +\
                    self.check_Sand_w.get() + self.check_4_16.get() +\
                    self.check_16_32.get() == 0:
                mBox.showinfo('', 'Sieblinie auswählen!')
            else:
                self.name = str(date.today())+"_"+self.Schleudertisch.get() +\
                    "_"+self.Schleuderplatten.get()+"_" +\
                    str(self.Testgeschwindigkeit.get()) +\
                    "_"+self.Motor.get()+"_"+self.Aufgabe.get()+"_" +\
                    self.Uhrzeit.get()+"_"+str(self.Probennummer.get())
                self.Einstellungen = []
                self.Einstellungen.append(self.Uhrzeit.get())
                self.Einstellungen.append(self.Probennummer.get())
                self.Einstellungen.append(self.Aufgabe.get())
                self.Einstellungen.append(self.AufgabenM.get())
                self.Einstellungen.append(self.AufgabenM.get())
                self.Einstellungen.append(self.BrecherErtragM.get())
                self.Einstellungen.append(self.BrecherErtragM.get())
                self.Einstellungen.append(self.Schleudertisch.get())
                self.Einstellungen.append(self.Schleuderplatten.get())
                self.Einstellungen.append(self.Motor.get())
                self.Einstellungen.append(self.Testgeschwindigkeit.get())
                save_data(self.name, self.KornData, self.Einstellungen)
                self.Daten = calculate_data(self.name)
                Dict = self.Daten.__dict__
                self.Eingabe_Ertrag_p = Dict['Eingabe_Ertrag_p']
                self.Eingabe_Sand_p = Dict['Eingabe_Sand_p']
                self.Eingabe_Sand_w_p = Dict['Eingabe_Sand_w_p']
                self.Eingabe_4_16_p = Dict['Eingabe_4_16_p']
                self.Eingabe_16_32_p = Dict['Eingabe_16_32_p']
                self.checklist = [self.check_Ertrag.get(), self.check_Sand.get(),
                                  self.check_Sand_w.get(), self.check_4_16.get(),
                                  self.check_16_32.get()]
                self.graflist = [self.Eingabe_Ertrag_p, self.Eingabe_Sand_p,
                                 self.Eingabe_Sand_w_p, self.Eingabe_4_16_p,
                                 self.Eingabe_16_32_p]
                create_plot(self.name, self.checklist, self.graflist)
                create_pdf_file(self.name, self.Einstellungen, Dict, self.checklist)

            # =====================
            # Start GUI
            # =====================


oop = OOP()
oop.win.mainloop()
