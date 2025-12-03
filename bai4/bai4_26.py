balance = 0

while True:
    line = input()
    if line == "":
        break

    action, money = line.split()
    money = int(money)

    if action == "D":
        balance += money
    elif action == "W":
        balance -= money

print(balance)
