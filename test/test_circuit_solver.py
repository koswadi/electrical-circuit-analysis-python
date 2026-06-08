from src.circuit_solver import (
    calculate_current,
    calculate_voltage,
    calculate_resistance
)

def test_calculate_current():
    assert calculate_current(12, 6) == 2

def test_calculate_voltage():
    assert calculate_voltage(2, 6) == 12

def test_calculate_resistance():
    assert calculate_resistance(12, 2) == 6