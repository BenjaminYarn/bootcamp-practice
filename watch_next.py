####Programme to compare movies
import spacy
nlp = spacy.load('en_core_web_sm')

planet_hulk =  nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.")
 
with open('movies.txt', 'r') as file:
    for line in file:
        movie, description = line.split(' :')
        similarity = nlp(description).similarity(planet_hulk)
        print(f"{movie} similarity to Planet Hulk: {similarity}")