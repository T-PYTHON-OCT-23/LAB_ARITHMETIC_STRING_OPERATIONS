
sentence:str = "my name is danah ,I'm a fresh graduate from Princess nora university"
word : str = " danah"

print("The Length in sentence is : " , len(sentence))
print()
print(f"location of{word} in sentence is in " , sentence.find(word))
print()
print(f"{word} appeard in the sentence {sentence.count(word)} times ")
print()

print(" uppercase letters : " , sentence.upper())
print(" lowercase letters : " , sentence.lower())

print()
print(sentence.replace( word , " nada"))

print()
print("Last character is :", sentence[len(sentence)-1])
