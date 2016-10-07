# -- coding: utf-8 --
# 将汽车的数量100赋值给cars
cars = 100
# 设置汽车可容纳空间
space_in_a_car = 4.0
# 设置驾驶员数量
drivers = 30
# 设置乘客数量
passengers = 90
# 空闲车辆数量
cars_not_driven = cars - drivers
# 运营汽车数量
cars_driven = drivers
# 最大载客量
carpoll_capacity = cars_driven * space_in_a_car
# 每辆车的平均载客数量
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpoll_capacity, "people today."
print "We have", passengers, "to carpoll today."
print "We need to put about", average_passengers_per_car, "in each car."
