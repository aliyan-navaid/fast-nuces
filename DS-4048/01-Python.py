def T1():
    weight=float(input("Weight (kg): "))
    height=float(input("Height (m): "))
    
    bmi = get_bmi(weight, height)
    status = get_status(bmi)
    
    print(status)


def get_bmi(weight: float, height: float) -> float:
    return round( weight/height**2, 2 )
    
def get_status(bmi: float) -> str:
    return "Under Weight" if bmi<18 else "Normal Weight" if bmi<24.9 else "Over Weight" if bmi<29.9 else "Obese"


def T2():
    nums: list[int] = [int(x) for x in input().split()]
    odd = 0
    for num in nums:
        odd += num%2

    print(f"Even: {len(nums)-odd}, Odd: {odd}")

def T3():
    nums: list[int] = list( map( int, input("Enter Numbers: ").split() ) )
    x: int = int( input("X: ") )

    cnt: int = 0
    for num in nums:
        cnt += x<num
    print(f"f({nums}, {x}): {cnt}")

def T4():
    nums: list[int] = list( map( int, input("Enter Numbers: ").split() ) )
    non_neg: list[int] = [ num for num in nums if num>=0 ]

    print(non_neg)

def T5():
    x: int = int(input("Number: "))
    print(f"x^2: {x**2}, x^3: {x**3}")

def T6():
    GROWTH_RATE: int = 1.15
    population = int(input("Popualation: "))
    print(f"Post 5 Years - Population: {int(population*(1.15**4))}")

def T7():
    kg = float(input("Weight(kg): "))
    lb = kg*2.2
    print(f"Weight(lb): {lb}")

def T8():
    info = ["Hall 10.5", "Kitchen 7.2", "Bedroom 13.8", "Bathroom 4.5"]
    for seq in info:
        extracted = seq.partition(" ")
        print(extracted[0], extracted[2], sep='\n')

def T9():
    first: set[int] = set([1,3,6,78,35,55])
    second: set[int] = set([12,24,35,24,88,120,155])

    print(f"Intersection: {first&second}")

def T10():
    score1 = [3.2,3.5,3.1,3.6,3.4,3.7]
    score2 = [2.8,3.0,2.9,3.1,3.0,3.2]
    score3 = [3.9,3.8,3.7,3.9,4.0,3.8]

    students = []

    students.append(["Yahya",score1])
    students.append(["Khush", score2])
    students.append(["Bush Kate",score3])

    print(students)

if __name__=="__main__":
    T10()
