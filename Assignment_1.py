#Some of the List's in-built functions
List1= [ 1, 2, 3, 4, 5, True, "ABCDE", "FGHIJ", "KLMNO", "PQRST"]
print(List1)
List1.append("UVWXYZ")#Adds an element at the end of the List
print("After performing append(""UVWXYZ"") function ")
print(List1)
print("List1.count(2)=")
print(List1.count(2))#Returns the number of times a specific value is present in List
print("List1.index(5)=")
print(List1.index(5))#Returns the index of the first element with the specified value
List1.insert(11, "New")#Inserts an element at the specified address
print("After performing insert(11) function ")
print(List1)
List1.pop(11)#Removes the element present at the given index
print("After performing pop(11) function ")
print(List1)
print("-------------------------")
#Some of the Dictionarie's in-built functions
Dict1= {"Name": "KSR", "Age": 20, "City": "Vijayawada", "Occupation": "Student",
        "Course": "Python Essentials", "Provider": "Let's Upgrade"}
print(Dict1)
Dict1.update({"College": "DJRCET"})#Adds the given key:value pair to the the Dictionary if previously not present
print("After performing update(""College"":""DJRCET"") function ")
print(Dict1)
print("Dict1.get(""Name"")")
print(Dict1.get("Name"))#Returns the value of the specified key
print("Dict1.keys()")
print(Dict1.keys())#Returns a list conatining Dictionary keys
print("Dict1.values()")
print(Dict1.values())#Returns a list of all the values containing Dictionary values
Dict1.popitem()#Removes the last inserted key:value pair
print("Dict1.popitem()")
print(Dict1)
print("-------------------------")
