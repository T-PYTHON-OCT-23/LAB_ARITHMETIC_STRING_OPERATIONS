sentence = "Python camp it's so helpful. It's a great apportunity for me"
word = "Python"

print(f"the lenth od sentance is: {len(sentence)}")
print(f"the index of the first occurrence of the {word} in the sentence is {sentence.find(word)}")
print (f"the {word} appers in the sentance for {sentence.count(word)} times")
print (sentence.upper())
print (sentence.lower())

sentence_update = sentence.replace(word, "Java")
print(sentence_update)

print(f"the last character of the sentence is {sentence[-1]}")
