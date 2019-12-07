import math

def generate_grade(random_time):

    if(random_time > 3 and random_time < 17):
        average_grade = random_time/2
    elif (random_time <= 3):
        average_grade = 2
    else:
        average_grade = 8
    minimum_grade = average_grade - 2
    maximum_grade = average_grade + 2
    return random.randint(int(minimum_grade), int(maximum_grade))
    

if __name__ == "__main__":

    provjera = 1
    while(provjera != 0):
        n = input("\nMatrix: ")
        if(int(n) != 1):
            provjera = math.sqrt(int(n)) - int(math.sqrt(int(n)))
            if(provjera != 0):
                print("Square root of matrix size must be whole number!")
        else:
            print("Please input number greater than 1.")                
    matrixName = (n + "x" + n + "_matrix.csv")
    matrixFile = open(matrixName, "w")
    for i in range (0, int(n)):
        for i in range (0, int(n)):
            if(i < (int(n)-1)):
                matrixFile.write("0;")
            else:
                matrixFile.write("0")
                
        matrixFile.write("\n")

    matrixFile.close()
    print("Null matrix successfully created.")

    
