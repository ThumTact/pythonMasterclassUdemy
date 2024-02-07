letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

backwards2 = letters[25:0:-1] + letters[0]
print(backwards2)
backwards3 = letters[::-1]
print(backwards3)

# qpo
print(letters[16:13:-1])
# edcba
print(letters[4::-1])
# last 8 characters, in reverse order
print(letters[:17:-1])

