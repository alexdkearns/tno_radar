from iff import (format_radar_scan,
iff_scanner
)

def test_format_radar_scan():
    """Test function for radar scan formatter, tests for standard and edge cases where values
    are only 1s or 0s and a mixed binary that is non-standard format.
    """
    # Test Case 1: Standard radar data format.
    scan = ['0001010', '0110011', '0100110']
    expected_output = [0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
    print(format_radar_scan(scan))
    assert format_radar_scan(scan) == expected_output

    # Test Case 2: Edge case with only zeros.
    scan = ['000', '000']
    expected_output = [0, 0, 0, 0, 0, 0]
    assert format_radar_scan(scan) == expected_output

    # Test Case 3: Edge case with only ones.
    scan = ['111', '111']
    expected_output = [1, 1, 1, 1, 1, 1]
    assert format_radar_scan(scan) == expected_output

    # Test Case 4: Mixed binary values.
    scan = ['101', '010']
    expected_output = [1, 0, 1, 0, 1, 0]
    assert format_radar_scan(scan) == expected_output

def test_iff_scanner():
    """Test function for the iff scanner, tests standard inputs for hostile and no hostile.
    Also checks edge cases where there are only evens and only odds.
    """
    # Test Case 1: More odds than evens, should return True (hostile detected).
    radar_data = [1, 1, 0, 1, 1]
    assert iff_scanner(radar_data) is True

    # Test Case 2: More evens than odds, should return False (no hostile detected).
    radar_data = [0, 0, 1, 0, 0]
    assert iff_scanner(radar_data) is False

    # Test Case 3: Equal number of odds and evens, should return False (no hostile detected).
    radar_data = [1, 0, 1, 0]
    assert iff_scanner(radar_data) is False

    # Test Case 4: Only evens, should return False (no hostile detected).
    radar_data = [0, 0, 0, 0]
    assert iff_scanner(radar_data) is False

    # Test Case 5: Only odds, should return True (hostile detected).
    radar_data = [1, 1, 1, 1]
    assert iff_scanner(radar_data) is True
