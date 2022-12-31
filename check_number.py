from car_numbers import plates_list
import collections

car_numbers_counts = {}
for number in plates_list:
    if number not in car_numbers_counts.keys():
        car_numbers_counts[number] = 1
    else:
        car_numbers_counts[number] = car_numbers_counts[number] + 1
duplicated_numbers = {number: car_numbers_counts[number]
                      for number in car_numbers_counts.keys()
                      if car_numbers_counts[number] > 1}
print(duplicated_numbers)

# unique
unique_numbers = [item for item, count in collections.Counter(plates_list).items() if count == 1]
print(len(unique_numbers))


# Check unique car numbers
car_nums_counts = {}
for number in plates_list:
    if number not in car_nums_counts.keys():
        car_nums_counts[number] = 1
    else:
        car_nums_counts[number] = car_nums_counts[number] + 1
uniq_nums = {number: car_nums_counts[number]
             for number in car_nums_counts.keys()
             if car_nums_counts[number] == 1}
print(f"Count of unique numbers: {len(uniq_nums)}")
