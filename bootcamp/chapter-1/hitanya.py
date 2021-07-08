# string format

# using .format()

book = 'Ikigai'
pages = 208
author = 'Hector Gracia'

print('The name of the book is {b}, it has {p} pages, author of the book is {a}'.format(b='Ikigai' ,p=208 ,a='Hector Gracia'))
print('The name of the book is {b}, it has {p} pages, author of the book is {a}'.format(b='book' ,p=pages ,a='author'))
print('The name of the book is {}, it has {} pages, author of the book is {}'.format(book ,pages ,author))

# using f-string

print(f'The name of the book is {book}, it has {pages} pages, author of the book is {author}')

# to get string representation
print(f'The name of the book is {book!r}, it has {pages!r} pages, author of the book is {author!r}')




