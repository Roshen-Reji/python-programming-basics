words = input("Enter the sentance ").split()
nwords= len(words)
i =0
new_word =""
while i < nwords:
  j = len(words[i])
  a = j-1
  while a >=0:
    alpha = (words[i])[a]
    new_word += alpha 
    a-=1
  i+=1
  new_word=new_word + " "
print("The reversed word is \"",new_word,"\"")