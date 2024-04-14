def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * 2 >= distance_to_pump else False

print(zero_fuel(50, 25, 2))