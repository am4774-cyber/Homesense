# TASK 7 - Boundary and Unusual Cases
from homesense import get_energy_status, calculate_cost

print("===== Boundary and Unusual Cases =====")

# Case 1 - Upper normal boundary
print("1. LED Light at upper normal limit:")
print(get_energy_status("LED Light", 0.10))

print()
# Case 2 - Slightly above normal limit
print("2. LED Light slightly above normal limit:")
print(get_energy_status("LED Light", 0.11))

print()
# Case 3 - Significantly above normal limit
print("3. Air Conditioner significantly above normal limit:")
print(get_energy_status("Air Conditioner", 12.00))

print()
# Case 4 - Unknown device
print("4. Unknown device:")
print(get_energy_status("Microwave", 1.00))

print()
# Case 5 - Negative energy
print("5. Negative energy:")
print(calculate_cost(-2.0, 0.30))
