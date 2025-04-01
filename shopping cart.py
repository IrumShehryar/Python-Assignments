shopping_list=[]
while True:
    user_input=int(input("Press 1 to add, 2 to remove the item, 3 to stop;"))
    int_user_input= int(user_input)
    if int_user_input==1:
        item=input("Give me the item: ")
        shopping_list.append(item)
        print(f"{shopping_list}")
    elif int_user_input==2:
        if len(shopping_list) >= 1:
            item = input("Give me the item to remove: ")
            if item in shopping_list:
                 shopping_list.remove(item)
                 print(f" {item} removed")
            else:
                print("Item is not in the list")
        else:
             print("The cart is empty")

    elif user_input == 3 :
        print("Thank you!")
        print(shopping_list)
        for i in shopping_list:
            print(i)
        break

    else:
        print("Invalid Input!")