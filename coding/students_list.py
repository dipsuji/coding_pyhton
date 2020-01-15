from os.path import sep


class students:
    """
    Create student class Id, roll, name
    """
    def __init__(self, id, name, roll):
        self.id = id
        self.name = name
        self.roll = roll


print "Table 1:"

# Create list of students objects
list1 = []

# appending instances to list
list1.append(students(11, 'Akash', 15))
list1.append(students(2, 'Deependra', 40))
list1.append(students(3, 'Reaper', 44))
list1.append(students(5, 'Dinakar', 2))

for obj1 in list1:
    print(obj1.id, obj1.name, obj1.roll, sep == ' ')

print "Table 2:"

# Create another list of objects using same student class
list2 = []

# appending instances to list
list2.append(students(1, 'Dinakar', 3))
list2.append(students(11, 'Sujata', 41))
list2.append(students(5, 'Arnav', 44))
list2.append(students(7, 'Anuj', 47))

for obj2 in list2:
    print(obj2.id, obj2.name, obj2.roll, sep == ' ')

#  according to same id find the student from second list
for obj1 in list1:
    for obj2 in list2:
        if obj1.id == obj2.id:
            print obj1.name + " " + obj2.name
