from fpdf import FPDF 
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Rainbow Report')
customer_name = "Example Customer"
pdf.output( customer_name + ".pdf", 'F')
 # https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html