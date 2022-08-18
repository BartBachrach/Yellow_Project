# Movie Finder
### Movie Recommendation Engine with:
  - Python
  - Machine Learning
  - Amazon AWS
  - PostgreSQL
  - Flask
  - HTML
  - Heroku

## ETL
The team used the MovieLens 25M Dataset (https://grouplens.org/datasets/movielens/25m/) as a starting point for our movie recommendation tool. First, we loaded the movies.csv and links.csv into Jupyter Notebooks, merged the two data frames into one, then created a movies_data_complete.csv. Next, we loaded the ratings.csv into Jupyter Notebooks, then we dropped unneeded columns, and averaged the ratings for each movie. We then merged the movies_data_complete and ratings data frames into an updated movies_data_complete.csv. Finally, we created a data frame consisting of only the top genome score for each movie, then merged the top genome data frame into the movies_data_complete data frame to update our movies_data_complete.csv that we will use for our machine learning model.

The project required the team to identify, clean, filter and repackage data from multiple .csv files that will allow our machine learning model to more easily train and produce useful insights for our movie recommendation tool. 

## Machine Learning Model
In order to cluster the movies, we found the top most-relevant tag for each movie; with 1128 tags and over fifty thousand movies, there were going to be repeated top-tags. We merged the top tags to our dataframe that contained the movie name, genre, and other metadata and created a pivot table with boolean values for each tag, with the genres as the columns. We converted that table to a csv file and used the elbow curve method to determine the optimal number of clusters was five. We then ran the KMeans algorithm on that dataframe and clustered our movies. The clusters were sci-fi movies, suspense, critically acclaimed, animation, and the final cluster included everything else, as it clustered by the most repeated tags. We then used the clusters to recommend second movies from the same cluster for our recommendation website.

![this is an image](https://github.com/BartBachrach/Yellow_Project/blob/main/Elbow_Curve.png)

We further attempted to experiment with more clusters, but those simply represented the next most popular tags from what was already clustered, and did not represent a true multivariate cluster, and for the purposes of this project, we limited the number of clusters to five for simplicitys sake. 

## Database
We used Amazon RDS to create a PostgreSQL DB Instance. We then connected our Amazon RDS to the PostgreSQL database using pgAdmin4. Lastly, we used PySpark to import or data into a SQL table.


## User Interface
Using a Flask application and HTML files, we created a website that we deployed from Heroku. The main page has three drop-down menus that filter the data based on the user's selections. The options for types of movies are based on the five clusters created from our machine learning model. When you click search, it takes you to a recommendations page where one movie title is displayed that matches your search specifications. The address for our website is: https://yellow-project.herokuapp.com/.

<img width="1440" alt="Screen Shot 2022-08-17 at 5 52 40 PM" src="https://user-images.githubusercontent.com/100643519/185257786-5fd3ca3e-09ca-444e-bb53-f01d884a3baf.png">

<img width="1440" alt="Screen Shot 2022-08-17 at 5 52 55 PM" src="https://user-images.githubusercontent.com/100643519/185257819-54cc3465-f454-455f-87f0-442fd7c8445e.png">

<img width="1440" alt="Screen Shot 2022-08-17 at 5 53 08 PM" src="https://user-images.githubusercontent.com/100643519/185257859-bb54739d-d0a6-4aed-a33b-c81ba483bbdb.png">
