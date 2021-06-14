# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830255 , 20200543

# Date: 25/04/2021

# type_mark is so I can use one function to take all inputs
def input_taker(type_mark):      # type_mark is so I can use one function to take all inputs
    while True:
        try:
            mark = int(input(f"Please enter your credit at {type_mark}: "))
        except ValueError:
            print("Enter an Integer")
        else:
            if mark in [0, 20, 40, 60, 80, 100, 120]:
                return mark
            else:
                print("Integer out of range")
                continue


# Produces a histogram
def histogram(progress_count, retriever_count, exclude_count, trailing_count):
    # displays a horizontal histogram
    total = progress_count + retriever_count + exclude_count + trailing_count
    progress_stars = progress_count * "*"
    retriever_stars = retriever_count * "*"
    exclude_stars = exclude_count * "*"
    trailing_stars = trailing_count * "*"
    print(f" progress : {progress_stars}\n trailing : {trailing_stars}"
           f" \n retriever: {retriever_stars}\n excluded : {exclude_stars}\n\n")
    print(f"{total} outcomes recorded.")



# checks the sum of the numbers and the returns the result as a number depending on the marks
def teacher_checker(pass_mark, deff_mark, fail_mark):
    sum_mark = pass_mark + deff_mark + fail_mark
    progress_add = 0
    trailing_add = 0
    exclude_add = 0
    retriever_add = 0
    if sum_mark != 120:
        print("total incorrect")
        pass
    elif pass_mark == 100:
        print("Progress - Module Trailer")
        trailing_add = 1

    elif pass_mark > 100:
        print("Progress")
        progress_add = 1

    elif fail_mark >= 80:
        print("Exclude")
        exclude_add = 1
    else:
        print("Do not progress - Module retriever")
        retriever_add = 1
    return progress_add, trailing_add, exclude_add, retriever_add



def main():


    more_input = ""
    progress_count = 0
    retriever_count = 0
    exclude_count = 0
    trailing_count = 0
    while True:
        pass_marks = input_taker("pass")
        deff_marks = input_taker("deffer")
        fail_marks = input_taker("fail")
        # Increment each stat based on the results
        progress_inc, trailing_inc, exclude_inc, retriever_inc = teacher_checker(pass_marks, deff_marks, fail_marks)
        if progress_inc == 1:
            progress_count += 1
        elif trailing_inc == 1:
            trailing_count += 1
        elif exclude_inc == 1:
            exclude_count += 1
        elif retriever_inc == 1:
            retriever_count += 1
        while more_input != "q":
            more_input = input("Enter y to continue and q to quit")
            if more_input == "y":
                break
        if more_input == "q":
            break
    histogram( progress_count, retriever_count, exclude_count, trailing_count)




main()
