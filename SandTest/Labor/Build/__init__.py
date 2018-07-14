# from .<foldername> import *
# falls module geladen werden sollen aus <foldername>


def create_pdf_file(self):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Siebanalyse Kieswerk Oberbrunn', 0, 1, 'c')
    pdf.output("PDF/"+str(self.name)+".pdf", 'F')


create_pdf_file()
