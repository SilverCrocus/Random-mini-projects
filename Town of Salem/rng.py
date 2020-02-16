import random
def rng():
    num = input("How many players?: ")
    random_num = random.randint(1 , int(num))
    print(random_num)
    while True:
        new = input("Press enter for a new number or type exit to quit: ")
        if new == "quit":
            break
        random_num = random.randint(1 , int(num))
        print(random_num)

rng()
