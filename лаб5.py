lines = 0
words = 0
characters = 0
charactersProb = 0
with open(r"E:\test.txt", "r") as file:
    for line in file:
        lines = lines+1
        wordlist = line.split()
        words += len(wordlist)
        charactersProb += len(line)
        characters += sum(len(word) for word in wordlist)
        print("число строк =",lines)
        print("число слов =",words)
        print("число символов (без пробелов) =",characters)
        print("число символов (с пробелами) =",charactersProb)


       
