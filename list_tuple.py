# List r mutable 
#list in []
#Tuple r immutale just like string , we cannot change after creation.
#tuple in ()

lst=["Janvi",21,168,"Pune", True]# we can store any value int,float,str,boolean,none
lst2=[20,30,1,66,47,99,46.5]
lst.append(25000) #does not return anything, change happen in original list
lst2.sort() #sort betn same data types 
lst.reverse()# reverse the original list
lst2.reverse()
lst2.sort(reverse="True") #sort in descending order
lst2.pop(0) #remove ele at that index
lst[::-1] # we can do slicing 
lst[4] #indexing 

tup=()#empty tuple
tup2=(1,)#we give , if only one ele is there
tup3=(2,4,2,1,7,40)
print(tup3[::-1])#indexing
print(tup3.index(4))#returns index number
print(tup3.count(1))#returns count of number

#enter 3 movie names and store it in list
movie1="Avenger"
movie2="Spider man"
movie3="Captain america"
lst=[]
lst.append(movie1)
lst.append(movie2)
lst.append(movie3)
print(lst)

#check list contains palindrome
lst1=[1,2,3,2,1]
lst2=lst1.copy()
lst2.reverse()
if lst1==lst2:
    print("Palindrome")

#create a tuple to count grade A student
tup=("c","c","b","a","a")
print(tup.count("a"))
