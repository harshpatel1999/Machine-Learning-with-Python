#LIST lenthgth
list1 = ['BMW','RR','Range Rover','jaguar','GMC']
print(len(list1))

#max list

list1 = ['BMW','RR','Range Rover','jaguar','GMC']
list2 = [10,2,5,8,9,7,3,50]
print(max(list1))
print(max(list2))

#min()

list1 = ['BMW','RR','Range Rover','jaguar','GMC']
list2 = [10,2,5,6,78,98,5]
print(min(list2))
print(min(list1))

#list(seq)

tuple = ('BMW','RR','Range Rover','jaguar','GMC')
list1 = list(tuple)
print(list1)

tuple = (123,'c','C++','kotlin','go','c#')
list1 = list(tuple)
print(list1)

str = "hello world"
list2 = list(str)
print(list2)

#append()

list1 = ['C++', 'Java', 'Python']
list1.append('C#')
print ("updated list : ", list1)

list=['BMW','RR','Range Rover','jaguar','GMC']
list.append('Ferrari')
print(list)


#count()

list=['BMW','RR','Range Rover','RR','jaguar','GMC']
print(list.count('RR'))

#extend()

list = [15,20,25,30]
list2 = [35,40,45,50]

list.extend(list2)
print(list)

#index(obj)

list1 = ['RR', 'BMW', 'Jaguar']
print ('Index of car list', list1.index('RR'))


#INSERT()

list=['BMW','RR','Range Rover','jaguar']
list.insert(2,'GMC')
print(list)

#pop()
list=['BMW','RR','Range Rover','jaguar','GMC']
list.pop(1)
print(list)


#remove()
list= ['BMW','RR','Range Rover','jaguar','GMC']
list.remove('jaguar')
print(list)

#reverse()

list = ['BMW','RR','Range Rover','jaguar','GMC']
list.reverse()
print(list)

list = [10,20,30,54,6,8,48,7,8,95,25]
list.sort()
print(list)

#















