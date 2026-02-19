print("hello")
Student_info={                                  #Dictionary in python 
    "name":"ullas",
    "age": 20,
    "branch":"cse"
}
print(Student_info["name"])                    # To print key and value
Student_info["age"]=21                         # To append the age value
Student_info["collage"]="pes"                  # Add the new value to dictionary
print(Student_info.get("place","not found"))
print(Student_info)
----------------------------------------------------------------------------------------------------------------------------------------------
marks = {
    "math":90,
    "abc":90,
    "physics":85,
    "cs":95
}
total=sum(marks.values())            # To find the sum of values in dictionary
avg=total/len(marks)                 # to calculate average value 
h=max(marks.values())                # to find max values
c=list(marks.values()).count(90)     # to count repeated
print(c)
print(h)
print(avg)
print(total)
print(marks)
---------------------------------------------------------------------------------------------------------------------------------------------
m={
    "pen":10,
    "book":30,
    "laptop":50000,
    "sun":10000
}
n={
   "a":"apple",
   "b":"ball",
   "c":"cat",
   "d":"dog"
}
print(n)
print(m)
ms=m|n                                # to merge both dictionary
su=sum(m.values())
for key in m:
   m[key]=m[key]*1.10                 # increase all key values by 10%
product=1
for value in m.values():
    if value>500:
     product*=value                  # to find product of two values
print(product)
print(su)
print(m)
m.pop("sun")                         # deleting the value from dictionary
print(m)            
print(ms)                

#-------------------------------------------------------------------------------------------------------------------------------------------
