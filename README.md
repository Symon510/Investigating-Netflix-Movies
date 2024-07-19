# Investigating-Netflix-Movies

This repository contains an analysis of Netflix movies, focusing on films released in the 1990s. The primary goal is to explore the distribution of movie durations and filter for action movies of that decade.

Overview :
This project analyzes a dataset of Netflix movies to understand the characteristics of films released during the 1990s. The analysis includes filtering for movies by 'release year','genre' and the distribution of movie duration. 

Data preparation :
We filter the DataFrame to inlcude only the column name 'type' where the rows only show 'Movie' 

![image](https://github.com/user-attachments/assets/970eac8c-b3e8-4eb2-9a3a-4a8c4a203f06)

we filter by 'release_year' to only keep movies released in 1990, further we only filter movies released between 1990 and 2000
Before 1990 :

![image](https://github.com/user-attachments/assets/3572ae28-8094-444c-b666-d4e5a2ee6709)

On or After 2000 :

![image](https://github.com/user-attachments/assets/3636d56d-7820-454d-8629-be2c2c0f2ab9)

Data analysis :

We now visualize the 'duration' column of the filter data to know the distribution of movie duration using a histogram from matplotlib.

![image](https://github.com/user-attachments/assets/707a0e85-8394-44d6-abe4-3388ff36b12e)

It is oberserved that the most frequent movie duration during the 1990's is 100 minutes (duration)

We now filter only the action movies from the filtered datset 

![image](https://github.com/user-attachments/assets/8f7f9004-8b28-4809-a03d-81a240d80430)

Used a loop to find the count of all the short actions movies which had a duration of less than 90 minutes :

The following result gave a count of 7 short action movies in the dataset

Conclusion :

The analysis provides insgights about the 1990's movies on Netflix, particularly focusing on actions films and their durations.


