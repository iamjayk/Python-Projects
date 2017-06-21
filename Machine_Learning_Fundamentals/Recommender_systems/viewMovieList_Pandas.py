# Reading dataset to a webpage with Predefined Index columns

import pandas
import webbrowser
import os

# Reading dataset into data table using Pandas
data_table = pandas.read_csv("movies.csv", index_col="movie_id")

# Creating a webpage view of data
html = data_table.to_html()

# Saving the html to temp file
with open("movie_list.html", "w") as f:
    f.write(html)
    
# Opening webpage in web browser
full_filename = os.path.abspath("movie_list.html")
webbrowser.open("file://{}".format(full_filename))
