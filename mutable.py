shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

# How many lists are there in this program?
# What are the contents of another_list?
print(another_list)
print(id(another_list))
# There is only one list, both names point to the same list due to its mutability
# 8 references to the same list, still only one list though not 8
a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)
