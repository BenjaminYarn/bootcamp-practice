###NLP basics programme
import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = nlp("Why is my cat on the car")

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#The example file when run with the simpler language model ‘en_core_web_sm'
#Similar sentences were rated as less similar
#Less similar sentences (recipes vs complaints) gave much more erratic
#results, including high and low similarity ratings