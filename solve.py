def StringChallenge(sen):
 
  words = sen.split()

  lw = max(words,key=len)
  
  return lw

# keep this function call here 
# print(StringChallenge(input()))
