# Yellow_Project
## Movie Recommendations
Our goal is to create a website that makes movie recommendations based on user input. We will employ a machine-learning model to cluster similar movies based on the criteria we choose for the search filters on the website.

## ETL
We used the MovieLens 25M Dataset (https://grouplens.org/datasets/movielens/25m/) as a starting point for our movie recommendation tool. First, we loaded the movies.csv and links.csv into Jupyter Notebooks, merged the two data frames into one, then created a movies_data_complete.csv. Next, we loaded the ratings.csv into Jupyter Notebooks, then we dropped unneeded columns, and averaged the ratings for each movie. Finally, we merged the movies_data_complete and ratings data frames into an updated movies_data_complete.csv file that we will use for our machine learning model.

## Web Design Prototype
[Web_Design_Sketch.pdf](https://github.com/BartBachrach/Yellow_Project/files/9176834/Web_Design_Sketch.pdf)

## User Interface
We will create a JavaScript file and HTML file that will be hosted on a website with a dropdown menu for a user to select a number of criteria, such as ratings, popularity, and genre. The code will then recommend one popular movie, and one similar, lesser-known movie that the user might enjoy.

https://github.com/BartBachrach/Yellow_Project/blob/Dev_Frontend/templates/index.html

<img width="1552" alt="Screen Shot 2022-07-30 at 6 02 15 PM" src="https://user-images.githubusercontent.com/100643519/182002956-f37e5136-c338-41cd-9f56-d9c406859bfc.png">
