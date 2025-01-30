### this code acts as an accumulator and a loop to manage a students result over time in his desired number of units
n = input("No of students: ")
for i in n:
     print("Student :" + str(i+1))
     y = input("No of units to be computed: ")
     total = 0
     for u in y:
             t = input("Unit :" + str(y+1))
             total += t
     print("Total for Student" + str(i+1))
     print("is: " + str(total))
