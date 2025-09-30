book_list=[]

class book:#here we are defining the class 
    def __init__(self,title,author,status):#here we are initiating the class's objects
        self.title=title
        self.author=author
        self.status=status
    def show(self):#it is used to show the objects stored in the class
        print(f"Title:{self.title},Author:{self.author},Status:{self.status}")
    def mark_issued(self):#defining the function of mark_issued
        self.status="Issued"
        print(f"{self.title}, has been marked as issued")
    def delete(self):#here I have defined the delete function
        try:#try is used to handle error if user gave wrong input but it is not gonna ask the input again 
            book_list.remove(self)
        except ValueError:
            print("Book Not found!!")
        print(f"{self.title} has been deleted")

def convert_object(obj):#for json file handling we need to create this convert object function becasue in python it cannot be saved as oop but need to convert into json format to save the json file 
    return obj.__dict__#this line will convert the above obj into dictionary to save into json


try:#can also used in the while loop for asking the input again from user
    total=int(input("How many books: "))
except ValueError:
    print("please enter a valid Number: ")
    total=0#if not in the loop then it will store the value as 0 then move to the next line of code
print("Total number of books are:",int(total))

for i in range(total):
    title=input(f"What is the title of Book{i+1}: ")
    author=input(f"Who is the Author of {title}: ")
    status=input(f"What is the status: ")
    
    b=book(title,author,status)
    book_list.append(b)#the values are being stored as objects
    

for b in book_list:
    b.show()

search=input("Enter the name of book, you want to search: ").strip().lower()

found=False
for b in book_list:
    if search.lower()==b.title.lower():
        b.mark_issued()
        '''b.status="Issued"#simple way is this-----
        print(f"{search} has been marked as issued.")
        found=True'''
        b.show()
        break
else:
    print(f"{search} is not found")

delete_title=input("Enter the name of book you want to delete: ")
found=False

for b in book_list:
    if delete_title.lower()==b.title.lower():
        b.delete()
        '''found=True
        book_list.remove(b)
        print(f"{delete_title} has been deleted")'''
import json
try:
    f=open("books.json","w")
    json.dump(book_list,f,default=convert_object,indent=2)#convert obj is used here to save this books.json file as json whih is now converted from object to dictionary format.
    f.close()
except FileNotFoundError:
    print("File Not Found!!")
print("\n Current Book List:")
for b in book_list:
    b.show()
    break
import json
f=open("books.json","r")
data=json.load(f)
f.close()

print(data)

if not found:
    found=False
    print(f"{delete_title} is not in the book_list.")