#Ass no 3.1

ListOfFriends = ["Qasim","Kamran","Farhan","Ahmed"]
print(ListOfFriends[0])
print(ListOfFriends[1])
print(ListOfFriends[2])
print(ListOfFriends[3])


# Ass no 3.2 

print(f"Hellow {ListOfFriends[0]} how are you")
print(f"Hellow {ListOfFriends[1]} how are you")
print(f"Hellow {ListOfFriends[2]} how are you")
print(f"Hellow {ListOfFriends[3]} how are you")

# Ass no 3.3

transport_options = ["Bike","Honda Vezel","Train","Airplane"]
print(f"I am currently using {transport_options[0]} for regular travelling in city")
print(f"I would like to buy {transport_options[1]} in future inshallah")
print(f"I would like to travel to Islamabad using {transport_options[2]}")
print(f"I had never experience travelling by {transport_options[3]} ")

#Ass no 3.4

Guess_list = ["Kamran","Hammad","Hadi"]
print(f"{Guess_list[0]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[1]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[2]} you are invited to a dinner at my house this sunday")


#Ass no 3.5

#'Hammad' can't make it to dinner so therefore inviting 'Taha' for dinner

Guess_list[1] = "Taha"

print(f"{Guess_list[0]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[1]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[2]} you are invited to a dinner at my house this sunday")

#Ass no 3.6

Guess_list.insert(0,"Farhan")
Guess_list.insert(2,"Saad")
Guess_list.append("Ibad")

print(f"{Guess_list[0]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[1]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[2]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[3]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[4]} you are invited to a dinner at my house this sunday")
print(f"{Guess_list[5]} you are invited to a dinner at my house this sunday")

#Ass no 3.7
print(f"I am extremly sorry {Guess_list.pop()} you are not invited")
print(f"I am extremly sorry {Guess_list.pop()} you are not invited")
print(f"I am extremly sorry {Guess_list.pop()} you are not invited")
print(f"I am extremly sorry {Guess_list.pop()} you are not invited")

# Ass no 3.8

PlacesToVisit = ["Muree","Skardu","Hunza","Islamabad"]
print(PlacesToVisit)         #normal list
print(sorted(PlacesToVisit)) #sorted list but no change in orignal list
print(PlacesToVisit)         #normal list
PlacesToVisit.reverse()      #reversing the orignal list   
print(PlacesToVisit)         #reversed list   
PlacesToVisit.sort()         #soring orignal list
print(PlacesToVisit)         #sorted list

# Ass no 3.9
print(f"The total no Guest invited are : {len(Guess_list)}")

#Ass no 3.10

wishlist =[]                            # creating empty list
wishlist.append("Honda Vezel")          # append method to add item
wishlist += ["Iphone x","Hacker"]       # append alternative to add more than one value
wishlist.insert(1,"BSCS")               # using insert method to add at 1 position
wishlist2 = ["developer","Samsung","travelling"]
wishlist.extend(wishlist2)              #extending adding items of list 2 in list 1
wishlist3 = wishlist.copy()             #creating a copy of list1 and adds to list 3 list are reference type
removed_item = wishlist.pop()           #pop remove last element of list and return last elemetn
del wishlist3[2]                        # delete item at spicific index
wishlist.remove("Samsung")              #find and removes define item
print(f"removed item : {removed_item}")
print("The index position of hacker is : {}".format(wishlist.index("Hacker")))              #find the index position of item


print("Wish list 1")
print(wishlist)
print("Wish list 2")
print(wishlist2)
print("Wish list 3")
print(wishlist3)


