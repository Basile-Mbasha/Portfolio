
# Author: Basile M.
# Date: March 25th,2022 12:31PM
# Description: Program will:
#   + calculate the average mark of a student 
#   + give the student a grade note based on his/her average
        

# find the average mark
def average_mark(marks):
    
    sum_of_subjects = len(marks)
    total_marks = sum(marks)
    average_mark = total_marks / sum_of_subjects
    
    return average_mark

# compute the grade
def compute_grade(average_mark):
    
    if average_mark >= 80:
        grade = 'A'
    elif average_mark >= 70:
        grade = 'B'
    elif average_mark >= 60:
        grade = 'C'
    else:
        grade = 'D'
        
    return grade


# run the program
# output result on the console
def main():
    
    # sample testing marks
    marks = [54,75,45,69,99.5]
    
    average = average_mark(marks)
    grade = compute_grade(average)
    
    print("\nYour average is:", average)
    print("Your grade is:", grade)
        
if __name__ == "__main__":
    main()


# program could be modified 
# to check if student passed or not
# endless implementation could be done here
# feel free to send in your suggestions 
# for more efficiency ,..



#__happy coding,...





