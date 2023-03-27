# TODO: Edit the function to return the correct grade for different scores
def get_grade(marks):
    if marks>89:
        grade= "A"
    elif marks>79:
        grade= "B"
    elif marks> 69:
        grade= "C"
    elif marks>59:
        grade= "D"
    elif marks<=59:
        grade="F"
    else:
        print("Out of range") 
    return grade
marks=int(input("Marks"))
print(get_grade(marks))
    
