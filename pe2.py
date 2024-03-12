def find_balance_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == total_sum - arr[i] - left_sum:
            return "YES"
        left_sum += arr[i]
    return "NO"

def main():
    arr = input("Enter the array elements separated by space: ").split()
    arr = [int(x) for x in arr]
    result = find_balance_index(arr)
    print(result)

if __name__ == "__main__":
    main()

