# Importing pandas and matplotlib 

import pandas as pd
import matplotlib.pyplot as plt

# Reading netflix CSV as a DataFrame
netflix_df = pd.read_csv(r"C:\Users\symon\Downloads\netflix_data.csv")

# Subset DataFrame for column name "type" were the rows are "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Filter to only keep movies released in 1990
# Filtering movies that were released before 1990 
subset = netflix_subset[(netflix_subset["release_year"] >= 1990)]

# Filtering movies that were released on or after 2000
movies_1990s = subset[(subset["release_year"] < 2000 )]

#print(movies_1990s)

# Visualize the duration column of filtered data to see distribution of movie duration
plt.hist(movies_1990s["duration"])
plt.title("distribution of movie duration in the 1990s")
plt.xlabel("Duration(minutes)")
plt.ylabel("Number of Movies")
plt.show()

duration = 100

# Filter data again to keep only action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use For loop and a counter to count how many movies where there in the 90s
# Start counter
short_movie_count = 0

# Iterate over rows and columns of the DataFrame to check if the duration is less than 90
for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count


print(short_movie_count)
