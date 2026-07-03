#data type is type of data
#string, int, float, boolean

#create a dictionary
Score={
    #key-value pair
    'Zainab':20,
    'Hiba':19,
    'aarav':10,
    'Alia':20,


}

print(Score)
print(Score['Zainab'])

#show all keys 
print(Score.keys())
print(Score.values())

#delete
del(Score['Alia'])
print(Score)

#update score
Score['Aarav']=13
print(Score)