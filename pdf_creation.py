from fpdf import FPDF 
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Adds the title
title="2021 Arcadia Mobile Market"
starting_x = pdf.get_x()
pdf.set_fill_color(0, 160, 0)
pdf.cell(170, 20, '', 0, 0, 'C', True)
pdf.set_x(starting_x)
pdf.cell(170, 10, title, 0, 0, 'C', False)

# Adds the purchase report below title
member="Purchase Report: Member #12"
pdf.set_font('Arial', 'B', 12)
pdf.cell(170, 10, member, 0, 1, 'C', False)

visits = 9
servings =170
total = "$94.65"

pdf.cell(55, 10, f"Visits: {visits}", 0, 0, 'C', False)
pdf.cell(55, 10, f"Servings: {servings}", 0, 0, 'C', False)
pdf.cell(55, 10, f"Total: {total}", 0, 1, 'C', False)

starting_x = pdf.get_x()
starting_y = pdf.get_y()
pdf.set_y(pdf.get_y() + 5)
pdf.set_fill_color(0, 190, 0)
pdf.cell(70, 40, '', 0, 0, 'C', True)
pdf.set_x(starting_x)
pdf.cell(70, 10, "EAT A RAINBOW", 0, 1, 'C', False)
pdf.set_font('Arial', '', 8)
rainbow_text = "An easy way to eat right is to fill at least half your plate with vegetables and fruits, and to try to eat all the colors of the rainbow every day, especially lots of greens. Different colors of produce have different nutrients, so eating a rainbow means you get as many as possible."
pdf.multi_cell(70, 5, rainbow_text, 0, 'L', False)


pdf.set_y(pdf.get_y() + 5)
pdf.set_fill_color(204, 85, 0)
pdf.set_font('Arial', 'B', 12)
pdf.cell(70, 16*5 + 30, '', 0, 0, 'C', True)
pdf.set_x(starting_x)
pdf.cell(70, 10, "YOUR 2021 PURCHASES", 0, 1, 'C', False)
pdf.set_font('Arial', '', 10)
purchases = {
                'Asian Pears' : '6.25',
                'Blueberries' : '3.50',
                'Broccoli' : '1.95',
                'Cabbage' : '8.59',
                'Cantaloupe' : '3.00',
                'Corn' : '3.96',
                'Cucumber' : '1.95',
                'Garlic' : '1.00',
                'Kale' : '4.00',
                'Okra (Pound)' : '3.72',
                'Peaches' : '20.72',
                'Peppers (Bell)' : '2.40',
                'Plums' : '3.75',
                'Potatoes' : '5.25',
                'Potatoes (Sweet)' : '5.01',
                'Tomatoes (Red)' : '9.50',
                'Watermelon (Small)' : '6.10'
            }

for purchase in purchases:
    pdf.cell(35, 5, purchase, 0, 0, 'L', False)
    pdf.cell(35, 5, f"${purchases[purchase]}", 0, 1, 'L', False)

second_col_x = starting_x + 80
pdf.set_xy(second_col_x, starting_y + 5)
pdf.set_fill_color(234,182,118)
pdf.cell(90, 40, '', 0, 0, 'C', True)
pdf.set_x(second_col_x)
pdf.cell(90, 10, "Your Personal 2021 Eating Rainbow", 0, 1, 'C', False)
rainbow_info="THIS IS YOUR PERSONAL EATING RAINBOW CHART, BASED ON THE PERCENTAGE OF COLORS OF PRODUCE YOU PURCHASED AT THE MOBILE MARKET LAST YEAR. TURN THE PAGE FOR SUGGESTIONS ON WHAT VEGETABLES TO ADD TO MAKE YOUR DIET EVEN HEALTHIER!"
pdf.set_x(second_col_x)
pdf.multi_cell(90, 5, rainbow_info, 0, 'L', False)
pdf.set_y(pdf.get_y() + 5)
pdf.image("./piechart.png", second_col_x + 12 , starting_y + 45, 70, 60, 'png')

total_spent = 82.20
pdf.set_xy(second_col_x, starting_y + 110)
pdf.set_fill_color(0, 190, 0)
pdf.cell(90, 50, '', 0, 0, 'C', True)
spent_info=f"You spent ${total_spent} in nutrition benefits at the Mobile Market in 2017, including:"
pdf.set_xy(second_col_x, starting_y + 115)
pdf.set_font('Arial', '', 14)
pdf.multi_cell(90, 5, spent_info, 0, 'C', False)

benefits = {
                'SNAP' : '0.00',
                'PPP' : '64.20',
                'Loyalty' : '18.00',
                'WIC' : '0.00',
                'Sr FMNP' : '0.00',
            }

pdf.set_y(pdf.get_y() + 5)
for benefit in benefits:
    pdf.set_x(second_col_x)
    pdf.cell(45, 5, benefit, 0, 0, 'L', False)
    pdf.cell(45, 5, f"${benefits[benefit]}", 0, 1, 'L', False)

# Generates the PDF
customer_name = "Example Customer"
pdf.output(customer_name + ".pdf", 'F')
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html