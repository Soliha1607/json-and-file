"""
#task1
import json
data = {
    "name": "Soliha",
    "age": 16,
    "name1": "Someone",
    "age1": 21
}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print(f"Name: {data['name']}, Age: {data['age']}")
print(f"Name: {data['name1']}, Age: {data['age1']}")
"""
"""
#task2
import json
date = {
    "name": "Soliha",
    "age": 16,
    "name1": "Someone",
    "age1": 21
}
with open('date.json', 'w') as file:
    json.dump(date, file, indent=4)
json_string = '{"name": "Somebody", "age": 5}'
with open("date.json", "w") as file:
   json.dump(json.loads(json_string), file, indent=4)
"""
""""
#task3
with open('tasks.txt', 'w') as matn_fayl: 
    matn_fayl.write(f"Project tugatish kere!\n")
    matn_fayl.write("Examga tayyorlanish kere\n")
    matn_fayl.write("Yana nimadur qilarsan\n")
"""
"""
#task4
file_name = "books.txt"
with open(file_name, "w") as file:
    file.write("Harry Potter, J.K. Rowling\n")
    file.write("The Hobbit, J.R.R. Tolkien\n")
    file.write("Pride and Prejudice, Jane Austen\n")

with open(file_name, "r") as file:
    books = file.readlines()
search_book = input("Kitob nomini kiriting: ")

found = False
for book in books:
    book_info = book.strip().split(", ")
    if book_info[0].lower() == search_book.lower():
        print(f"Book: {book_info[0]}, Author: {book_info[1]}")
        found = True
        break

if not found:
    print("Kitob topilmadi.")
"""
"""
#task5
import json
data = {
    "name": "Oyposh", "grades": [80, 90, 85],
    "name1": "Soliha", "grades1": [95, 88, 87]
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
oyposh_grades = data['grades']
oyposh_avg = sum(oyposh_grades) / len(oyposh_grades)
soliha_grades = data['grades1']
soliha_avg = sum(soliha_grades) / len(soliha_grades)

print(f"Name: {data['name']}, Average: {oyposh_avg}")
print(f"Name: {data['name1']}, Average: {soliha_avg}")
"""