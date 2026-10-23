emp={
     "Name": "Sumit",
     'age':19,
     'ID':"XYZ",
     "Department":"IT",
     "salary":210000,
     'Bonus':20000
}
emp["Job"]="Software developer"
print("After Adding")
print(emp)

emp["age"]=18
print("After Updating")
print(emp)

del emp["Bonus"]
print("After deleting:")
print(emp)

