fulltext = input("Paste the text:")
alphabet = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"x":0,"y":0,"z":0,"Ã¥":0,"Ã¤":0,"Ã¶":0}
for letter in alphabet:
    alphabet[letter] = fulltext.count(letter)
print("Ceasar ciper analysis:\n"+str(alphabet))

n=3
while n<7:
    i=n-1
    newtext = ""
    while i<len(fulltext):
        newtext = newtext+fulltext[i]
        i = i+n
    for letter in alphabet:
        alphabet[letter] = newtext.count(letter)
    print("Vignere ciper analysis("+str(n)+"):\n"+str(alphabet))
    n=n+1
