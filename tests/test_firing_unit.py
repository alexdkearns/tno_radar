from unittest.mock import patch
from firing_unit import simulate_engagement

def test_simulate_engagement_mocked():
    """Test mocks the randomly generated value and uses this to check if it correctly
    compares this to the pk.
    """
    # Test Case 1: Mock `lib.get_random_value` to return a value below pk
    with patch('firing_unit.lib.get_random_value', return_value=0.5):
        assert simulate_engagement(0.8) is True  # 0.5 <= 0.8, should return True

    # Test Case 2: Mock `lib.get_random_value` to return a value equal to pk
    with patch('firing_unit.lib.get_random_value', return_value=0.8):
        assert simulate_engagement(0.8) is True  # 0.8 <= 0.8, should return True

    # Test Case 3: Mock `lib.get_random_value` to return a value above pk
    with patch('firing_unit.lib.get_random_value', return_value=0.9):
        assert simulate_engagement(0.8) is False  # 0.9 > 0.8, should return False
