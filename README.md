# HomeSense - Smart Home Energy Monitor

## Project Description

HomeSense is a Python program that monitors energy consumption for different smart-home devices.

The program classifies energy readings as Normal, High, or Critical, determines whether attention is required, calculates estimated electricity costs, and produces a summary report.

## Supported Devices

The program supports the following devices:

* LED Light
* Television
* Refrigerator
* Washing Machine
* Air Conditioner

Each device has its own normal operating energy range.

## High and Critical Rule

The program uses the following classification rule:

* Normal: the energy reading is within the normal range, including the minimum and maximum values.
* High: the reading is above the normal maximum and up to two times the normal maximum.
* Critical: the reading is above two times the normal maximum.

This rule was selected as the design rule for the HomeSense program.

## Main Functions

The program contains functions for:

* Getting the normal operating range of a device.
* Determining the energy status.
* Determining whether attention is required.
* Calculating estimated electricity cost.

## Sample Readings

The program processes 10 sample energy readings for the supported devices.

The readings are processed using a loop rather than separate code for each reading.

For each reading, the program displays the device, energy consumption, status, attention requirement, and estimated cost.

## Report

The program calculates and displays:

* Total number of readings
* Total energy consumed
* Total estimated cost
* Number of Normal readings
* Number of High readings
* Number of Critical readings
* Number of readings requiring attention
* Device with the highest individual consumption

## Testing

The project includes a pytest test file named `test_homesense.py`.

The test file contains 10 tests covering different parts of the program, including normal operation, boundary values, High and Critical classifications, attention requirements, cost calculation, invalid values, and unknown devices.

All 10 tests passed successfully.

## Boundary and Unusual Cases

The project also includes `boundary_test.py`, which demonstrates boundary and unusual cases such as:

* An energy reading at the upper normal limit.
* A reading slightly above the normal limit.
* A significantly high reading.
* An unknown device.
* Negative energy input.

## Files

* `homesense.py` - Main HomeSense Python program.
* `boundary_test.py` - Boundary and unusual case demonstrations.
* `test_homesense.py` - Pytest test cases.
* `DESIGN_EXPLANATION.md` - Explanation of the program design.
* `README.md` - Project overview and documentation.
