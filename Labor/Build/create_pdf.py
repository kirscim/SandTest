# Modul für die grafische Ausgabe
from fpdf import FPDF
from datetime import date


class create_pdf_file():
    def __init__(self, name, einstellungen, dict, checklist):
        self.name = name
        self.einstellungen = einstellungen
        self.checklist = checklist
        Dict = dict
        self.Einwaage_trocken = Dict['Einwaage_trocken']
        self.Einwaage_feucht = Dict['Einwaage_feucht']
        self.Eigenfeuchte = Dict['Eigenfeuchte']
        self.Eigenfeuchte_p = Dict['Eigenfeuchte_p']
        self.Eingabe_Ertrag = Dict['Eingabe_Ertrag']
        self.Eingabe_Ertrag_p = Dict['Eingabe_Ertrag_p']
        self.Eingabe_Ertrag_p.reverse()
        self.Eingabe_Sand = Dict['Eingabe_Sand']
        self.Eingabe_Sand_p = Dict['Eingabe_Sand_p']
        self.Eingabe_Sand_p.reverse()
        self.Eingabe_Sand_w = Dict['Eingabe_Sand_w']
        self.Eingabe_Sand_w_p = Dict['Eingabe_Sand_w_p']
        self.Eingabe_Sand_w_p.reverse()
        self.Eingabe_4_16 = Dict['Eingabe_4_16']
        self.Eingabe_4_16_p = Dict['Eingabe_4_16_p']
        self.Eingabe_4_16_p.reverse()
        self.Eingabe_16_32 = Dict['Eingabe_16_32']
        self.Eingabe_16_32_p = Dict['Eingabe_16_32_p']
        self.Eingabe_16_32_p.reverse()
        # Seite generieren
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        # Header
        pdf.cell(65)
        pdf.cell(60, 10, 'Siebanalyse Kieswerk Oberbrunn', 0, 2, 'C')
        pdf.set_font('Arial', '', 10)
        pdf.cell(70)
        pdf.cell(30, 5, 'Probennummer: '+str(self.einstellungen[1]), 0, 0)
        pdf.cell(30, 5, 'Datum:', 0, 2, 'R')
        pdf.cell(30, 5, str(date.today()), 0, 2, 'R')
        pdf.cell(30, 5, self.einstellungen[0], 0, 1, 'R')
        # Optionen
        pdf.cell(40, 5, 'Brechereinstellungen:', 1, 0, 'C')
        pdf.cell(98)
        pdf.cell(30, 5, 'Aufgabe:', 1, 1, 'C')
        pdf.cell(30, 5, 'Schleudertisch:', 0, 0, 'R')
        pdf.cell(30, 5, str(self.einstellungen[7]), 0, 0, 'L')
        pdf.cell(75)
        pdf.cell(30, 5, self.einstellungen[2], 0, 1, 'C')
        pdf.cell(30, 5, 'Schleuderplatten:', 0, 0, 'R')
        pdf.cell(30, 5, self.einstellungen[8], 0, 0, 'L')
        pdf.cell(75)
        pdf.cell(30, 5, 'feine Gesteinsart', 0, 1, 'C')
        pdf.cell(30, 5, 'Testgeschwindigkeit:', 0, 0, 'R')
        pdf.cell(30, 5, str(self.einstellungen[10]), 0, 0, 'L')
        pdf.cell(75)
        pdf.cell(30, 5, 'Kalkstein', 0, 1, 'C')
        pdf.cell(30, 5, 'Motor:', 0, 0, 'R')
        pdf.cell(30, 5, self.einstellungen[9], 0, 1, 'L')
        pdf.cell(10, 5, '', 0, 1)
        pdf.cell(40, 5, 'Aufgabe in [t/h]:', 1, 0, 'C')
        pdf.cell(20, 5, '', 1, 0, 'L')
        pdf.cell(30)
        pdf.cell(40, 5, 'Ertrag Sand in [t/h]:', 1, 0, 'C')
        pdf.cell(20, 5, '', 1, 1, 'L')
        pdf.cell(10, 5, '', 0, 1)
        pdf.cell(30)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(33, 5, 'Ertrag 0/32')
        pdf.cell(33, 5, 'Sand 0/4')
        pdf.cell(33, 5, 'Sand 0/4 w')
        pdf.cell(33, 5, 'Rücklauf 4/16')
        pdf.cell(33, 5, 'Rücklauf 16/32', 0, 1)
        pdf.set_font('Arial', '', 10)
        pdf.cell(33, 5, 'Einwaage feucht:', 0, 0)
        pdf.cell(17, 5, str(self.Einwaage_feucht[0])+'g', 1)
        pdf.cell(16, 5)
        pdf.cell(17, 5, str(self.Einwaage_feucht[1])+'g', 1)
        pdf.cell(16)
        pdf.cell(17, 5, str(self.Einwaage_feucht[2])+'g', 1)
        pdf.cell(16)
        pdf.cell(17, 5, str(self.Einwaage_feucht[3])+'g', 1)
        pdf.cell(16)
        pdf.cell(17, 5, str(self.Einwaage_feucht[4])+'g', 1, 1)
        pdf.cell(33, 5, 'Einwaage trocken:', 0, 0)
        pdf.cell(17, 5, str(self.Einwaage_trocken[0])+'g', 1)
        pdf.cell(16, 5)
        pdf.cell(17, 5, str(self.Einwaage_trocken[1])+'g', 1)
        pdf.cell(16)
        pdf.cell(17, 5, str(self.Einwaage_trocken[2])+'g', 1)
        pdf.cell(16)
        pdf.cell(17, 5, str(self.Einwaage_trocken[3])+'g', 1)
        pdf.cell(16)
        pdf.cell(17, 5, str(self.Einwaage_trocken[4])+'g', 1, 1)
        pdf.cell(33, 5, 'Eigenfeuchte:', 0, 0)
        pdf.cell(17, 5, str(self.Eigenfeuchte[0])+'g', 1)
        pdf.cell(16, 5, '{0:3.2f}'.format(self.Eigenfeuchte_p[0])+'%', 1)
        pdf.cell(17, 5, str(self.Eigenfeuchte[1])+'g', 1)
        pdf.cell(16, 5, '{0:3.2f}'.format(self.Eigenfeuchte_p[1])+'%', 1)
        pdf.cell(17, 5, str(self.Eigenfeuchte[2])+'g', 1)
        pdf.cell(16, 5, '{0:3.2f}'.format(self.Eigenfeuchte_p[2])+'%', 1)
        pdf.cell(17, 5, str(self.Eigenfeuchte[3])+'g', 1)
        pdf.cell(16, 5, '{0:3.2f}'.format(self.Eigenfeuchte_p[3])+'%', 1)
        pdf.cell(17, 5, str(self.Eigenfeuchte[4])+'g', 1)
        pdf.cell(16, 5, '{0:3.2f}'.format(self.Eigenfeuchte_p[4])+'%', 1, 1)
        pdf.cell(33, 5, 'Kornzusammensetzung in [mm] und [M.%]', 0, 1)
        pdf.cell(33, 5, '>32')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[0])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[0])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, str(self.Eingabe_16_32[0])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_16_32_p[0])+'%', 1, 1)
        pdf.cell(33, 5, '22-32')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[1])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[1])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, str(self.Eingabe_16_32[1])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_16_32_p[1])+'%', 1, 1)
        pdf.cell(33, 5, '16-22')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[2])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[2])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, str(self.Eingabe_4_16[0])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_4_16_p[0])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_16_32[2])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_16_32_p[2])+'%', 1, 1)
        pdf.cell(33, 5, '11-16')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[3])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[3])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, str(self.Eingabe_4_16[1])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_4_16_p[1])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_16_32[3])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_16_32_p[3])+'%', 1, 1)
        pdf.cell(33, 5, '8-11')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[4])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[4])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, str(self.Eingabe_4_16[2])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_4_16_p[2])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '5.6-8')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[5])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[5])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, str(self.Eingabe_4_16[3])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_4_16_p[3])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '4-5.6')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[6])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[6])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[0])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[0])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[0])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[0])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_4_16[4])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_4_16_p[4])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '2-4')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[7])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[7])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[1])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[1])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[1])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[1])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_4_16[5])+'g', 1)
        pdf.cell(16, 5, '{0: 3.2f}'.format(self.Eingabe_4_16_p[5])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '1-2')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[8])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[8])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[2])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[2])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[2])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[2])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '0.5-1')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[9])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[9])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[3])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[3])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[3])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[3])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '0.25-0.5')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[10])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[10])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[4])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[4])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[4])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[4])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '0.125-0.25')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[11])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[11])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[5])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[5])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[5])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[5])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '0.063-0.125')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[12])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[12])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[6])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[6])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[6])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[6])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.cell(33, 5, '<0.063')
        pdf.cell(17, 5, str(self.Eingabe_Ertrag[13])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Ertrag_p[13])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand[7])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_p[7])+'%', 1)
        pdf.cell(17, 5, str(self.Eingabe_Sand_w[7])+'g', 1)
        pdf.cell(16, 5, "{0: 3.2f}".format(self.Eingabe_Sand_w_p[7])+'%', 1)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0)
        pdf.cell(17, 5, '', 0)
        pdf.cell(16, 5, '', 0, 1)
        pdf.set_font('Arial', 'B', 14)
        pdf.image("images/"+str(self.name)+".png", x=40, w=160, type='PNG')
        pdf.output("PDF/"+str(self.name)+".pdf", 'F')
