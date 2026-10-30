emp={
     "Name": "sooraj",
     'age':19,
     'ID':"XYZ",
     "Department":"IT",
     "salary":210000,
     'Bonus':20000
}
print("Keys:")
print(emp.keys())

print("Values")
print(emp.values())

print("Items:")
print(emp.items())

print("Name", emp.get("Name"))
print("Marks",emp.get('marks','not available'))

emp.update({"place":"Blr","Experience":"5Years"})
print("After Updating:")
print(emp) 
