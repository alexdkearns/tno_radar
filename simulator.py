import csv
import time
from typing import List

from iff import (
        format_radar_scan,
        iff_scanner
        )

from firing_unit import simulate_engagement


def run_simulation(radar_data: List[str], pk=0.8) -> None:
    """Orchestrates simulation using the radar, IFF and firing unit.
    

    :param radar_data: Radar data object created from Radar scan output.
    :type radar_data: List[str]
    :param pk: Probability of kill, defaults to 0.8
    :type pk: float, optional
    """
    second = 1
    for scan in radar_data:
        binary_scan = format_radar_scan(scan)
        hostile = iff_scanner(binary_scan)
        print(f"Time-step {second}(s)")

        # IFF Identification based on precomputed hostility
        if hostile is True:
            print("  IFF: Hostile entity detected!")
            # Firing Unit - Launch Missile
            print("  Firing Unit: Missile launched.")

            # Engagement Success
            if simulate_engagement(pk):
                print("  Result: Target neutralised.")
            else:
                print("  Result: Engagement failed. Target still active.")
        else:
            print("  IFF: No hostile entity detected.")
        time.sleep(1)  # Simulate each time-step with a 1-second delay
        second += 1

# Load radar data from radar-output.csv
def load_radar_data(filename: str) -> list[str]:
    """Loads Radar data from csv file, using standard open python library.

    :param filename: File path for radar data.
    :type filename: str
    :return: Radar data object as List/1D Array.
    :rtype: list[int]
    """
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        radar_data = list(reader)
    return radar_data


# Main Execution
if __name__ == "__main__":
    # Load Radar Data from csv
    radar_scan = load_radar_data('radar_data.csv')
    # Simulate on loaded radar data
    run_simulation(radar_scan)
