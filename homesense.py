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
        return None 
def get_energy_status(device,energy):
    device_range = get_device_range(device)
    if device_range is None:    
        return "Unknown Device"
    Minimum,Maximum = device_range
    if energy >= Minimum and energy <= Maximum:
        return "Normal"
    elif energy > Maximum and energy <= Maximum*2:
        return "High"
    else:
        return "Critical"
def requires_attention(device,energy):
    status = get_energy_status(device,energy)
    if status == "Normal":
        return False
    else:
        return True
def calculate_cost(energy,rate):
    if energy < 0 or rate < 0:
        return "Invalid"
    estimate_cost = rate*energy
    return estimate_cost
def recommendation_letter(device,energy):
    status = get_energy_status(device,energy)
    if device == "Air Conditioner":

        if status == "High":
            return "Check the operating duration and temperature settings"
        elif status == "Critical":
            return "turn off your device"
        else:
            return "the device status is good, I recommend maintaining it"
    elif device == "Television":
         if status == "High":
            return "Check the operating duration"
         elif status == "Critical":
             return "turn off your TV"
         else:
             return "the device status is good, I recommend maintaining it"
    elif device == "LED Light":
         if status == "High":
            return "Check the battery and wires"
         elif status == "Critical":
            return "turn off your led"
         else:
            return "the device status is good, I recommend maintaining it"
    elif device == "Refrigerator":
         if status == "High":
            return "put an organizer"
         elif status == "Critical":
            return "turn off your refrigetor for a while"
         else:
            return "the device status is good, I recommend maintaining it"
    elif device == "Washing Machine":
         if status == "High":
            return "check temperature and load"
         elif status == "Critical":
            return "turn off your washing machine for a while"
         else:
            return "the device status is good, I recommend maintaining it"
    else:
        return "Invalid"
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


total_energy = 0
total_cost = 0

normal_count = 0
high_count = 0
critical_count = 0
attention_count = 0

highest_energy = 0
highest_device = ""

for device, energy in readings:
    status = get_energy_status(device, energy)
    attention = requires_attention(device, energy)
    cost = calculate_cost(energy, 0.30)

    print("Device: ",device,"Energy: ",energy,"Status: ",status,"Does it required attention: ",attention,"Cost: ",cost)

    total_energy += energy
    total_cost += cost

    if status == "Normal":
        normal_count = normal_count + 1
    elif status == "High":
        high_count = high_count + 1
    elif status == "Critical":
        critical_count = critical_count + 1

    if attention:
        attention_count = attention_count + 1

    if energy > highest_energy:
        highest_energy = energy
        highest_device = device
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

