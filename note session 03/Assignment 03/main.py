
#            ____  _____  ______ _      _____            _    _ __  __          _   _            _    _ __  __ ______ _____             ____  _____  ______ _      _____          _____ __  __
#      /\   |  _ \|  __ \|  ____| |    |  __ \     /\   | |  | |  \/  |   /\   | \ | |     /\   | |  | |  \/  |  ____|  __ \      /\   |  _ \|  __ \|  ____| |    |  __ \   /\   |_   _|  \/  |
#     /  \  | |_) | |  | | |__  | |    | |__) |   /  \  | |__| | \  / |  /  \  |  \| |    /  \  | |__| | \  / | |__  | |  | |    /  \  | |_) | |  | | |__  | |    | |  | | /  \    | | | \  / |
#    / /\ \ |  _ <| |  | |  __| | |    |  _  /   / /\ \ |  __  | |\/| | / /\ \ | . ` |   / /\ \ |  __  | |\/| |  __| | |  | |   / /\ \ |  _ <| |  | |  __| | |    | |  | |/ /\ \   | | | |\/| |
#   / ____ \| |_) | |__| | |____| |____| | \ \  / ____ \| |  | | |  | |/ ____ \| |\  |  / ____ \| |  | | |  | | |____| |__| |  / ____ \| |_) | |__| | |____| |____| |__| / ____ \ _| |_| |  | |
#  /_/    \_\____/|_____/|______|______|_|  \_\/_/    \_\_|  |_|_|  |_/_/    \_\_| \_| /_/    \_\_|  |_|_|  |_|______|_____/  /_/    \_\____/|_____/|______|______|_____/_/    \_\_____|_|  |_|



#-------------------------------#
##List
List = ['Abdelrahman', 'ahmed', 1997, 2022,[20,55,'Abdo']]
print(List)

#append
List.append('porstSaid')
print(List)
#insert
List.insert(2,'Abdeldaim')
print(List)
#extend
List2 = ['Red','Code']
List.extend(List2)
print(List)
#count
print(List.count('Abdeldaim'))
#length
print(len(List))
#remove
List.remove('Abdelrahman')
print(List)

#-------------------------------#
##Dictionary
Dictionary = {'name': 'Abdelrahman', 'Last Name': 'Ahmed Abdeldaim', }
print(Dictionary)
#update
Dictionary2= {'age': '25','Phone':'01067668841'}
Dictionary.update(Dictionary2)
print(Dictionary)
#get
print(Dictionary.get('name'))
#keys
print(Dictionary.keys())
#values
print(Dictionary.values())
#pop
Dictionary.pop('Phone')
print(Dictionary)

#-------------------------------#
##Tuple
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
Tuple2 = ('python', 'geek', 'python',
          'for', 'java', 'python')
print('Tuple1:', Tuple1 ,'\n','Tuple2: ', Tuple2)
#Count
print(Tuple2.count(2))

#-------------------------------#
##Set
Set = {'Abdelrahman', 'ahmed'}
print(Set)
#add
Set.add("Abdeldaim")

print(Set)
#remove
Set.remove("Abdeldaim")

print(Set)
#update
Set2 = {25,1997}
Set.update(Set2)

print(Set)
#pop
#  -----------------------------------------------------------
# Remove a random item from the set:
#  -----------------------------------------------------------

Set.pop()

print(Set)
#clear
Set.clear()

print(Set)
