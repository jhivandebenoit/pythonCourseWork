# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830255 , 20200543

# Date: 25/04/2021

def main():

    # Taking mark inputs
    pass_marks = int(input("Please enter your credits at pass: "))
    deff_marks = int(input("Please enter your credits at defer: "))
    fail_marks = int(input("Please enter your credits at fail: "))

    # Checking and printing the relevant result
    if pass_marks == 100:
        print("Progress - Module Trailer")
    elif pass_marks > 100:
        print("Progress")
    elif fail_marks >= 80:
        print("Exclude")
    else:
        print("Do not progress - Module retriever")




main()