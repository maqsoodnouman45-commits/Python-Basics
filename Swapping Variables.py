#How to swap Variables in Python.

glass_1 = "Red Juice"
glass_2 = "Blue Water"
print("Before Swapping")
print("glass_1:", glass_1)
print("glass_2:", glass_2)

swap_glass = glass_1

glass_1 = glass_2
glass_2 = swap_glass

print("After Swapping")
print("glass_1:", glass_1)
print("glass_2:", glass_2)