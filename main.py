import wolframalpha
  
app_id = "6HH4YA-KLRHRL6JVW"     #API Key

client = wolframalpha.Client(app_id)  #Verification of API key

question = input('Question ')    #Input from user
  
res = client.query(question)     #Respone from the website
  
answer = next(res.results).text  #Storing the result
  
print(answer)