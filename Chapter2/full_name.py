first_name = "ada"
last_name  = "lovelace"
# Need to figure out wtf this does
full_name  = f"{first_name} {last_name}"
# To insert a variable's value into a STRING
# place the letter f immediately before the
# opening quotation mark. Put braces around
# the name or names of any variable you want
# to use inside the string

# Called f-strings: f for format
message = f"Hello, {full_name.title()}!"
print(message)

# F-string were first introduced in Python 3.6

# You can even do cool stuff like this
full_name = "{} {}".format(first_name, last_name)
print(full_name)


