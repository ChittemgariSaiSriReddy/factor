def alphabatical_order(word):
    sorting=sorted(word)
    join=''.join(sorting)
    print(sorting)
    return join


word=input("Enter a Word : ")
print(alphabatical_order(word))