import math
import statistics
def main():
    print("\nET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display_main_menu()
    temp_list = get_user_input()

    calc_average(temp_list)
    find_min_max(temp_list)
    sort_temperature(temp_list)
    calc_median_temperature(temp_list)

def display_main_menu():
    print("\ndisplay_main_menu")
    print("\nEnter some numbers separated by commas (eg 5,67,32)")

def get_user_input():
    value = input()
    a = value.split(",")
    temp_list = []
    for x in a:
        temp_list.append(float(x))
    return temp_list

def calc_average(temp_list):
    avg = sum(temp_list)/len(temp_list)
    print(f"The average value is  {avg}")
    return avg

def find_min_max(temp_list):
    minimum = min(temp_list)
    maximum = max(temp_list)
    print(f"The min value is {minimum}")
    print(f"The max value is {maximum}")
    min_max = []
    min_max.append(minimum)
    min_max.append(maximum)
    return min_max

def sort_temperature(temp_list):
    temp_list.sort()
    print(f"The sorted array list in ascending order is {temp_list}")
    return temp_list

def calc_median_temperature(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    if n % 2 != 0:
        # If the length of the list is odd
        median = sorted_arr[n // 2]
    else:
        # If the length of the list is even
        median = (sorted_arr[(n // 2) - 1] + sorted_arr[n // 2]) / 2

    print("The median is ", median)
    return median



if __name__ == "__main__":
    main()