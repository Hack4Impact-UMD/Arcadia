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

#Prints Thank You Text
pdf.set_y(pdf.get_y() + 10)
pdf.set_font('Arial', '', 10)
thankYouText="Thanks for being a Loyalty Member at the Arcadia \nMobile Market! Based on your purchases last \nyear, consider adding more Brown/White and \nBlue/Purple to your diet this season to make sure \nyou get all the nutrients you need for a healthy \ndiet!"
pdf.multi_cell(170, 5, thankYouText, 0, 0, 'J', False)

#Print white box next to it
pdf.set_y(pdf.get_y()-35)
pdf.set_x(pdf.get_x()+130)
boxText="Remember, the Arcadia Mobile Market doubles your SNAP, WIC, and SR FMNP purchases so you get even more great food for your money!"
pdf.multi_cell(40, 5, boxText, 1, 1, 'J', False)

#Draw Line
pdf.line(0, 80, 1000, 82)

# Draw Red Box
pdf.set_y(pdf.get_y()+20)
pdf.set_fill_color(255,0,0)
pdf.cell(50, 5, "Red", 0, 1, 'C', True)
redBoxText="Good for the heart and can help to lower the risk of heart disease. TIP: Ketchup is NOT a vegetable TRY: Beets, red pepper, red apples, tomatoes"
pdf.multi_cell(50, 5, redBoxText, 0, 'L', True)

# Generates the PDF
customer_name = "Example Customer P2"
pdf.output(customer_name + ".pdf", 'F')