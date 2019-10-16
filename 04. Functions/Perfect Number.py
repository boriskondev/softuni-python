def perfect_or_not(number):
    total = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    if total == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())

perfect_or_not(num)