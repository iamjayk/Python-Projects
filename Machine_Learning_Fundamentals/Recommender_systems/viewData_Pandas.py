# Viewing Dataset data on a webpage using Pandas

import pandas
import webbrowser
import os

# Reading dataset into a data table using Pandas
data_table = pandas.read_csv("Movie_ratings_data_set.csv")

# Creating a webpage view of data 
html = data_table[0:100].to_html()

# Saving html to a temp file
with open("data.html", "w") as f:
     f.write(html)
     
# Opening the webpage in a browser
full_filename = os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))
