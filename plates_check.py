from car_numbers import plates_list

# 1st
unique_numbers = []
duplicated_numbers = []
for number in plates_list:
    if number in unique_numbers:
        unique_numbers.remove(number)
        duplicated_numbers.append(number)
    elif number not in unique_numbers and number not in duplicated_numbers:
        unique_numbers.append(number)

unique_numbers_count = len(unique_numbers)
print(f"Count of all numbers: {len(plates_list)}")
print(f"Count of unique numbers: {unique_numbers_count}")

new_car_num = input("Enter car number and press Enter \n")
# Check if number exists in plates list
if new_car_num.upper() in plates_list:
    print(f"This number - '{new_car_num}' exists in the car numbers list")
else:
    print(f"This number - '{new_car_num}' doesn't exist in the car numbers list")

car_nums_sum = 0
for char in new_car_num:
    if char.isdigit():
        car_nums_sum += int(char)
print(f"The car number sum is: {car_nums_sum=}")
