from typing import List

def format_radar_scan(scan: object) -> List[int]:
    """Flattens input format into a string then unpacks it into an Array of integers.
    Returns this Array. Makes the scanning algorthim more efficient.

    :param scan: Row in the radar data input e.g. 0001010;0110011;0100110
    :type scan: object
    :return: Array of binary integers.
    :rtype: List[int]
    """
    # flattens comma delimitted row into a string.
    binary_string = ''.join(scan)
    # creates array of integers from this string
    binary_array = [int(digit) for digit in binary_string]
    return binary_array

def iff_scanner(radar_data: List[int]) -> bool:
    """Takes list, pointers scan for odd values. Checks proportion of odd and evens.
    Returns True if hostile detected condition is met aka more odds than evens,
    Otherwise returns False.

    :param radar_data: Array representing radar scan data.
    :type radar_data: List[int]
    :return: Whether hostile is detected, number of odds > number of evens.
    :rtype: bool
    """
    # initialise pointers for scanning as well as length of radar data for later use.
    length = len(radar_data)
    left, right = 0, length - 1
    odd_count = 0

    # loop through data.
    while left <= right:
        # Check and count for the left pointer.
        if radar_data[left] % 2 != 0:
            odd_count += 1

        # Check and count for the right pointer, avoiding double-counting the middle.
        if left != right and radar_data[right] % 2 != 0:
            odd_count += 1

        # move left and right pointer every loop until they reach middle.
        left += 1
        right -= 1

    # Return True if hostile entity (more odds than evens), otherwise False.
    return odd_count > (length - odd_count)
