def get_output_array(nums_array: list) -> list:
    for i in range(len(nums_array) - 1):
        if nums_array[i] == 0:
            nums_array.append(nums_array[i])
            nums_array.remove(nums_array[i])
    return nums_array


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The resultant array is : ", get_output_array(num_array))
except ValueError:
    print("Invalid input. Enter only integers")
