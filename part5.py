# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830255 , 20200543

# Date: 25/04/2021

data = [
    [120, 0, 0],
    [100, 20, 0],
    [100, 0, 20],
    [80, 20, 20],
    [60, 40, 20],
    [40, 40, 40],
    [20, 40, 60],
    [20, 20, 80],
    [20, 0, 100],
    [0, 0, 120]
]


def histogram(progress_count, retriever_count, exclude_count, trailing_count):
    total = progress_count + retriever_count + exclude_count + trailing_count
    # displays a horizontal histogram
    progress_stars = progress_count * "*"
    retriever_stars = retriever_count * "*"
    exclude_stars = exclude_count * "*"
    trailing_stars = trailing_count * "*"
    print(f" progress : {progress_stars}\n trailing : {trailing_stars}"
           f" \n retriever: {retriever_stars}\n excluded : {exclude_stars}\n\n")
    print(f"{total} outcomes recorded.")


def main():
    progress_count = 0
    retriever_count = 0
    exclude_count = 0
    trailing_count = 0
    for a, b, c in data:  # tuple unpacking
        pass_marks = a
        deff_marks = b
        fail_marks = c
        if pass_marks == 100:  # checking the grade
            print("Progress - Module Trailer")
            trailing_count += 1
        elif pass_marks > 100:
            print("Progress")
            progress_count += 1
        elif fail_marks >= 80:
            print("Exclude")
            exclude_count += 1
        else:
            print("Do not progress - Module retriever")
            retriever_count += 1
    # calling histogram when the mark verification is done
    histogram(progress_count, retriever_count, exclude_count, trailing_count)



main()
