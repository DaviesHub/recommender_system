import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')


def movie_recommender(movie_db, movie_descr):
    '''
    This function recommends a new movie for a users based on the word vector similarity of the description 
    of previously watched movies using python's SpaCy library.

    It takes in two arguments, the movie text file as param movie_db and movie description as movie_descr as strings.
    It returns the name of a movie as a string.
    '''

    # Compare similarity of movie description entered and movie descriptions in the dictionary and select the movie
    # with the highest description.
    descr_list = [] # Initialize list to hold all movie descriptions
    similarities = {} 

    for movie in movie_db.values():
        descr_list.append(movie)

    target_token = nlp(movie_descr)
    for descr in descr_list:
        descr_token = nlp(descr)
        sim = descr_token.similarity(target_token)
        similarities[descr] = sim

    # Check what movie has the highest sim
    del similarities[movie_descr]
    max_sim = max(similarities.values())
    for descr, sim in similarities.items():
        if sim == max_sim:
            recommended_movie_descr = descr

    for movie, descr in movie_db.items():
        if descr == recommended_movie_descr:
            recommended_movie = movie

    return recommended_movie


# Reading in movie.txt file containing movies and storing movies and descriptions in a dictionary.
movie_dict = {} # Empty list to store movies
fhand = open("movies.txt", "r")
for line in fhand:
    line = line.split(":") # Splits each movie name and description
    movie_dict[line[0].casefold()] = line[1] # Stores movie name and description in dictionary

# Request previously watched movie (pwm) and get the previously watched movie description (pwmd) from the dictionary
while True:
    pwm = input('''Enter the title of a previously watched movie below. Enter e to exit:
        # enter title: ''').casefold()

    if pwm in movie_dict.keys():
        pwmd = movie_dict[pwm]
        movie = movie_recommender(movie_dict, pwmd)
        print("The most similar movie is:", movie)

    elif pwm == "e":
        print('\nGoodbye!!!')
        exit()

    else:
        print("Movie not found. Enter movie in our record or enter e to exit")
    