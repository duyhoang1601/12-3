def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_prime_numbers(sequence):
    primes = []
    for num in sequence:
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    while True:
        try:
            sequence = input("Enter a sequence of positive integers separated by spaces: ").split()
            sequence = [int(num) for num in sequence]
            if not all(num > 0 for num in sequence):
                print("Please enter only positive integers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter positive integers separated by spaces.")

    prime_numbers = get_prime_numbers(sequence)
    if prime_numbers:
        print("Prime numbers in the sequence:", prime_numbers)
        print("Largest prime number in the sequence:", max(prime_numbers))
    else:
        print("No prime numbers found in the sequence.")

if __name__ == "__main__":
    main()
