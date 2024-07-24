from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Привет, это мой первый PDF-документ.")
    c.save()

create_pdf("example.pdf")
