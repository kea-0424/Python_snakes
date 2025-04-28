
# Question 2.1

set1 = {42, 'python',(1,2),3.14,True}
set2 = {'apple', 100, (2,3,4),4.5,None}


# Question 2.2
set3 = set1.intersection(set2)
print("\nIntersection of set1 and set2 is: ", set3)


# Question 2.3
set4 = set1.union(set2)
print("\nUnion of set1 and set2 is: ", set4)

# Question 2.4
set5 = set1.difference(set2)
print("\nDifference of set1 and set2 is: ", set5)

# Question 2.5
set6 = set1.symmetric_difference(set2)
print("\nSymmetric difference of set1 and set2 is: ", set6)

# Question 2.6
length_set3 = len(set3)
length_set4 = len(set4)
length_set5 = len(set5)
length_set6 = len(set6)
print("\nLength of intersection set3 is: ", length_set3)
print("\nLength of union set4 is: ", length_set4)
print("\nLength of difference set5 is: ", length_set5)
print("\nLength of symmetric difference set6 is: ", length_set6)
