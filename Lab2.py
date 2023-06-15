print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input().split(",")
    for i in range(0,len(x)):
        x[i] = float(x[i])
    return x
def calc_average(input_list):
    total = 0
    for i in input_list:
        total += i
    average = total / len(input_list)
    print("Average = " + str(average))

def find_min_max(input_list):
    min_temp = input_list[0]
    max_temp = input_list[0]

    for i in input_list:
        if (i < min_temp):
            min_temp = i

    for i in input_list:
        if (i > max_temp):
            max_temp = i

    print("Minimum = " + str(min_temp))
    print("Maximum = " + str(max_temp))

def sort_temperature(input_list):
    return sorted(input_list)


def calc_median_temperature(sorted_list):
    median = 0
    print(sorted_list)

    if len(sorted_list) % 2 == 1:
        median = sorted_list[int((len(sorted_list) + 1) / 2)-1]
    elif len(sorted_list) % 2 == 0:
        median = (sorted_list[int(len(sorted_list) / 2)-1] + sorted_list[int((len(sorted_list) / 2) + 1)-1]) / 2

    print("Median = " + str(median))


display_main_menu()
list_of_numbers = get_user_input()
calc_average(list_of_numbers)
find_min_max(list_of_numbers)
sorted = sort_temperature(list_of_numbers)
calc_median_temperature(sorted)