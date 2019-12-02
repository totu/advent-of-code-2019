#!/usr/bin/env python3
import task1
import task2


task_1_fuel_consumed = 0
task_2_fuel_consumed = 0

with open("input", "r") as input_file:
    for entry in input_file:
        task_1_fuel_consumption = task1.calculate_fuel_consumption(int(entry))
        task_1_fuel_consumed += task_1_fuel_consumption
        task_2_fuel_consumption = task2.calculate_fuel_consumption(int(entry))
        task_2_fuel_consumed += task_2_fuel_consumption

print("task1:")
print(task_1_fuel_consumed)
print("task2:")
print(task_2_fuel_consumed)
