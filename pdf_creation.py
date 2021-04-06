from fpdf import FPDF 
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Adds the title
title="2021 Arcadia Mobile Market"
pdf.set_fill_color(0, 180, 0)
pdf.cell(170, 10, title, 0, 1, 'C', True)

# Adds the purchase report below title
member="Purchase Report: Member #12"
pdf.set_font('Arial', 'B', 12)
pdf.cell(170, 10, member, 0, 1, 'C', True)

visits = 9
servings =170
total = "$94.65"

pdf.cell(55, 10, f"Visits: {visits}", 0, 0, 'C', False)
pdf.cell(55, 10, f"Servings: {servings}", 0, 0, 'C', False)
pdf.cell(55, 10, f"Total: {total}", 0, 0, 'C', False)


# Generates the PDF
customer_name = "Example Customer"
pdf.output(customer_name + ".pdf", 'F')
 # https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html