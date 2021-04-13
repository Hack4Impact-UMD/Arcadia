from fpdf import FPDF 
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Adds the title
title="2021 Arcadia Mobile Market"
pdf.set_fill_color(0, 180, 0)
titleX = pdf.get_x()
titleY = pdf.get_y()
pdf.cell(170, 20, '', 0, 1, 'C', True)
pdf.set_x(titleX)
pdf.set_y(titleY)
pdf.cell(170, 10, title, 0, 1, 'C', False)

# Adds the purchase report below title
member="Purchase Report: Member #12"
pdf.set_font('Arial', 'B', 12)
pdf.set_y(titleY+10)
pdf.cell(170, 10, member, 0, 1, 'C', False)

#Prints Thank You Text
pdf.set_y(pdf.get_y() + 10)
pdf.set_font('Arial', '', 10)
thankYouText="Thanks for being a Loyalty Member at the Arcadia Mobile Market! Based on your purchases last year, consider adding more Brown/White and Blue/Purple to your diet this season to make sure you get all the nutrients you need for a healthy diet!"
pdf.multi_cell(120, 5, thankYouText, 0, 0, 'J', False)

#Print white box next to it
pdf.set_y(pdf.get_y()-25)
pdf.set_x(pdf.get_x()+120)
boxText="Remember, the Arcadia Mobile Market doubles your SNAP, WIC, and SR FMNP purchases so you get even more great food for your money!"
pdf.multi_cell(50, 5, boxText, 1, 1, 'J', False)

#Draw Line
pdf.line(0, 80, 1000, 82)

# Draw Red Box
pdf.set_y(pdf.get_y()+20)
redX = pdf.get_x()
redY = pdf.get_y()
pdf.set_fill_color(255,0,0)
pdf.cell(80, 35, '', 0 , 1, 'C', True)
pdf.set_x(redX)
pdf.set_y(redY)
pdf.cell(80, 5, "Red", 0, 1, 'C', False)
redBoxText="Good for the heart and can help to lower the risk of heart disease. \n\nTIP: Ketchup is NOT a vegetable \nTRY: Beets, red pepper, red apples, tomatoes"
pdf.set_y(redY+5)
pdf.multi_cell(80, 5, redBoxText, 0, 'L', False)

#Draw Tan Box
pdf.set_y(pdf.get_y() - 30)
pdf.set_x(pdf.get_x() + 90)
tanY = pdf.get_y()
tanX = pdf.get_x()
pdf.set_fill_color(210, 180, 140)
pdf.cell(100, 35, '', 0 , 1, 'C', True)
pdf.set_x(tanX)
pdf.set_y(tanY)
pdf.cell(100, 5, "Brown/White", 0 , 1, 'C', False)
#pdf.set_y(tanY+5)
#tanBoxText="Great for removing toxins from the liver and reducing inflammation that accumulates in the body from the stresses of everyday life.\nTIP: Don’t confuse white-colored natural foods with highly processed foods that are white in color like rice, white bread, and pudding \nTRY: Garlic, jicama, parsnips, mushrooms, cauliflower"
#pdf.multi_cell(100, 5, tanBoxText, 0, 'L', True)

# Generates the PDF
customer_name = "Example Customer P2"
pdf.output(customer_name + ".pdf", 'F')