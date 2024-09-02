# Movie_recommender_system
# How to run.
<b>
Download the repository then open the terminal and run the command 
streamit run app.py (please see that streamlit is already installed in the system if not then run the command pip install streamlit)

# Approach and working of project
I made this movie recommender system using 5000 movie dataset 
The very first step is preprocessing of my data and merging the movies and credits dataframes together.
Then I removed the irrelevant data points and the duplicate values.
In the end i kept in my data only movie_id, movie_name, director, top 3 crew and the casts, then created a single column overview for the cast, the crew and the director.
By using vectorization and cosine similarity created a 4806*4806 similarity matrix which shows the cosine angle between any two vectors or movies.
For any given movie fetched the top 5 vectors(movies) which are nearest to that particular movie and displayed them to user.
Using my api key and movie id for each respective movie I fetched out the posters for the recommended movies from the TMDB website.
Used streamlit for the frontend.
