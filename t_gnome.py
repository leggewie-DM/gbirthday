import evolution

b = evolution.ebook.list_addressbooks()

print b

b = evolution.ebook.open_addressbook(b[0][1])

for c in b.get_all_contacts():
    if c:
        print c.props.birth_date
        if c.props.birth_date:
            print c.props.birth_date.year
