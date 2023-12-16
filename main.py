import time

while True:

    print("\033[1m--- Welcome to the Tip Calculator! ---\033[0m")
    bill = float(input("What was the total bill? $"))
    people = int(input("How many people to split the bill? "))
    tip = int(input("What percentage tip would you like to give? (10, 12 or 15) "))
    print('--- Calculating... ---')
    time.sleep(1)

    if tip == 10:
        bill = bill * 1.1
        break
    elif tip == 12:
        bill = bill * 1.12
        break
    elif tip == 15:
        bill = bill * 1.15
        break
    else:
        print('Value of percentage invalid. Please start again.')
        continue

value_per_person = bill / people

print(f"Each person should pay: $ {value_per_person:.2f}")