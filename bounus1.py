print("_"*15)

phrase= "Basel is the a good boy . he is like watch superman movie. Basel loves fantasy movies and like to watch planets and stars."
word= "Basel"
print("the number of character in tht pharse is:" , len(phrase))
print(f"location of {word} in the pharse is in ", phrase.find(word))
print(f"appeard in the phrase {phrase.count(word)}times")
new_phrase = phrase.replace(word,"Muhammed",)
print(new_phrase)