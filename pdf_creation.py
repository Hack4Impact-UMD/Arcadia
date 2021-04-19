from fpdf import FPDF 
pdf = FPDF('P', 'mm', 'Letter')
pdf.set_margins(15, 15, -1)

# Adds the header to the top of the page (title + member number)
def add_header():
    # Adds the title
    title="2021 Arcadia Mobile Market"
    pdf.set_x(15)
    starting_x = pdf.get_x()
    pdf.set_fill_color(115, 170, 110)
    pdf.cell(186, 20, '', 0, 0, 'C', True)
    pdf.set_x(starting_x)
    pdf.cell(186, 10, title, 0, 1, 'C', False)
    # Adds the purchase report below title
    member="Purchase Report: Member #12"
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(186, 10, member, 0, 1, 'C', False)

# Adds the Arcadia contact information on one line at the bottom
def add_contact_info():
    pdf.set_y(245)
    pdf.cell(62, 5, "www.arcadiafood.org", 0, 0, 'C', False)
    pdf.cell(62, 5, "571-384-8845", 0, 0, 'C', False)
    pdf.cell(62, 5, "info@arcadiafood.org", 0, 1, 'C', False)
    

# FIRST PAGE
pdf.add_page()
pdf.set_font('Arial', 'B', 18)

# Header
add_header()
starting_x = 15

# Adds the visits, servings, and total on one line below the header
visits = 9
servings =170
total = "$94.65"
pdf.cell(62, 10, f"Visits: {visits}", 0, 0, 'C', False)
pdf.cell(62, 10, f"Servings: {servings}", 0, 0, 'C', False)
pdf.cell(62, 10, f"Total: {total}", 0, 1, 'C', False)

pdf.line(pdf.get_x(), pdf.get_y(), pdf.get_x() + 186, pdf.get_y())

# Adds the eat a rainbow box
starting_y = pdf.get_y()
pdf.set_y(pdf.get_y() + 5)
pdf.set_fill_color(138, 182, 214)
pdf.cell(85, 55, '', 0, 0, 'C', True)
pdf.set_x(starting_x)
pdf.cell(85, 10, "EAT A RAINBOW", 0, 1, 'C', False)
pdf.set_font('Arial', '', 12)
rainbow_text = ("An easy way to eat right is to fill at least half your plate "
                "with vegetables and fruits, and to try to eat all the colors of "
                "the rainbow every day - especially lots of greens. Different colors "
                "of produce have different nutrients, so eating a rainbow means you "
                "get as many as possible.")
pdf.set_x(pdf.get_x() + 5)
pdf.multi_cell(75, 5, rainbow_text, 0, 'J', False)


# Adds the purchases box
pdf.set_y(pdf.get_y() + 10)
pdf.set_fill_color(204, 85, 0)
pdf.set_font('Arial', 'B', 14)
pdf.cell(85, 16*5 + 50, '', 0, 0, 'C', True)
pdf.set_x(starting_x)
pdf.cell(85, 10, "YOUR 2021 PURCHASES", 0, 1, 'C', False)
pdf.set_font('Arial', '', 12)
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
    pdf.set_x(pdf.get_x() + 15)
    pdf.cell(40, 5, purchase, 0, 0, 'L', False)
    pdf.cell(40, 5, f"${purchases[purchase]}", 0, 1, 'L', False)

# Adds the personal eating rainbow information box
second_col_x = starting_x + 96
pdf.set_xy(second_col_x, starting_y + 5)
pdf.set_fill_color(234,182,118)
pdf.cell(90, 45, '', 0, 0, 'C', True)
pdf.set_x(second_col_x)
pdf.set_font('Arial', 'B', 14)
pdf.cell(90, 10, "Your Personal 2021 Eating Rainbow", 0, 1, 'C', False)
rainbow_info=("This is your personal eating rainbow chart, based on the "
              "percentage of colors of produce you purchased at the mobile "
              "market last year. Turn the page for suggestions on what "
              "vegetables to add to make your diet even healthier!")
