import json

def submit():
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()
    
    if find_book(self.isbn.get()) == 0:
        if find_stock(self.stock.get()) == 0:
            # the book is borrowed
            pass

def find_book(isbn):
    file = open("books.txt", "r")
    content = file.readlines()
    file.close()
    
    print(content)
    for i in range(len(content)):
        content[i] = json.loads(content[i])
    print(content)
    print(len(content))
    
    for i in content:
        if i['isbn'] == isbn:
            print("yay!")
    return
    for line in lines:
        line = line.strip()
        line = line.split(",")
        line = dict(title = line[0], genre = line[1], isbn = line[2], authors = line[3], stock = line[4])
        print(line)
        #if line["isbn"] == str(isbn):
            # show info ("book is available")
           # return 0
    # error: book not found
    
    return 1

def find_stock(s):
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()
    
print(find_book(4546))