shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# does the same as continue
# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        # continue
        break

    print("Buy " + item)
