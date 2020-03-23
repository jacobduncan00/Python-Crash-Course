string1 = "This is a string."
string2 = 'This is also a string.'

print(string1)
print(string2)

# Adding whitespace
print("Python")
# Adds a tab "\t"
print("\tPython")
# Adds a line "\n"
print("Languages:\nPython\nC\nJavaScript")

# Stripping Whitespace
favorite_language = 'python '
print(favorite_language)
# Strips white space
favorite_language.rstrip()
print(favorite_language)

favorite_language = '    python     '

# Strip left side is lstrip()
favorite_language.rstrip()
# Strip right side is rstrip()
favorite_language.lstrip()
# Strip both sides is strip()
favorite_language.strip()
