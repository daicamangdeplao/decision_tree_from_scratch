# write your code here
node = [int(x) for x in input().split(" ")]

class_0 = 0
class_1 = 1

def calculate_probability(class_i, arr):
    counter = arr.count(class_i)
    return counter / len(arr)

def calculate_gini(arr):
    p_0 = calculate_probability(class_0, arr)
    p_1 = calculate_probability(class_1, arr)
    return 1 - p_0 ** 2 - p_1 ** 2

split_1 = [int(x) for x in input().split(" ")]
split_2 = [int(x) for x in input().split(" ")]

def calculate_weighted_gini():
    gini_index_1 = calculate_gini(split_1)
    gini_index_2 = calculate_gini(split_2)
    return round(len(split_1) / len(node) * gini_index_1 + len(split_2) / len(node) * gini_index_2, 5)

print(f"{round(calculate_gini(node), 2)} {round(calculate_weighted_gini(), 2)}")
