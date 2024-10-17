#Conversion of two list into Dictionary

def list_to_dict():
    keys=["Name","Age","City"]
    values=["John",25,"New York"]
    result = dict(zip(keys,values))  #grab into zip and convert by using dict
    print(result)


list_to_dict()