# calculate_total_demo.py — trainer demo (contains ONE deliberate bug)
import logging
 
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
 
def calculate_total(numbers):
    """Return the sum of downtime minutes."""
    total = 0
    for n in numbers:
        total = total + n
    return total   # deliberate bug: NameError
 
north_dc = [45, 30, 120, 15]   # downtime minutes per incident
print("North DC total downtime:", calculate_total(north_dc))