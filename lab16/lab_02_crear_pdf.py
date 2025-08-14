from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("portada.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 28)
c.drawString(72, 780, "Tu Nombre")
c.setFont("Helvetica", 14)
c.drawString(72, 750, "Portada Esteganografía PDF")
c.showPage()
c.save()
print("portada.pdf listo")

