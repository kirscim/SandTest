# Modul zur Erstellung von GUI Einträgen
import tkinter as tk
from tkinter import ttk


class Texteintrag():
    def __init__(self, window, text, column, row):
        self.win = window
        self.text = text
        self.column = column
        self.row = row
        self.Eintrag = ttk.Label(self.win, text=self.text, anchor='w')
        self.Eintrag.grid(column=self.column, row=self.row)


class Auswahlkasten(Texteintrag):
    def __init__(self, window, text, column, row, values):
        super().__init__(window, text, column, row)
        self.values = values
        self.variable = tk.StringVar()
        self.Kasten = ttk.Combobox(self.win, width=20, textvariable=self.variable)
        self.Kasten['values'] = self.values
        self.Kasten.grid(column=self.column+1, row=self.row)
        self.Kasten.current(0)

    def get(self):
        return self.variable.get()


class UAuswahlkasten(Auswahlkasten):
    def __init__(self, window, text, column, row, values):
        super().__init__(window, text, column, row, values)
        self.Kasten.grid(column=self.column, row=self.row+1)


class EingabeZahl(Texteintrag):
    def __init__(self, window, text, column, row):
        super().__init__(window, text, column, row)
        self.variable = tk.DoubleVar()
        self.Eintrag = ttk.Entry(self.win, width=20, textvariable=self.variable)
        self.Eintrag.grid(column=self.column+1, row=self.row)

    def get(self):
        return self.variable.get()


class UEingabeZahl(EingabeZahl):
    def __init__(self, window, text, column, row):
        super().__init__(window, text, column, row)
        self.Eintrag.grid(column=self.column, row=self.row+1)


class UEingabeString(UEingabeZahl):
    def __init__(self, window, text, column, row):
        super().__init__(window, text, column, row)
        self.variable = tk.StringVar()


class Korn_Eingabe():
    def __init__(self, window, columnspan, rowspan):
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.win = window
        self.tabcontrol = ttk.Notebook(self.win)
        self.tabcontrol.grid(columnspan=self.columnspan, rowspan=self.rowspan)
        self.tab = []
        self.data = []

    def create(self, name, Kornung):
        self.name = name
        self.Kornung = Kornung
        self.tab.append(ttk.Frame(self.tabcontrol))
        self.tabcontrol.add(self.tab[-1], text=self.name)
        Efeucht = EingabeZahl(self.tab[-1], 'Einwaage feucht:', 0, 0)
        self.data.append(Efeucht)
        Etrocken = EingabeZahl(self.tab[-1], 'Einwaage trocken:', 0, 1)
        self.data.append(Etrocken)
        Spalte = 0
        Reihe = 3
        for Korn in self.Kornung:
            Kornob = EingabeZahl(self.tab[-1], Korn, Spalte, Reihe)
            self.data.append(Kornob)
            Reihe = Reihe + 1


class Check(Texteintrag):
    def __init__(self, window, text, column, row):
        super().__init__(window, text, column, row)
        self.variable = tk.IntVar()
        self.Check = ttk.Checkbutton(self.win, text=self.text,
                                     variable=self.variable,
                                     onvalue=1, offvalue=0)
        self.Check.grid(column=self.column, row=self.row)

    def get(self):
        return self.variable.get()
