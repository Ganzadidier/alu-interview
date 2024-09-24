#!/usr/bin/python3
"""Check readme for full description"""


def rain(walls):
    """
    This function calculates the total amount of rainwater that can be trapped between walls after it rains.
    
    Parameters:
    walls (list): A list of non-negative integers where each integer represents the height of a wall with width 1.
    
    Returns:
    int: The total number of units of water that can be trapped between the walls.
    """
    # If the list is empty, no water can be trapped, so return 0
    if not walls:
        return 0
    
    # Initialize two pointers, one starting from the left and the other from the right
    left, right = 0, len(walls) - 1
    
    # Initialize variables to keep track of the maximum wall heights encountered from both the left and the right
    left_max, right_max = walls[left], walls[right]
    
    # Variable to accumulate the total amount of water trapped
    water_trapped = 0
    
    # Loop until the two pointers meet
    while left < right:
        # If the wall on the left is shorter or equal to the one on the right, move the left pointer
        if walls[left] <= walls[right]:
            # If the current left wall is shorter than the maximum wall seen from the left, trap water
            if walls[left] < left_max:
                # Water trapped at this position is the difference between left_max and the current wall height
                water_trapped += left_max - walls[left]
            else:
                # Update left_max if the current wall is the tallest seen so far from the left
                left_max = walls[left]
            # Move the left pointer to the right
            left += 1
        else:
            # If the current right wall is shorter than the maximum wall seen from the right, trap water
            if walls[right] < right_max:
                # Water trapped at this position is the difference between right_max and the current wall height
                water_trapped += right_max - walls[right]
            else:
                # Update right_max if the current wall is the tallest seen so far from the right
                right_max = walls[right]
            # Move the right pointer to the left
            right -= 1
    
    # Return the total amount of water trapped
    return water_trapped
