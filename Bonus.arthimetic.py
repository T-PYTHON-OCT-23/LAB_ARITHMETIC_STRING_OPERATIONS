
advice = "if you can imagine it, you can achieve it. Have faith to achieve what you want"
word = "achieve"

print("the lenth of the word is: ", len(word))
print(f"location of {word} in the advice is in ", advice.find(word))
print(f"{word} appeard in the advice {advice.count(word)} times")

new_advice = advice.replace(word, "get")
print(new_advice)