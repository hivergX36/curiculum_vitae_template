from fpdf import FPDF
from io import BytesIO


# 1. Create a function to generate PDF data in memory
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello from Streamlit!", ln=1, align="C")

    # Return PDF as bytes
    return pdf.output(dest="S").encode("latin1")


# 2. Generate the PDF bytes
pdf_bytes = create_pdf()
