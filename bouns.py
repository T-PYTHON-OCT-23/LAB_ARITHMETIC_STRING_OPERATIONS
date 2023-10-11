sentence = "Dana is the most beautiful girl, Dana is 5 months old now"
word = "Dana"
print("Length of sentence = ", len(sentence))
print(f"location of {word} in:{sentence.find(word)}")
print(f"The name Dana appears {sentence.count(word)} times" )
print(f"sentence in uppercase {sentence.upper()}")
print(f"sentence in lowercase {sentence.lower()}")

newWord= sentence.replace(word , "Ebtesam",)
print(newWord)
print(f"last character of the sentenceis: {sentence[-1]}")