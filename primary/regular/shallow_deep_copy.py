import copy

original_list = [1, 2, [3, 4], 6]

shallow_copied_list = copy.copy(original_list)
deep_copied_list =copy.deepcopy(original_list)

original_list[2].append(5)

print(original_list)
print(shallow_copied_list)
print(deep_copied_list)