#!/usr/bin/python3
"""Check readme for full description"""


def rain(walls):
	"""Function to calculate the water retained by the walls"""
    if not walls:  # If the list is empty, return 0
	return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_trapped = 0

    while left < right:
        if walls[left] <= walls[right]:
            if walls[left] < left_max:
                water_trapped += left_max - walls[left]
            else:
                left_max = walls[left]
            left += 1
        else:
            if walls[right] < right_max:
                water_trapped += right_max - walls[right]
            else:
                right_max = walls[right]
            right -= 1

    return water_trapped
