def calculate_soh(present_capacity, rated_capacity):
    """
    Calculate the State-of-Health (SoH) of a battery.

    Parameters:
    - present_capacity (float): The charge available in the battery after a full charge.
    - rated_capacity (float): The rated capacity of a new battery.

    Returns:
    - float: The State-of-Health percentage.
    """
    soh_percentage = (present_capacity / rated_capacity) * 100
    return soh_percentage
def classify_batteries(present_capacities):
    """
    Classify batteries based on State-of-Health (SoH).

    Parameters:
    - present_capacities (list): List of present capacities for a bunch of batteries.

    Returns:
    - tuple: Counts of healthy, exchange, and failed batteries.
    """
    # Define the rated capacity of a new battery
    rated_capacity = 120
    
    # Initialize counters for healthy, exchange, and failed batteries
    healthy_count = 0
    exchange_count = 0
    failed_count = 0
    
    # Iterate through each battery's present capacity
    for present_capacity in present_capacities:
        # Calculate state-of-health (SoH) in percentage
        soh_percentage = calculate_soh(present_capacity, rated_capacity)
        
        # Classify batteries based on SoH
        if soh_percentage > 80:
            healthy_count += 1
        elif 62 <= soh_percentage <= 80:
            exchange_count += 1
        else:
            failed_count += 1
    
    # Return the counts for each classification
    return healthy_count, exchange_count, failed_count

def count_batteries_by_health(present_capacities):
  return {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
 # Classify batteries and update counts
    for present_capacity in present_capacities:
        soh_percentage = calculate_soh(present_capacity, 120)

        if soh_percentage > 80:
            counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
