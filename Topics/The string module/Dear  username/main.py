import string

# put your code here
username = input()
str_template = string.Template("Dear $username! It was really nice to meet you. Hopefully, you have"
                               " a nice day! See you soon, $username!")
my_str = str_template.substitute(username=username)
print(my_str)

