#Find out common letters between two strings

def common_letter():
    str1= input("Enter the first string:")
    str2= input("Enter the second string:")
    s1= set(str1)
    s2= set(str2)
    lst= s1&s2
    print(lst)

common_letter()

#------------------------------------------------------------------
#Directly enter the number
def common_number():
    str1=(2,3,4,5,3)
    str2=(3,6,4,3)
    s1=set(str1)
    s2=set(str2)
    lst=s1&s2
    print(lst)
    
common_number()
