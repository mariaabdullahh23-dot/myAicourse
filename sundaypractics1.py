book=[7687 , 1050 ," Jane Austen" , 2025 ,999, True ]
print(book)
print(type(book))
print(type(book[2]))

for i in book :
    print(i)

book.append ("Leo Tolstoy")
print(book)
book.insert(2,"review")
print(book)
book.remove(1050)
print(book)
popvalue = book. pop(2)
print(popvalue)

book=(7687 , 1050 ," Jane Austen" , 2025 ,999, True )
print(type(book))
print(type(book[4]))
print(type(book[-3]))

for i in book:
    print(i)