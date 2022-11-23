from typing import List


if __name__ == '__main__':
    prime_numbers_list_compl: List[int] = [num for num in range(2, 1001) if len([divider for divider in range(2, num) if num % divider == 0]) == 0]

    print(prime_numbers_list_compl)


    prime_numbers_lambda: List[int] = list(filter(lambda num: num == 2 or len([dev for dev in range(2, num) if num % dev == 0]) == 0, range(2, 1001)))

    print(prime_numbers_lambda)


    prime_numbers_list: List[int] = [2]
    for num in range(2, 1001):
        prime: bool = True
        for prime_number in prime_numbers_list:
            if num % prime_number == 0:
                prime = False
        if prime:
            prime_numbers_list.append(num)

    print(prime_numbers_list)
