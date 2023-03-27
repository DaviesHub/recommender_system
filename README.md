# A Movie Recommender System Using SpaCy Word Vector Similarity of the Movie Description

## Contents
1. Description
2. Features
3. Package Requirements
4. Installation & Usage
5. Running the Application with Docker
6. Contributions
7. References

## Description
This is a Python script that recommends movies to users based on the similarity of the descriptions of previously watched movies. The script uses Spacy, a natural language processing library, to compare the similarity of movie descriptions and recommends the movie with the highest similarity to the user.

## Features
- Recommends a new movie to users based on previously watched movies

- Uses Spacy for natural language processing

- Command-line interface for easy usage

- Containerized for easy deployment using Docker

## Package Requirements
Package requirements for this app can be seen on the requirements.txt file. Install the required packages by running the
following command on the command line:
'pip install -r requirements.txt'

## Installation & Usage
To use the script, follow these steps:

1. Clone the repository to your local machine using git clone git clone git@github.com:Username/RepositoryName.git
2. Install the required packages by running pip install -r requirements.txt in the project directory
3. Run the script using python movie_recommender.py
4. Enter the title of a previously watched movie when prompted and press Enter
5. The script will recommend a new movie based on the similarity of the descriptions of previously watched movies

## Running the Application with Docker
To run the script using Docker, follow these steps:

1. Make sure Docker is installed on your machine
2. Build the Docker image using docker build -t image-name.
3. Run the Docker container using docker run -it image-name

## Contributions
Contributions to this script are welcome. Please fork the repository, make changes, and submit a pull request.

## References
Spacy documentation: https://spacy.io/
Docker documentation: https://docs.docker.com/
Python documentation: https://docs.python.org/