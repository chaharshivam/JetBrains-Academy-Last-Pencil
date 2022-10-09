import string
template = string.Template("Hi, $name! You look $adjective today! You're doing great!")
name = input()
adjective = input()
compliment = template.substitute(name=name, adjective=adjective)
print(compliment)
