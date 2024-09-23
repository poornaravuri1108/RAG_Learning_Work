import magic

mime = magic.Magic(mime=True)
print(mime.from_file('data/books/alice_in_wonderland.md'))