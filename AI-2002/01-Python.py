def T1():
    n = int(input("Enter Index for Fibonacci (1,..): "))
    print(f"Fibonacci: {fibonacci(n-1)}")

def fibonacci(n):
	return 0 if n<=0 else 1 if n==1 else fibonacci(n-1)+fibonacci(n-2)

def T2():
    var = [ 1, 2, [3, 4], [5, [100, 200, ['hello']], 2, 3, 1], 1, 7 ]
    print(f"Var[3]: {var[3]}]", f"var[3][1]: {var[3][1]}", f"var[3][1][2]: {var[3][1][2]}", f"var[3][1][2][0]: {var[3][1][2][0]}", sep = '\n')

def T3():
    var = { 'k1': [1, 2, 3, { 'tricky': ['oh', 'man', 'inception', { 'target': [1,2,3,'hello'] } ] } ] }
    print(var['k1'][3]['tricky'][3]['target'][3])

def T4():
    speed = int(input("Speed: "))
    anniversary = input("is anniversary? (y/n): ").lower()=='y'
    print( fine(speed, anniversary) )

def fine(speed: int, anniversary: bool) -> str:
    speed -= anniversary * 10

    # inline statements
    if ( speed<=70 ): return f"No fine"
    elif (speed<=80): return f"Less fine"
    else: return "Car seized"

def T5():
    nums = []
    for i in range(5):
        nums.append(int(input()))

    new = set()
    for num in nums:
        if num not in new:
            new.add(num)
        else:
            print(f"{num} is duplicate")

    print(f"Nums without duplicates: {new}")

def T6():
    sentence = input("Enter sentence: ")
    
    letters, digits = 0, 0
    for char in sentence:
        if '0' <= char <= '9': digits+=1
        else: letters += 1
    print(f"Letters: {letters}, Digits: {digits}")

def T7():
    food_items= {"Lasagna":350, "Besan ke Fries":500, "White Sauce Pasta":900}
    order, discount, hostelite = {}, 0, False

    hostelite = input("Are you a hostelite? (y/n)").lower()=="y"
    
    for item, price in food_items.items():
        print(f"{item}: {price}")
    print("Enter done to quit ordering...\n")

    while True:
        item = input("Item: ")
        if (item=="done"): break
        order[item] = order.get(item, 0) + 1
    
    for item, count in order.items():
        print(f"{count}x {item}")

    total=0
    for item, count in order.items():
       total += food_items[item] * count
    if total>=1000:
        print(f"Discount: {total*0.1}")
        total-=total*0.1
    if hostelite:
        print(f"Hostelite Discount: 100")
        total-=100
    print(f"Total: {total}")

if __name__=="__main__":
	T7()
