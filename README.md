# Yellow_Project
## Movie Recommendations
Our goal is to create a website that makes movie recommendations based on user input. We will employ a machine-learning model to cluster similar movies based on the criteria we choose for the search filters on the website.

## ETL
The team used the MovieLens 25M Dataset (https://grouplens.org/datasets/movielens/25m/) as a starting point for our movie recommendation tool. First, we loaded the movies.csv and links.csv into Jupyter Notebooks, merged the two data frames into one, then created a movies_data_complete.csv. Next, we loaded the ratings.csv into Jupyter Notebooks, then we dropped unneeded columns, and averaged the ratings for each movie. We then merged the movies_data_complete and ratings data frames into an updated movies_data_complete.csv. Finally, we created a data frame consisting of only the top genome score for each movie, then merged the top genome data frame into the movies_data_complete data frame to update our movies_data_complete.csv that we will use for our machine learning model.

The project required the team to identify, clean, filter and repackage data from multiple .csv files that will allow our machine learning model to more easily train and produce useful insights for our movie recommendation tool. 

## Machine Learning Model
In order to cluster the movies, we found the top most-relevant tag for each movie; with 1128 tags and over fifty thousand movies, there were going to be repeated top-tags. We merged the top tags to our dataframe that contained the movie name, genre, and other metadata and created a pivot table with boolean values for each tag, with the genres as the columns. We converted that table to a csv file and used the elbow curve method to determine the optimal number of clusters was five. We then ran the KMeans algorithm on that dataframe and clustered our movies. The clusters were sci-fi movies, suspense, critically acclaimed, animation, and the final cluster included everything else, as it clustered by the most repeated tags. We then used the clusters to recommend second movies from the same cluster for our recommendation website.

## Database
We used PySpark and PostgreSQL to load our data into an Amazon RDS instance.

https://github.com/BartBachrach/Yellow_Project/blob/Database/movie_data.ipynb

https://github.com/BartBachrach/Yellow_Project/blob/Database/sample_table_schema.txt

## Web Design Prototype
[Web_Design_Sketch.pdf](https://github.com/BartBachrach/Yellow_Project/files/9176834/Web_Design_Sketch.pdf)

## User Interface
We will create a Flask app and HTML file that will be hosted on a website with a dropdown menu for a user to select a number of criteria, such as ratings, popularity, and genre. The code will then recommend one popular movie, and one similar, lesser-known movie that the user might enjoy.

https://github.com/BartBachrach/Yellow_Project/blob/Dev_Frontend/templates/index.html

<img width="1552" alt="Screen Shot 2022-07-30 at 6 02 15 PM" src="https://user-images.githubusercontent.com/100643519/182002956-f37e5136-c338-41cd-9f56-d9c406859bfc.png">
