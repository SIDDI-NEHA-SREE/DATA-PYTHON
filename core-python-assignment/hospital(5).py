def searchdisease(p, d):
    result = []
    for i in p:
        if i["Disease"].lower() == d.lower():
            result.append(i["Name"])
    return result

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search = "Flu"
print(f"Patients with {search}: {searchdisease(patients, search)}")