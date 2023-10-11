sentence = "Hi i am Reef Zayed ,I have the cat is very nice , Reef is very frindliy "
word="Reef"
print("the number of sentence is :", len(sentence))
print("location of word in the setence: ",sentence.find(word))
print("appears in the sentence",sentence.count(word))
print (sentence.upper())
print (sentence.lower())
newSentence = sentence.replace(word,"Ruba")
print(newSentence)
print(sentence[-1])

