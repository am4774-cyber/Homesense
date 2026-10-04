# TASK 1.1 - Device Range
# Returns the normal energy range for each supported device
def get_device_range(device):
    if device == "LED Light":
        return 0.01 , 0.10
    elif device == "Television":
        return 0.05 , 0.50
    elif device == "Refrigerator":
        return 0.10 , 1.50
    elif device == "Washing Machine":
        return 0.30 , 2.50
    elif device == "Air Conditioner":
        return 0.50 , 5.00
    else:
        # Return None if the device is not supported
        return None 
    # TASK 1.2 - Energy Status
    # Determines whether the energy reading is Normal, High, or Critical
def get_energy_status(device,energy):
    device_range = get_device_range(device)
    # Check if the device is unknown
    if device_range is None:    
        return "Unknown Device"
    Minimum,Maximum = device_range
    # Energy within the normal range is classified as Normal
    if energy >= Minimum and energy <= Maximum:
        return "Normal"
    # Energy above the normal maximum up to twice the maximum is High
    elif energy > Maximum and energy <= Maximum*2:
        return "High"
    # Energy above twice the normal maximum is Critical
    else:
        return "Critical"
    # TASK 1.3 - Attention Required
    # Determines whether the reading requires attention
def requires_attention(device,energy):
    status = get_energy_status(device,energy)
    # Normal readings do not require attention
    if status == "Normal":
        return False
    else:
        # High and Critical readings require attention
        return True
    # TASK 2 - Cost Calculation
    # Calculates the estimated electricity cost
def calculate_cost(energy,rate):
    # Negative energy or rate values are considered invalid
    if energy < 0 or rate < 0:
        return "Invalid"
    estimate_cost = rate*energy
    return estimate_cost
# TASK 3 - Recommendations
# Provides a recommendation based on the device and its energy status
def recommendation_letter(device,energy):
    status = get_energy_status(device,energy)
    # Recommendations for Air Conditioner
    if device == "Air Conditioner":
        if status == "High":
            return "Check the operating duration and temperature settings"
        elif status == "Critical":
            return "turn off your device"
        else:
            return "the device status is good, I recommend maintaining it"
        # Recommendations for Television
    elif device == "Television":
         if status == "High":
            return "Check the operating duration"
         elif status == "Critical":
             return "turn off your TV"
         else:
             return "the device status is good, I recommend maintaining it"
         # Recommendations for LED Light
    elif device == "LED Light":
         if status == "High":
            return "Check the battery and wires"
         elif status == "Critical":
            return "turn off your led"
         else:
            return "the device status is good, I recommend maintaining it"
         # Recommendations for Refrigerator
    elif device == "Refrigerator":
         if status == "High":
            return "put an organizer"
         elif status == "Critical":
            return "turn off your refrigetor for a while"
         else:
            return "the device status is good, I recommend maintaining it"
         # Recommendations for Washing Machine
    elif device == "Washing Machine":
         if status == "High":
            return "check temperature and load"
         elif status == "Critical":
            return "turn off your washing machine for a while"
         else:
            return "the device status is good, I recommend maintaining it"
    else:
        return "Invalid"
    # TASK 4 - Sample Readings
    # Sample energy readings used by the HomeSense program
readings = [
    ("LED Light", 0.06),
    ("LED Light", 0.18),
    ("Television", 0.32),
    ("Television", 1.20),
    ("Refrigerator", 0.80),
    ("Refrigerator", 2.20),
    ("Washing Machine", 1.40),
    ("Washing Machine", 4.50),
    ("Air Conditioner", 2.80),
    ("Air Conditioner", 7.50)
]

         
print(get_device_range("LED Light"))
print(get_device_range("Television"))
print(get_device_range("Refrigerator"))
print(get_device_range("Washing Machine"))
print(get_device_range("Air Conditioner"))
print(get_device_range("Microwave"))


print(get_energy_status("LED Light",0.05))
print(get_energy_status("LED Light",0.05))
print(get_energy_status("Air Conditioner",11))
print(get_energy_status("Air Conditioner",2))


print(requires_attention("LED Light",0.05))
print(requires_attention("Television",5))
print(requires_attention("Air Conditioner",11))
print(requires_attention("Air Conditioner",2))



print(calculate_cost(5,4))
print(calculate_cost(3,1))

print( recommendation_letter("Television",5))
print( recommendation_letter("LED Light",0.02))

# Variables used to calculate the final HomeSense report
total_energy = 0
total_cost = 0

normal_count = 0
high_count = 0
critical_count = 0
attention_count = 0

highest_energy = 0
highest_device = ""
# TASK 4 - Process Readings
# TASK 5 - Calculate Summary
# Process all readings using a loop
for device, energy in readings:
    status = get_energy_status(device, energy)
    attention = requires_attention(device, energy)
    # Electricity rate is 0.30 AED per kWh
    cost = calculate_cost(energy, 0.30)

    print("Device: ",device,"Energy: ",energy,"Status: ",status,"Does it required attention: ",attention,"Cost: ",cost)
# Add the current reading to the total energy and cost
    total_energy += energy
    total_cost += cost
# Count readings according to their status
    if status == "Normal":
        normal_count = normal_count + 1
    elif status == "High":
        high_count = high_count + 1
    elif status == "Critical":
        critical_count = critical_count + 1
# Count readings that require attention
    if attention:
        attention_count = attention_count + 1
# Find the device with the highest individual consumption
    if energy > highest_energy:
        highest_energy = energy
        highest_device = device
# TASK 5 - HomeSense Report
# TASK 6 - Readable Report
# Display the final HomeSense report
print()
print("================================")
print("       HomeSense Report")
print("================================")
print("Total readings:", len(readings))
print()
print("Total energy consumed:", total_energy, "kWh")
print()
print("Total estimated cost: AED", round(total_cost, 2))
print()
print("Normal readings:", normal_count)
print("High readings:", high_count)
print("Critical readings:", critical_count)
print()
print("Readings requiring attention:", attention_count)
print()
print("Highest consumption device:", highest_device)
print("Highest individual consumption:", highest_energy, "kWh")
print("================================")