pdf.set_x(second_col_x + 5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(80, 5, rainbow_info, 0, 'J', False)
pdf.set_y(pdf.get_y() + 5)
pdf.image("./piechart.png", second_col_x + 10 , starting_y + 55, 80, 75, 'png')

# Adds the benefits information box
total_spent = 82.20
pdf.set_xy(second_col_x, starting_y + 135)
pdf.set_fill_color(203, 150, 139)
pdf.cell(90, 60, '', 0, 0, 'C', True)
spent_info=f"You spent ${total_spent} in nutrition benefits at the Mobile Market in 2017, including:"
pdf.set_xy(second_col_x, starting_y + 140)
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
    pdf.set_x(second_col_x + 12)
    pdf.cell(45, 5, benefit, 0, 0, 'L', False)
    pdf.cell(45, 5, f"${benefits[benefit]}", 0, 1, 'L', False)

# Adds Arcadia's contact info
add_contact_info()

# SECOND PAGE
pdf.add_page()
pdf.set_font('Arial', 'B', 18)

# Header
add_header()
starting_x = 15

# Adds thank you text
pdf.set_font('Arial', '', 12)
pdf.set_y(pdf.get_y() + 5)
thank_you_text=("Thanks for being a Loyalty Member at the Arcadia Mobile Market! "
            "Based on your purchases last year, consider adding more Brown/White "
            " and Blue/Purple to your diet this season to make sure you get all "
            " the nutrients you need for a healthy diet!")
pdf.multi_cell(120, 5, thank_you_text, 0, 'J', False)

# Adds the benefits reminder box to the right of the thank you text
pdf.set_y(pdf.get_y() - 25)
pdf.set_x(pdf.get_x() + 125)
boxText="Remember, the Arcadia Mobile Market doubles your SNAP, WIC, and SR FMNP purchases so you get even more great food for your money!"
pdf.multi_cell(61, 5, boxText, 1, 1, 'J', False)

pdf.line(pdf.get_x(), pdf.get_y() + 5, pdf.get_x() + 186, pdf.get_y() + 5)

# Adds the red box
pdf.set_y(pdf.get_y() + 10)
redX = pdf.get_x()
redY = pdf.get_y()
pdf.set_fill_color(255, 0, 0)
pdf.cell(70, 47, '', 0 , 1, 'C', True)
pdf.set_x(redX)
pdf.set_y(redY)
pdf.set_font('Arial', 'B', 14)
pdf.cell(70, 10, "RED", 0, 1, 'C', False)
red_box_text=("Good for the heart and can help to lower the risk of heart disease.\n\n"
            "TIP: Ketchup is NOT a vegetable\n"
            "TRY: Beets, red pepper, red apples, tomatoes")
pdf.set_xy(redX + 2, redY + 10)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(66, 5, red_box_text, 0, 'L', False)

# Adds the brown/white box
pdf.set_y(redY)
pdf.set_x(pdf.get_x() + 75)
tanY = pdf.get_y()
tanX = pdf.get_x()
pdf.set_fill_color(210, 180, 140)
pdf.cell(111, 47, '', 0 , 1, 'C', True)
brown_box_text=("Great for removing toxins from the liver and reducing inflammation "
              "that accumulates in the body from the stresses of everyday life.\n"
              "TIP: Don't confuse white-colored natural foods with highly processed "
              "foods that are white in color like rice, white bread, and pudding\n"
              "TRY: Garlic, jicama, parsnips, mushrooms, cauliflower")
pdf.set_xy(tanX, tanY)
pdf.set_font('Arial', 'B', 14)
pdf.cell(111, 10, "BROWN/WHITE", 0 , 1, 'C', False)
pdf.set_xy(tanX + 2, pdf.get_y())
pdf.set_font('Arial', '', 12)
pdf.multi_cell(107, 5, brown_box_text, 0, 'L', False)

# Adds the green/light green box
greenY = tanY + 52
pdf.set_y(greenY)
tanY = pdf.get_y()
tanX = pdf.get_x()
pdf.set_fill_color(0, 180, 0)
pdf.cell(125, 62, '', 0 , 1, 'C', True)
green_box_text=("Great for fighting cancer and maintaining strong bones and joints.\n\n"
                "TIP: When eating out, most salads are made from iceberg lettuce which "
                "is very light green in color and contains very little nutrition. Instead "
                "ask for a salad made from romaine, spinach or kale which is much more nutritious.\n"
                "TRY: Kale, spinach, asparagus, mustard greens, arugulaand pudding\n"
                "TRY: Garlic, jicama, parsnips, mushrooms, cauliflower")
pdf.set_xy(tanX, tanY)
pdf.set_font('Arial', 'B', 14)
pdf.cell(125, 10, "GREEN/LIGHT GREEN", 0 , 1, 'C', False)
pdf.set_xy(tanX + 2, pdf.get_y())
pdf.set_font('Arial', '', 12)
pdf.multi_cell(121, 5, green_box_text, 0, 'L', False)

# Adds the blue/purple box
purpleY = greenY + 66
pdf.set_y(purpleY)
tanY = pdf.get_y()
tanX = pdf.get_x()
pdf.set_fill_color(163, 88, 232)
pdf.cell(125, 37, '', 0 , 1, 'C', True)
purple_box_text=("Helps to stabilize blood pressure, lower cholesterol, and improve memory.\n\n"
                "TRY: Purple potato, red cabbage, blueberries, eggplant, plums")
pdf.set_xy(tanX, tanY)
pdf.set_font('Arial', 'B', 14)
pdf.cell(125, 10, "BLUE/PURPLE", 0 , 1, 'C', False)
pdf.set_xy(tanX + 2, pdf.get_y())
pdf.set_font('Arial', '', 12)
pdf.multi_cell(121, 5, purple_box_text, 0, 'L', False)

# Adds the orange/yellow box
yellowY = greenY
pdf.set_y(yellowY)
tanY = pdf.get_y()
tanX = pdf.get_x()
pdf.set_fill_color(223, 226, 43)
pdf.set_xy(tanX + 130, tanY)
pdf.cell(56, 101, '', 0 , 1, 'C', True)
yellow_box_text=("High in Vitamin C which helps boost the immune system. "
                 "They are also important for eye and vision health = so eat those carrots!\n\n"
                 "TRY: Carrots, winter squash, sweet potatoes, yellow peppers")
pdf.set_font('Arial', 'B', 14)
pdf.set_xy(tanX + 132, tanY)
pdf.cell(56, 10, "YELLOW", 0 , 1, 'C', False)
pdf.set_font('Arial', '', 12)
pdf.set_xy(tanX + 132, tanY + 10)
pdf.multi_cell(52, 5, yellow_box_text, 0, 'L', False)

# Adds Arcadia's contact info
add_contact_info()

# Generates the PDF using the customer's name
customer_name = "Example Customer"
pdf.output(customer_name + ".pdf", 'F')