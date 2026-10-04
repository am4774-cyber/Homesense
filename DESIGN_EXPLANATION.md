# HomeSense - Design Explanation

## 1. Program Decomposition

The HomeSense program was divided into several functions so that each function has a clear and specific responsibility.

The `get_device_range()` function returns the normal operating range for a given device.

The `get_energy_status()` function determines whether an energy reading is Normal, High, or Critical.

The `requires_attention()` function determines whether a reading requires attention based on its status.

The `calculate_cost()` function calculates the estimated electricity cost using the energy consumption and electricity rate.

The main part of the program processes multiple energy readings using a loop and calculates the required information for each reading.

## 2. Normal, High, and Critical Decision-Making

The program uses conditions to classify each energy reading.

A reading is classified as Normal when it is within the device's normal operating range, including the lower and upper limits.

For readings above the normal maximum, the program uses the following rule:

* Normal: from the minimum value up to and including the maximum value.
* High: above the normal maximum and up to two times the maximum value.
* Critical: above two times the normal maximum value.

For example, the normal range for an Air Conditioner is 0.50 to 5.00 kWh. Therefore, a reading up to and including 5.00 kWh is Normal, a reading above 5.00 and up to 10.00 kWh is High, and a reading above 10.00 kWh is Critical.

This High/Critical rule was selected as the design rule for this program.

## 3. Boundary Handling

The upper boundary of the normal range is included in the Normal category.

For example, an LED Light reading of exactly 0.10 kWh is classified as Normal because 0.10 kWh is the upper limit of its normal range.

A reading slightly above the upper limit is classified as High according to the selected rule.

The program also handles unusual cases such as negative energy values and unknown devices.

## 4. Different Devices

The program supports five different devices:

* LED Light
* Television
* Refrigerator
* Washing Machine
* Air Conditioner

Each device has its own normal operating range. The `get_device_range()` function is used to obtain the correct range based on the device name.

If an unknown device is provided, the program returns `Unknown Device`.

## 5. Processing Multiple Readings

The sample readings are stored in a list.

A `for` loop is used to process all readings instead of writing separate code for every reading.

For each reading, the program determines:

* Device name
* Energy consumption
* Energy status
* Whether attention is required
* Estimated cost

The program also keeps counters and totals to produce the final HomeSense report.

## 6. Testing

The program was tested using pytest.

The test file contains 10 meaningful test cases covering device ranges, normal readings, boundary values, High status, Critical status, attention requirements, cost calculation, invalid energy values, and unknown devices.

All 10 tests passed successfully.

Additional boundary and unusual cases were also tested separately, including an upper normal boundary, a value above the normal range, a significantly high value, an unknown device, and negative energy.
