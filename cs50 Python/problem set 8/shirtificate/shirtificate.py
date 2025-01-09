from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", style="B", size=15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)


user_name = input("Name? ")

pdf = PDF(unit="mm", format="A4")
pdf.add_page()
pdf.image("shirtificate.png", x=1, y=70)
pdf.cell(w=185, h=215, text=f"{user_name} took CS50", align="C")
pdf.output("shirtificate.pdf")
