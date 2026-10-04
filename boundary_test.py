from homesense import get_energy_status, calculate_cost


print("===== Boundary and Unusual Cases =====")

print("1. LED Light at upper normal limit:")
print(get_energy_status("LED Light", 0.10))

print()

print("2. LED Light slightly above normal limit:")
print(get_energy_status("LED Light", 0.11))

print()

print("3. Air Conditioner significantly above normal limit:")
print(get_energy_status("Air Conditioner", 12.00))

print()

print("4. Unknown device:")
print(get_energy_status("Microwave", 1.00))

print()

print("5. Negative energy:")
print(calculate_cost(-2.0, 0.30))
