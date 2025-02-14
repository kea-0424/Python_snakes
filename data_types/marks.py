#if statement
marks = int(input("What are your marks? "))

if marks < 50:
    print("Failed") 

elif marks < 1 and marks > 100:
    print ("Eror 404")

elif marks >= 50 and marks < 61:
    print("Average pass")

elif marks >= 61 and marks < 101:
    print("Perfect pass")

else:
    print("Invalid marks")