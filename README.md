# Yellow_Project
## Movie Recommendations
Our goal is to produce a tool to recommend lesser-known movies to streaming customers. We will employ a machine-learning model to group movies together based on multivariate factors, including the most relevant genome tag and genre, thus grouping similar movies. Our strategy is to recommend movies to users based on a selection of criteria, and recommend a second movie from the same cluster as an alternative.

## User Interface
We will create a JavaScript file and HTML file that will be hosted on a website with a dropdown menu for a user to select a number of criteria, such as ratings, popularity, and genre. The code will then recommend one popular movie, and one similar, lesser-known movie that the user might enjoy. 

# Machine Learning Model
In order to cluster the movies, we found the top most-relevant tag for each movie; with 1128 tags and over fifty thousand movies, there were going to be repeated top-tags. We merged the top tags to our dataframe that contained the movie name, genre, and other metadata and created a pivot table with boolean values for each tag, with the genres as the columns. We converted that table to a csv file and used the elbow curve method to determine the optimal number of clusters was five. We then ran the KMeans algorithm on that dataframe and clustered our movies. The clusters were sci-fi movies, suspense, critically acclaimed, animation, and the final cluster included everything else, as it clustered by the most repeated tags. We then used the clusters to recommend second movies from the same cluster for our recommendation website. 
