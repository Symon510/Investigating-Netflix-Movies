# Investigating-Netflix-Movies

This repository contains an analysis of Netflix movies, focusing on films released in the 1990s. The primary goal is to explore the distribution of movie durations and filter for action movies of that decade.

Table of Contents
Overview
Data Preparation
Analysis Steps
Visualization
Conclusion
Overview

This project analyzes a dataset of Netflix movies to understand the characteristics of films released during the 1990s. The analysis includes filtering for movies by release year and genre, as well as examining the duration distribution.

Data Preparation
Subset DataFrame for Movies:

Filter the dataset to include only movies (type == "Movie").
Filter by Release Year:

Further filter movies released between 1990 and 1999.
Analysis Steps
Visualize Duration Distribution:

Create a histogram to display the distribution of movie durations for the 1990s.
Filter Action Movies:

Extract action movies from the filtered dataset.
Count Short Movies:

Use a loop to count how many action movies have a duration of less than 90 minutes.
Visualization
A histogram is generated to show the distribution of movie durations in the 1990s.

Conclusion
This analysis provides insights into the characteristics of 1990s movies on Netflix, particularly focusing on action films and their durations. The code can be expanded to explore other genres or time periods.
