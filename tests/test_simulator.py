from unittest.mock import patch

from simulator import run_simulation


def test_run_simulation_hostile_detected_and_engagement_successful(capsys):
    """Tests for hostile detected and successful hit;
    with iff_scanner=True, simulate_engagement=True.

    :param capsys: allows capture of system message.
    :type capsys: module.
    """
    radar_data = [['0001010', '0110011', '0100110']]  # Example radar data

    with patch('simulator.format_radar_scan', return_value=[0, 1, 0, 1, 1]), \
         patch('iff.iff_scanner', return_value=True), \
         patch('simulator.simulate_engagement', return_value=True), \
         patch('simulator.time.sleep', return_value=None):

        run_simulation(radar_data, pk=0.8)
        captured = capsys.readouterr()
        assert "IFF: Hostile entity detected!" in captured.out
        assert "Firing Unit: Missile launched." in captured.out
        assert "Result: Target neutralised." in captured.out

def test_run_simulation_hostile_detected_and_engagement_failed(capsys):
    """Tests for hostile detected and unsuccessful hit;
    with iff_scanner=True, simulate_engagement=False.

    :param capsys: allows capture of system message.
    :type capsys: module
    """
    radar_data = [['0001010', '0110011', '0100110']]

    with patch('simulator.format_radar_scan', return_value=[0, 1, 0, 1, 1]), \
         patch('iff.iff_scanner', return_value=True), \
         patch('simulator.simulate_engagement', return_value=False), \
         patch('simulator.time.sleep', return_value=None):

        run_simulation(radar_data, pk=0.8)
        captured = capsys.readouterr()
        assert "IFF: Hostile entity detected!" in captured.out
        assert "Firing Unit: Missile launched." in captured.out
        assert "Result: Engagement failed. Target still active." in captured.out


def test_run_simulation_no_hostile_detected(capsys):
    """Test for no hostile detected.
    with iff_scanner=False.

    :param capsys: allows capture of system message.
    :type capsys: module
    """
    radar_data = [['0001010', '0110011', '0100110']]

    with patch('simulator.format_radar_scan', return_value=[0, 0, 0, 0, 0]), \
         patch('iff.iff_scanner', return_value=False), \
         patch('simulator.time.sleep', return_value=None):

        run_simulation(radar_data, pk=0.8)
        captured = capsys.readouterr()
        assert "IFF: No hostile entity detected." in captured.out
