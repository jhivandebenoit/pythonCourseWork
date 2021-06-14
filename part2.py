# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830255 , 20200543

# Date: 25/04/2021

# type_mark is so I can use one function to take all inputs
def input_taker(type_mark):
    while True:
        try:     # F string literal taking type from mark_sum
            mark = int(input(f"Please enter your credit at {type_mark}: "))
        except ValueError:
            print("Enter an Integer")
        else:
            if mark in [0, 20, 40, 60, 80, 100, 120]:
                return mark
            else:
                print("Integer out of range")
                continue


# Calls input function and checks mark sum
def mark_sum():
    while True:
        pass_mark = input_taker("pass")
        deff_mark = input_taker("deff")
        fail_mark = input_taker("fail")
        if pass_mark + deff_mark + fail_mark != 120:
            print("Total incorrect")
        else:
            break
    return pass_mark, fail_mark


# calls mark_sum and evaluates the students grade
def main():

    pass_mark, fail_mark = mark_sum()
    if pass_mark == 100:
        print("Progress - Module Trailer")
    elif pass_mark > 100:
        print("Progress")
    elif fail_mark >= 80:
        print("Exclude")
    else:
        print("Do not progress - Module retriever")


main()
