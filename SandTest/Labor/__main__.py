#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from datetime import date
import os
from tkinter import messagebox as mBox
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from fpdf import FPDF


class OOP():

    def __init__(self):

        # Create instance
        self.win = tk.Tk()
        # Add a title
        self.win.title("Kieswerk Oberbrunn Labor")
        # statisch
        self.win.resizable(0, 0)
        # Brecheroptionen
        self.brecher = ttk.Label(self.win, text="Brecheroptionen:")
        self.brecher.grid(column=0, row=0)
        # Schleudertisch
        self.brecher1 = ttk.Label(self.win, text="Schleudertisch:")
        self.brecher1.grid(column=0, row=1)
        # Auswahlmöglichkeiten Brecheroptionen Schleudertisch
        self.b1 = tk.StringVar()
        self.brecheroption1 = ttk.Combobox(self.win, width=20,
                                           textvariable=self.b1)
        self.brecheroption1['values'] = ("4", "5")
        self.brecheroption1.grid(column=1, row=1)
        self.brecheroption1.current(0)
        # Schleuderplatten
        self.brecher2 = ttk.Label(self.win, text="Schleuderplatten:")
        self.brecher2.grid(column=0, row=2)
        # Auswahlmöglichkeiten Schleuderplatten
        self.b2 = tk.StringVar()
        self.brecheroption2 = ttk.Combobox(self.win, width=20,
                                           textvariable=self.b2)
        self.brecheroption2['values'] = ("QCA102", "QCA064")
        self.brecheroption2.grid(column=1, row=2)
        self.brecheroption2.current(0)
        # Testgeschwindigkeit
        self.vdouble = tk.DoubleVar()
        self.geschwindigkeit = ttk.Label(self.win, text="Testgeschwindigkeit:")
        self.geschwindigkeit.grid(column=0, row=3)
        # Auswahlmöglichkeiten Testgeschwindigkeit
        self.geschwindigkeit = ttk.Entry(self.win, width=20,
                                         textvariable=self.vdouble)
        self.geschwindigkeit.grid(column=1, row=3)
        # Motor
        self.last = ttk.Label(self.win, text="Motor")
        self.last.grid(column=0, row=4)
        self.motor = tk.StringVar()
        self.motorlast = ttk.Combobox(self.win, width=20,
                                      textvariable=self.motor)
        self.motorlast['values'] = ("Volllast", "Halblast")
        self.motorlast.grid(column=1, row=4)
        self.motorlast.current(0)
        # Aufgabe
        self.aufgabe = ttk.Label(self.win, text="Aufgabe:")
        self.aufgabe.grid(column=2, row=1)
        self.aufstr = tk.StringVar()
        self.aufgabewahl = ttk.Combobox(self.win, width=20,
                                        textvariable=self.aufstr)
        self.aufgabewahl['values'] = ("16-32_gebrochen", "16-32_rund",
                                      "16-32_gemischt")
        self.aufgabewahl.grid(column=2, row=2)
        self.aufgabewahl.current(0)
        self.sieb = ttk.Label(self.win, text="Sieblinie Eingabe:")
        self.sieb.grid(column=1, row=6)

        self.aufgabenmenge = ttk.Label(self.win, text="Aufgabenmenge:")
        self.aufgabenmenge.grid(column=3, row=1)
        self.aufgabebandv1 = tk.DoubleVar()
        self.aufgabemasse1 = tk.IntVar()
        self.aufgabenmenge_eingabe_v = ttk.Entry(self.win, width=20,
                                                 textvariable=self.aufgabebandv1)
        self.aufgabenmenge_eingabe_v.grid(column=4, row=2)
        self.band_v1 = ttk.Label(self.win, text="Bandgeschwindigkeit")
        self.band_v1.grid(column=3, row=2)
        self.aufgabenmenge_eingabe_m = ttk.Entry(self.win, width=20,
                                                 textvariable=self.aufgabemasse1)
        self.aufgabenmenge_eingabe_m.grid(column=4, row=3)
        self.masse_1 = ttk.Label(self.win, text="Masser pro Meter")
        self.masse_1.grid(column=3, row=3)
        self.ertrag_brecher = ttk.Label(self.win, text="Ertrag Brecher:")
        self.ertrag_brecher.grid(column=3, row=4)
        self.aufgabebandv2 = tk.DoubleVar()
        self.aufgabemasse2 = tk.IntVar()
        self.aufgabenmenge_eingabe_v2 = ttk.Entry(self.win, width=20,
                                                  textvariable=self.aufgabebandv1)
        self.aufgabenmenge_eingabe_v2.grid(column=4, row=5)
        self.band_v2 = ttk.Label(self.win, text="Bandgeschwindigkeit")
        self.band_v2.grid(column=3, row=5)
        self.aufgabenmenge_eingabe_m2 = ttk.Entry(self.win, width=20,
                                                  textvariable=self.aufgabemasse1)
        self.aufgabenmenge_eingabe_m2.grid(column=4, row=6)
        self.masse_2 = ttk.Label(self.win, text="Masser pro Meter")
        self.masse_2.grid(column=3, row=6)

        self.datum = date.today()
        self.date_label = ttk.Label(self.win, text="Datum:")
        self.date_label.grid(column=5, row=0)
        self.showdatum = ttk.Label(self.win, text=self.datum)
        self.showdatum.grid(column=5, row=1)
        self.probe = ttk.Label(self.win, text="Probennummer:")
        self.probe.grid(column=5, row=2)
        self.probe_nr = tk.IntVar()
        self.probennummer = ttk.Entry(self.win, width=20,
                                      textvariable=self.probe_nr)
        self.probennummer.grid(column=5, row=3)
        self.probe_zeit = ttk.Label(self.win, text="Probenuhrzeit:")
        self.probe_zeit.grid(column=5, row=4)
        self.probe_t = tk.StringVar()
        self.probenzeit = ttk.Entry(self.win, width=20,
                                    textvariable=self.probe_t)
        self.probenzeit.grid(column=5, row=5)
        self.createWidgets()
        # Button callback
        self.checkVar0_32 = tk.IntVar()
        self.checkVar0_4 = tk.IntVar()
        self.checkVar4_16 = tk.IntVar()
        self.checkVar16_32 = tk.IntVar()
        self.check0_32 = ttk.Checkbutton(self.win, text="0/32 Siebline",
                                         variable=self.checkVar0_32,
                                         onvalue=1, offvalue=0)
        self.check0_4 = ttk.Checkbutton(self.win, text="0/4 Siebline",
                                        variable=self.checkVar0_4,
                                        onvalue=1, offvalue=0)
        self.check4_16 = ttk.Checkbutton(self.win, text="4/16 Sieblinie",
                                         variable=self.checkVar4_16,
                                         onvalue=1, offvalue=0)
        self.check16_32 = ttk.Checkbutton(self.win, text="16/32 Sieblinie",
                                          variable=self.checkVar16_32,
                                          onvalue=1, offvalue=0)
        self.check0_32.grid(column=1, row=7, sticky=tk.W)
        self.check0_4.grid(column=2, row=7, sticky=tk.W)
        self.check4_16.grid(column=3, row=7, sticky=tk.W)
        self.check16_32.grid(column=4, row=7, sticky=tk.W)
        self.create_pdf = ttk.Button(self.win, text="Sieblinie erstellen",
                                     command=self.create_file)
        self.create_pdf.grid(column=5, row=7)

    def test_file(self):
        x = 1
        self.name = str(date.today())+"_"+self.b1.get()+"_"+self.b2.get()+"_" +\
            str(self.vdouble.get())+"_"+self.motor.get()+"_"+self.aufstr.get()+"_" +\
            self.probe_t.get()+"_"+str(self.probe_nr.get())
        if os.path.isfile("storage/"+str(self.name)+".txt"):
            mBox.showinfo("", "Die Datei existiert bereits!")
            x = 0
            file = None
            return file, x
        else:
            file = open("storage/"+str(self.name)+".txt", "w")
            return file, x

    def test_v(self):
        x = 1
        if self.vdouble.get() < 45:
            mBox.showinfo("", "Geschwindigkeit zu niedrig.")
        else:
            x = 0
            return x

    def create_pdf_file(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(65)
        pdf.cell(60, 10, 'Siebanalyse Kieswerk Oberbrunn', 0, 2, 'C')
        pdf.set_font('Arial', '', 10)
        pdf.cell(100)
        pdf.cell(30, 5, 'Datum:', 0, 2, 'R')
        pdf.cell(30, 5, self.data[1], 0, 2, 'R')
        pdf.cell(30, 5, self.data[2], 0, 1, 'R')
        pdf.cell(40, 5, 'Brechereinstellungen:', 1, 0, 'C')
        pdf.cell(98)
        pdf.cell(30, 5, 'Aufgabe:', 1, 1, 'C')
        pdf.cell(30, 5, 'Schleudertisch:', 0, 0, 'R')
        pdf.cell(30, 5, str(self.data[4]), 0, 0, 'L')
        pdf.cell(75)
        pdf.cell(30, 5, self.data[3], 0, 1, 'C')
        pdf.cell(30, 5, 'Schleuderplatten:', 0, 0, 'R')
        pdf.cell(30, 5, self.data[5], 0, 0, 'L')
        pdf.cell(75)
        pdf.cell(30, 5, 'feine Gesteinsart', 0, 1, 'C')
        pdf.cell(30, 5, 'Testgeschwindigkeit:', 0, 0, 'R')
        pdf.cell(30, 5, str(self.data[11]), 0, 0, 'L')
        pdf.cell(75)
        pdf.cell(30, 5, 'Kalkstein', 0, 1, 'C')
        pdf.cell(30, 5, 'Motor:', 0, 0, 'R')
        pdf.cell(30, 5, self.data[6], 0, 1, 'L')
        pdf.cell(10, 5, '', 0, 1)
        pdf.cell(40, 5, 'Aufgabe in [t/h]:', 1, 0, 'C')
        pdf.cell(20, 5, '', 1, 0, 'L')
        pdf.cell(30)
        pdf.cell(40, 5, 'Ertrag Sand in [t/h]:', 1, 0, 'C')
        pdf.cell(20, 5, '', 1, 1, 'L')
        pdf.cell(10, 5, '', 0, 1)
        pdf.cell(30)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(30, 5, 'Ertrag 0/32')
        pdf.cell(30, 5, 'Sand 0/4')
        pdf.cell(30, 5, 'Rücklauf 4/16')
        pdf.cell(30, 5, 'Rücklauf 16/32', 0, 1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(30, 5, 'Einwaage feucht:', 0, 0)
        pdf.cell(20, 5, str(self.data[12])+'g', 1)
        pdf.cell(20, 5)
        pdf.cell(20, 5, str(self.data[30])+'g', 1)
        pdf.cell(20)
        pdf.cell(20, 5, str(self.data[42])+'g', 1)
        pdf.cell(20)
        pdf.cell(20, 5, str(self.data[58])+'g', 1, 1)
        pdf.cell(30, 5, 'Einwaage trocken:', 0, 0)
        pdf.cell(20, 5, str(self.data[13])+'g', 1)
        pdf.cell(20, 5)
        pdf.cell(20, 5, str(self.data[31])+'g', 1)
        pdf.cell(20)
        pdf.cell(20, 5, str(self.data[43])+'g', 1)
        pdf.cell(20)
        pdf.cell(20, 5, str(self.data[59])+'g', 1, 1)
        pdf.cell(30, 5, 'Eigenfeuchte:', 0, 0)
        pdf.cell(20, 5, str(self.data[14])+'g', 1)
        pdf.cell(20, 5, str(self.eigen_p_ertrag)+'%', 1)
        pdf.cell(20, 5, str(self.data[32])+'g', 1)
        pdf.cell(20, 5, str(self.eigen_p_sand)+'%', 1)
        pdf.cell(20, 5, str(self.data[44])+'g', 1)
        pdf.cell(20, 5, str(self.eigen_p_4_16)+'%', 1)
        pdf.cell(20, 5, str(self.data[60])+'g', 1)
        pdf.cell(20, 5, str(self.eigen_p_16_32)+'%', 1, 1)
        pdf.cell(30, 5, 'Kornzusammensetzung in [mm] und [M.%]', 0, 1)
        pdf.cell(30, 5, '>32')
        pdf.cell(20, 5, str(self.data[15])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-14])+'%', 1)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, str(self.data[61])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-14])+'%', 1, 1)
        pdf.cell(30, 5, '22-32')
        pdf.cell(20, 5, str(self.data[16])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-13])+'%', 1)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, str(self.data[62])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-13])+'%', 1, 1)
        pdf.cell(30, 5, '16-22')
        pdf.cell(20, 5, str(self.data[17])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-12])+'%', 1)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, str(self.data[45])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-12])+'%', 1)
        pdf.cell(20, 5, str(self.data[63])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-12])+'%', 1, 1)
        pdf.cell(30, 5, '11-16')
        pdf.cell(20, 5, str(self.data[18])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-11])+'%', 1)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, str(self.data[46])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-11])+'%', 1)
        pdf.cell(20, 5, str(self.data[64])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-11])+'%', 1, 1)
        pdf.cell(30, 5, '8-11')
        pdf.cell(20, 5, str(self.data[19])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-10])+'%', 1)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, str(self.data[47])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-10])+'%', 1)
        pdf.cell(20, 5, str(self.data[65])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-10])+'%', 1, 1)
        pdf.cell(30, 5, '5.6-8')
        pdf.cell(20, 5, str(self.data[20])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-9])+'%', 1)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, '', 0)
        pdf.cell(20, 5, str(self.data[48])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-9])+'%', 1)
        pdf.cell(20, 5, str(self.data[66])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-9])+'%', 1, 1)
        pdf.cell(30, 5, '4-5.6')
        pdf.cell(20, 5, str(self.data[21])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-8])+'%', 1)
        pdf.cell(20, 5, str(self.data[33])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-8])+'%', 1)
        pdf.cell(20, 5, str(self.data[49])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-8])+'%', 1)
        pdf.cell(20, 5, str(self.data[67])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-8])+'%', 1, 1)
        pdf.cell(30, 5, '2-4')
        pdf.cell(20, 5, str(self.data[22])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-7])+'%', 1)
        pdf.cell(20, 5, str(self.data[34])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-7])+'%', 1)
        pdf.cell(20, 5, str(self.data[50])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-7])+'%', 1)
        pdf.cell(20, 5, str(self.data[68])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-7])+'%', 1, 1)
        pdf.cell(30, 5, '1-2')
        pdf.cell(20, 5, str(self.data[23])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-6])+'%', 1)
        pdf.cell(20, 5, str(self.data[35])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-6])+'%', 1)
        pdf.cell(20, 5, str(self.data[51])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-6])+'%', 1)
        pdf.cell(20, 5, str(self.data[69])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-6])+'%', 1, 1)
        pdf.cell(30, 5, '0.5-1')
        pdf.cell(20, 5, str(self.data[24])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-5])+'%', 1)
        pdf.cell(20, 5, str(self.data[36])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-5])+'%', 1)
        pdf.cell(20, 5, str(self.data[52])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-5])+'%', 1)
        pdf.cell(20, 5, str(self.data[70])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-5])+'%', 1, 1)
        pdf.cell(30, 5, '0.25-0.5')
        pdf.cell(20, 5, str(self.data[25])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-4])+'%', 1)
        pdf.cell(20, 5, str(self.data[37])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-4])+'%', 1)
        pdf.cell(20, 5, str(self.data[53])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-4])+'%', 1)
        pdf.cell(20, 5, str(self.data[71])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-4])+'%', 1, 1)
        pdf.cell(30, 5, '0.125-0.25')
        pdf.cell(20, 5, str(self.data[26])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-3])+'%', 1)
        pdf.cell(20, 5, str(self.data[38])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-3])+'%', 1)
        pdf.cell(20, 5, str(self.data[54])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-3])+'%', 1)
        pdf.cell(20, 5, str(self.data[72])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-3])+'%', 1, 1)
        pdf.cell(30, 5, '0.063-0.125')
        pdf.cell(20, 5, str(self.data[27])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-2])+'%', 1)
        pdf.cell(20, 5, str(self.data[39])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-2])+'%', 1)
        pdf.cell(20, 5, str(self.data[55])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-2])+'%', 1)
        pdf.cell(20, 5, str(self.data[73])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-2])+'%', 1, 1)
        pdf.cell(30, 5, '<0.063')
        pdf.cell(20, 5, str(self.data[28])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_ertrag[-1])+'%', 1)
        pdf.cell(20, 5, str(self.data[40])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_sand[-1])+'%', 1)
        pdf.cell(20, 5, str(self.data[56])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_4_16[-1])+'%', 1)
        pdf.cell(20, 5, str(self.data[74])+'g', 1)
        pdf.cell(20, 5, "{0: 3.1f}".format(self.p_16_32[-1])+'%', 1, 1)
        pdf.set_font('Arial', 'B', 14)
        pdf.image("images/"+str(self.name)+".png", x=40, w=140, type='PNG')
        pdf.output("PDF/"+str(self.name)+".pdf", 'F')

    def create_plot(self):
        self.xaxis_ertrag = [0.063, 0.125, 0.25, 0.5, 1, 2, 4, 5.6, 8, 11, 16, 22, 32, 45]
        self.xaxis_sand = [0.063, 0.125, 0.25, 0.5, 1, 2, 4, 5.6]
        self.xaxis_4_16 = [0.063, 0.125, 0.25, 0.5, 1, 2, 4, 5.6, 8, 11, 16, 22]
        ax = plt.subplot()
        if self.checkVar0_4.get() == 1:
            x = self.xaxis_sand
            plt.axis([0, 6, 0, 100])
            ax.set_xscale('linear')
            if self.checkVar0_32.get()+self.checkVar4_16.get()+self.checkVar16_32.get() >= 1:
                x = self.xaxis_ertrag
                ax.set_xscale('log')
                plt.axis([0.06, 45, 0, 100])
                ax.set_xticks(x)
        else:
            x = self.xaxis_ertrag
            ax.set_xscale('log')
            plt.axis([0.06, 45, 0, 100])
            ax.set_xticks(x)
        y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        plt.grid(True, which='both')
        ax.set_yticks(y)
        formatter = FuncFormatter(lambda x, _: '{:.16g}'.format(x))
        ax.get_xaxis().set_major_formatter(formatter)
        self.p_ertrag = self.M_prozent_0_32.copy()
        self.p_sand = self.M_prozent_0_4.copy()
        self.p_4_16 = self.M_prozent_4_16.copy()
        self.p_16_32 = self.M_prozent_16_32.copy()
        if self.checkVar0_32.get() == 1:
            x = self.xaxis_ertrag
            self.M0_32 = []
            for n in range(len(self.M_prozent_0_32)):
                self.M0_32.append(sum(self.M_prozent_0_32))
                self.M_prozent_0_32.pop(0)
            self.M0_32.reverse()
            plt.plot(x, self.M0_32, 'b', label='Ertrag 0/32')
        if self.checkVar0_4.get() == 1:
            self.M0_4 = []
            for n in range(len(self.M_prozent_0_4)):
                self.M0_4.append(sum(self.M_prozent_0_4))
                self.M_prozent_0_4.pop(0)
            self.M0_4.reverse()
            x = self.xaxis_sand
            plt.plot(x, self.M0_4, 'g', label='Sand 0/4')
        if self.checkVar4_16.get() == 1:
            self.M4_16 = []
            for n in range(len(self.M_prozent_4_16)):
                self.M4_16.append(sum(self.M_prozent_4_16))
                self.M_prozent_4_16.pop(0)
            self.M4_16.reverse()
            x = self.xaxis_4_16
            plt.plot(x, self.M4_16, 'r', label='Rücklauf 4/16')
        if self.checkVar16_32.get() == 1:
            self.M16_32 = []
            for n in range(len(self.M_prozent_16_32)):
                self.M16_32.append(sum(self.M_prozent_16_32))
                self.M_prozent_16_32.pop(0)
            self.M16_32.reverse()
            x = self.xaxis_ertrag
            plt.plot(x, self.M16_32, 'y', label='Rücklauf 16/32')
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=2, mode="expand", borderaxespad=0.)
        plt.savefig("images/"+str(self.name)+".png")
        plt.clf()
        self.create_pdf_file()

    def calculate_data(self):
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
        # Berechnung der Massenprozente
        self.Einwaage_0_32 = self.data[13]
        self.Einwaage_0_4 = self.data[31]
        self.Einwaage_4_16 = self.data[43]
        self.Einwaage_16_32 = self.data[59]
        self.M_prozent_0_32 = []
        self.M_prozent_0_4 = []
        self.M_prozent_4_16 = []
        self.M_prozent_16_32 = []
        for x in range(15, 28):
            try:
                self.M_prozent_0_32.append((self.data[x]/self.Einwaage_0_32)*100)
            except ZeroDivisionError:
                self.M_prozent_0_32.append(0)
        if self.checkVar0_32.get() == 1 and self.data[28] == 0:
            mBox.showinfo('', 'Keine Einwaage für Ertrag 0/32')
        try:
            self.M_prozent_0_32.append((self.data[28]/self.Einwaage_0_32)*100)
        except ZeroDivisionError:
            self.M_prozent_0_32.append(0)
        for x in range(33, 40):
            try:
                self.M_prozent_0_4.append((self.data[x]/self.Einwaage_0_4)*100)
            except ZeroDivisionError:
                self.M_prozent_0_4.append(0)
        if self.checkVar0_4.get() == 1 and self.data[40] == 0:
            mBox.showinfo('', 'Keine Einwaage für Sand 0/4')
        try:
            self.M_prozent_0_4.append((self.data[40]/self.Einwaage_0_4)*100)
        except ZeroDivisionError:
            self.M_prozent_0_4.append(0)
        for x in range(45, 56):
            try:
                self.M_prozent_4_16.append((self.data[x]/self.Einwaage_4_16)*100)
            except ZeroDivisionError:
                self.M_prozent_4_16.append(0)
        if self.checkVar4_16.get() == 1 and self.data[56] == 0:
            mBox.showinfo('', 'Keine Einwaage für Rücklauf 4/16')
        try:
            self.M_prozent_4_16.append((self.data[56]/self.Einwaage_4_16)*100)
        except ZeroDivisionError:
            self.M_prozent_4_16.append(0)
        for x in range(61, 74):
            try:
                self.M_prozent_16_32.append((self.data[x]/self.Einwaage_16_32)*100)
            except ZeroDivisionError:
                self.M_prozent_16_32.append(0)
        if self.checkVar16_32.get() == 1 and self.data[74] == 0:
            mBox.showinfo('', 'Keine Einwaage für Rücklauf 16/32')
        try:
            self.M_prozent_16_32.append((self.data[74]/self.Einwaage_16_32)*100)
        except ZeroDivisionError:
            self.M_prozent_16_32.append(0)
        self.create_plot()

    def create_file(self):
        t = self.test_v()
        if t == 0:
            file, x = self.test_file()
            if x != 0:
                # Berechnungen
                self.auswage_ertrag = self.ertrag_eingabe[0].get()+self.ertrag_eingabe[1].get() +\
                    self.ertrag_eingabe[2].get()+self.ertrag_eingabe[3].get() +\
                    self.ertrag_eingabe[4].get() + self.ertrag_eingabe[5].get() +\
                    self.ertrag_eingabe[6].get() + self.ertrag_eingabe[7].get() +\
                    self.ertrag_eingabe[8].get() + self.ertrag_eingabe[9].get() +\
                    self.ertrag_eingabe[10].get() + self.ertrag_eingabe[11].get() +\
                    self.ertrag_eingabe[12].get()
                self._var_ertrag_verlust = self.var_trocken1.get() - self.auswage_ertrag
                self.var_eigenfeuchte_ertrag = self.var_feucht1.get() - self.var_trocken1.get()
                self.auswage2 = self.sand_eingabe[0].get()+self.sand_eingabe[1].get() +\
                    self.sand_eingabe[2].get()+self.sand_eingabe[3].get() +\
                    self.sand_eingabe[4].get() + self.sand_eingabe[5].get() +\
                    self.sand_eingabe[6].get()
                self._var_sand_verlust = self.var_trocken2.get() - self.auswage2
                self.var_eigenfeuchte2 = self.var_feucht2.get() - self.var_trocken2.get()
                self.auswage_kies4_16 = self.kies4_16_eingabe[0].get()+self.kies4_16_eingabe[1].get() +\
                    self.kies4_16_eingabe[2].get()+self.kies4_16_eingabe[3].get() +\
                    self.kies4_16_eingabe[4].get()+self.kies4_16_eingabe[5].get() +\
                    self.kies4_16_eingabe[6].get()+self.kies4_16_eingabe[7].get() +\
                    self.kies4_16_eingabe[8].get()+self.kies4_16_eingabe[9].get() +\
                    self.kies4_16_eingabe[10].get()
                self._var_kies4_16_verlust = self.var_trocken3.get() - self.auswage_kies4_16
                self.var_eigenfeuchte_kies4_16 = self.var_feucht3.get() - self.var_trocken3.get()
                self.auswage_kies16_32 = self.kies16_32_eingabe[0].get()+self.kies16_32_eingabe[1].get() +\
                    self.kies16_32_eingabe[2].get()+self.kies16_32_eingabe[3].get() +\
                    self.kies16_32_eingabe[4].get()+self.kies16_32_eingabe[5].get() +\
                    self.kies16_32_eingabe[6].get()+self.kies16_32_eingabe[7].get() +\
                    self.kies16_32_eingabe[8].get()+self.kies16_32_eingabe[9].get() +\
                    self.kies16_32_eingabe[10].get()+self.kies16_32_eingabe[11].get() +\
                    self.kies16_32_eingabe[12].get()
                self._var_kies16_32_verlust = self.var_trocken4.get() - self.auswage_kies16_32
                self.var_eigenfeuchte_kies16_32 = self.var_feucht4.get() - self.var_trocken4.get()
                Daten = {1: self.probe_nr.get(),
                         2: date.today(),
                         3: self.probe_t.get(),
                         4: self.aufstr.get(),
                         5: self.b1.get(),
                         6: self.b2.get(),
                         7: self.motor.get(),
                         8: self.aufgabemasse1.get(),
                         9: self.aufgabebandv1.get(),
                         10: self.aufgabemasse2.get(),
                         11: self.aufgabebandv2.get(),
                         12: self.vdouble.get(),
                         13: self.var_feucht1.get(),
                         14: self.var_trocken1.get(),
                         15: self.var_eigenfeuchte_ertrag,
                         16: self.ertrag_eingabe[0].get(),
                         17: self.ertrag_eingabe[1].get(),
                         18: self.ertrag_eingabe[2].get(),
                         19: self.ertrag_eingabe[3].get(),
                         20: self.ertrag_eingabe[4].get(),
                         21: self.ertrag_eingabe[5].get(),
                         22: self.ertrag_eingabe[6].get(),
                         23: self.ertrag_eingabe[7].get(),
                         24: self.ertrag_eingabe[8].get(),
                         25: self.ertrag_eingabe[9].get(),
                         26: self.ertrag_eingabe[10].get(),
                         27: self.ertrag_eingabe[11].get(),
                         28: self.ertrag_eingabe[12].get(),
                         29: self._var_ertrag_verlust,
                         30: self.auswage_ertrag,
                         31: self.var_feucht2.get(),
                         32: self.var_trocken2.get(),
                         33: self.var_eigenfeuchte2,
                         34: self.sand_eingabe[0].get(),
                         35: self.sand_eingabe[1].get(),
                         36: self.sand_eingabe[2].get(),
                         37: self.sand_eingabe[3].get(),
                         38: self.sand_eingabe[4].get(),
                         39: self.sand_eingabe[5].get(),
                         40: self.sand_eingabe[6].get(),
                         41: self._var_sand_verlust,
                         42: self.auswage2,
                         43: self.var_feucht3.get(),
                         44: self.var_trocken3.get(),
                         45: self.var_eigenfeuchte_kies4_16,
                         46: self.kies4_16_eingabe[0].get(),
                         47: self.kies4_16_eingabe[1].get(),
                         48: self.kies4_16_eingabe[2].get(),
                         49: self.kies4_16_eingabe[3].get(),
                         50: self.kies4_16_eingabe[4].get(),
                         51: self.kies4_16_eingabe[5].get(),
                         52: self.kies4_16_eingabe[6].get(),
                         53: self.kies4_16_eingabe[7].get(),
                         54: self.kies4_16_eingabe[8].get(),
                         55: self.kies4_16_eingabe[9].get(),
                         56: self.kies4_16_eingabe[10].get(),
                         57: self._var_kies4_16_verlust,
                         58: self.auswage_kies4_16,
                         59: self.var_feucht4.get(),
                         60: self.var_trocken4.get(),
                         61: self.var_eigenfeuchte_kies16_32,
                         62: self.kies16_32_eingabe[0].get(),
                         63: self.kies16_32_eingabe[1].get(),
                         64: self.kies16_32_eingabe[2].get(),
                         65: self.kies16_32_eingabe[3].get(),
                         66: self.kies16_32_eingabe[4].get(),
                         67: self.kies16_32_eingabe[5].get(),
                         68: self.kies16_32_eingabe[6].get(),
                         69: self.kies16_32_eingabe[7].get(),
                         70: self.kies16_32_eingabe[8].get(),
                         71: self.kies16_32_eingabe[9].get(),
                         72: self.kies16_32_eingabe[10].get(),
                         73: self.kies16_32_eingabe[11].get(),
                         74: self.kies16_32_eingabe[12].get(),
                         75: self._var_kies16_32_verlust,
                         76: self.auswage_kies16_32,
                         }
                for key, value in Daten.items():
                    file.write(str(value)+"\n")
                try:
                    self.eigen_p_ertrag = (self.data[14]/self.data[12])*100
                except:
                    ZeroDivisionError
                    self.eigen_p_ertrag = 0
                try:
                    self.eigen_p_sand = (self.data[32]/self.data[30])*100
                except:
                    ZeroDivisionError
                    self.eigen_p_sand = 0
                try:
                    self.eigen_p_4_16 = (self.data[44]/self.data[42])*100
                except:
                    ZeroDivisionError
                    self.eigen_p_4_16 = 0
                try:
                    self.eigen_p_16_32 = (self.data[60]/self.data[58])*100
                except:
                    ZeroDivisionError
                    self.eigen_p_16_32 = 0
                file.close()
                self.calculate_data()
            else:
                pass

    def createWidgets(self):

        # Tab Control introduced here -----------------------
        tabControl = ttk.Notebook(self.win)
        # Create Tab Control
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Ertrag 0/32')
        Eigenfeuchte1 = ttk.Label(tab1, text="Eigenfeuchte:")
        Eigenfeuchte1.grid(column=0, row=0)
        Einwaage_feucht1 = ttk.Label(tab1, text="Einwaage feucht:")
        Einwaage_feucht1.grid(column=0, row=1)
        self.var_feucht1 = tk.DoubleVar()
        E_feucht1 = ttk.Entry(tab1, width=15, textvariable=self.var_feucht1)
        E_feucht1.grid(column=1, row=1)
        Einwaage_trocken1 = ttk.Label(tab1, text="Einwaage trocken:")
        Einwaage_trocken1.grid(column=0, row=2)
        self.var_trocken1 = tk.DoubleVar()
        E_trocken1 = ttk.Entry(tab1, width=15, textvariable=self.var_trocken1)
        E_trocken1.grid(column=1, row=2)
        Kornung = {1: ">32", 2: "22-32", 3: "16-22", 4: "11-16", 5: "8-11",
                   6: "5.6-8", 7: "4-5.6", 8: "2-4", 9: "1-2", 10: "0,5-1",
                   11: "0,25-0,5", 12: "0,125-0,25", 13: "0,063-0,125"}
        spalte = 1
        reihe = 4
        self.ertrag_eingabe = []
        for key, Korn in Kornung.items():
            label = ttk.Label(tab1, text=Korn)
            label.grid(column=spalte, row=reihe)
            spalte = spalte + 1
            var = tk.DoubleVar()
            self.ertrag_eingabe.append(var)
            Eingabe = ttk.Entry(tab1, width=15, textvariable=var)
            Eingabe.grid(column=spalte, row=reihe)
            spalte = spalte - 1
            reihe = reihe + 1

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='0/4 Sand')  # Create a tab
        # Add the tab
        Eigenfeuchte2 = ttk.Label(tab2, text="Eigenfeuchte:")
        Eigenfeuchte2.grid(column=0, row=0)
        Einwaage_feucht2 = ttk.Label(tab2, text="Einwaage feucht:")
        Einwaage_feucht2.grid(column=0, row=1)
        self.var_feucht2 = tk.DoubleVar()
        E_feucht2 = ttk.Entry(tab2, width=15, textvariable=self.var_feucht2)
        E_feucht2.grid(column=1, row=1)
        Einwaage_trocken2 = ttk.Label(tab2, text="Einwaage trocken:")
        Einwaage_trocken2.grid(column=0, row=2)
        self.var_trocken2 = tk.DoubleVar()
        E_trocken2 = ttk.Entry(tab2, width=15, textvariable=self.var_trocken2)
        E_trocken2.grid(column=1, row=2)
        Kornung = {1: ">4", 2: "2-4", 3: "1-2", 4: "0,5-1", 5: "0,25-0,5", 6: "0,125-0,25",
                   7: "0,063-0,125"}
        spalte = 1
        reihe = 4
        self.sand_eingabe = []
        for key, Korn in Kornung.items():
            label = ttk.Label(tab2, text=Korn)
            label.grid(column=spalte, row=reihe)
            spalte = spalte + 1
            var = tk.DoubleVar()
            self.sand_eingabe.append(var)
            Eingabe = ttk.Entry(tab2, width=15, textvariable=var)
            Eingabe.grid(column=spalte, row=reihe)
            spalte = spalte - 1
            reihe = reihe + 1

        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='4/16 Kies')
        Eigenfeuchte3 = ttk.Label(tab3, text="Eigenfeuchte:")
        Eigenfeuchte3.grid(column=0, row=0)
        Einwaage_feucht3 = ttk.Label(tab3, text="Einwaage feucht:")
        Einwaage_feucht3.grid(column=0, row=1)
        self.var_feucht3 = tk.DoubleVar()
        E_feucht3 = ttk.Entry(tab3, width=15, textvariable=self.var_feucht3)
        E_feucht3.grid(column=1, row=1)
        Einwaage_trocken3 = ttk.Label(tab3, text="Einwaage trocken:")
        Einwaage_trocken3.grid(column=0, row=2)
        self.var_trocken3 = tk.DoubleVar()
        E_trocken3 = ttk.Entry(tab3, width=15, textvariable=self.var_trocken3)
        E_trocken3.grid(column=1, row=2)
        Kornung = {1: ">16", 2: "11-16", 3: "8-11",
                   4: "5.6-8", 5: "4-5.6", 6: "2-4", 7: "1-2", 8: "0,5-1",
                   9: "0,25-0,5", 10: "0,125-0,25", 11: "0,063-0,125"}
        spalte = 1
        reihe = 4
        self.kies4_16_eingabe = []
        for key, Korn in Kornung.items():
            label = ttk.Label(tab3, text=Korn)
            label.grid(column=spalte, row=reihe)
            spalte = spalte + 1
            var = tk.DoubleVar()
            self.kies4_16_eingabe.append(var)
            Eingabe = ttk.Entry(tab3, width=15, textvariable=var)
            Eingabe.grid(column=spalte, row=reihe)
            spalte = spalte - 1
            reihe = reihe + 1
          # Create second tab
        # Add second tab
        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text='16/32 Kies')
        tabControl.grid(column=0, row=7)
        Eigenfeuchte4 = ttk.Label(tab4, text="Eigenfeuchte:")
        Eigenfeuchte4.grid(column=0, row=0)
        Einwaage_feucht4 = ttk.Label(tab4, text="Einwaage feucht:")
        Einwaage_feucht4.grid(column=0, row=1)
        self.var_feucht4 = tk.DoubleVar()
        E_feucht4 = ttk.Entry(tab4, width=15, textvariable=self.var_feucht4)
        E_feucht4.grid(column=1, row=1)
        Einwaage_trocken4 = ttk.Label(tab4, text="Einwaage trocken:")
        Einwaage_trocken4.grid(column=0, row=2)
        self.var_trocken4 = tk.DoubleVar()
        E_trocken5 = ttk.Entry(tab4, width=15, textvariable=self.var_trocken4)
        E_trocken5.grid(column=1, row=2)
        Kornung = {1: ">32", 2: "22-32", 3: "16-22", 4: "11-16", 5: "8-11",
                   6: "5.6-8", 7: "4-5.6", 8: "2-4", 9: "1-2", 10: "0,5-1",
                   11: "0,25-0,5", 12: "0,125-0,25", 13: "0,063-0,125"}
        spalte = 1
        reihe = 4
        self.kies16_32_eingabe = []
        for key, Korn in Kornung.items():
            label = ttk.Label(tab4, text=Korn)
            label.grid(column=spalte, row=reihe)
            spalte = spalte + 1
            var = tk.DoubleVar()
            self.kies16_32_eingabe.append(var)
            Eingabe = ttk.Entry(tab4, width=15, textvariable=var)
            Eingabe.grid(column=spalte, row=reihe)
            spalte = spalte - 1
            reihe = reihe + 1

        # ======================
        # Start GUI
        # ======================
oop = OOP()
oop.win.mainloop()
