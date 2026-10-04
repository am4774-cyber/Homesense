from homesense import (
    get_device_range,
    get_energy_status,
    requires_attention,
    calculate_cost
)


def test_led_light_range():
    assert get_device_range("LED Light") == (0.01, 0.10)


def test_television_range():
    assert get_device_range("Television") == (0.05, 0.50)


def test_upper_normal_boundary():
    assert get_energy_status("LED Light", 0.10) == "Normal"


def test_high_status():
    assert get_energy_status("LED Light", 0.18) == "High"


def test_critical_status():
    assert get_energy_status("LED Light", 0.21) == "Critical"


def test_attention_for_normal_reading():
    assert requires_attention("LED Light", 0.06) == False


def test_attention_for_high_reading():
    assert requires_attention("LED Light", 0.18) == True


def test_cost_calculation():
    assert calculate_cost(4.0, 0.30) == 1.20


def test_negative_energy():
    assert calculate_cost(-2.0, 0.30) == "Invalid"


def test_unknown_device():
    assert get_energy_status("Microwave", 1.0) == "Unknown Device"
