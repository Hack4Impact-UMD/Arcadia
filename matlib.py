import matplotlib.pyplot as plt
from customer import Customer

def pie_chart():
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    dict_pie = Customer.color
    sizes = [dict_pie["blue"], dict_pie["red"], dict_pie["yellow"], dict_pie["green"], dict_pie["light_green"], dict_pie["brown"]]

    fig, ax = plt.subplots()
    ax.pie(sizes, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig('piechart.jpg')

