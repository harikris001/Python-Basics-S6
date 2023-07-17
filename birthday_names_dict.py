birthday_dict = {"abc":'jan 01',"def":'feb 02',"ghi":'mar 03',"jkl":'apr 04'}

search = input("Enter name of person: ")

if birthday_dict.get(search,None) != None:
    print(f"Birthday is {birthday_dict[search]}")
else:
    print("No data found")