# In case it is not obvious, a list comprehension produces a list, but
# it does not have to be given a list to iterate over
#
# You can use a list comprehension with any iterable type, so we will 
# write a comprehension to convert dimensions from inches to centimeters.
#
# Our dimensions will be represented by a tuple, for the length, width and height.
#
# There are 2.54 centimeters to 1 inch.

inch_measurement = (3, 8, 20)

cm_measurement = [inch * 2.54 for inch in inch_measurement]
print(cm_measurement)

# Once you have got the correct values, change the code to produce a tuple, rather than a list.

cm_measurement = tuple([inch * 2.54 for inch in inch_measurement])
print(cm_measurement)
