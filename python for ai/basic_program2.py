# Basic questions 
#Q1
movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

mov = input("3rd movie")
movies.append(mov)
print (movies)

#Q2 Important
list = [1,2,3,2,1]
list.append(input("enter = "))
copy_list = list.copy()
copy_list.reverse()

if (list == copy_list):
    print("palindrome")

else :
    print("not palindrome")

# or (without using copy function)
if (list == list[::-1]):   #[start:end:-1]
    print("palindrome")

else :
    print("not palindrome")

#Q3
tup = ("c","d","a","a","b","b","a")
print(tup.count("a"))

#Q4

grades = list(tup)
grades.sort()
print(grades)



