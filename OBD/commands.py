
# A * 256 + B
def Astar256plusB(messages):
    d = messages[4:6]
    d = int(d, 16)
    d2 = messages[6:8]
    d2 = int(d2, 16)
    d = d * 256 + d2
    return d


# A * 100 /255
def Astart100div255(messages):
    d = int(messages[4:], 16)
    d = d * 100 / 255
    return d


# fuel Pressure
def fuel_pressure(messages):
    d = int(messages[4:], 16)
    d = d * 3
    print(d)
    return d


# control module voltage
def control_module_voltage(messages):
    return Astar256plusB(messages) / 1000


# Timing Advance
def timing_advance(messages):
    d = int(messages[4:], 16)
    d = d / 2 - 64
    return d


# Ethanol fuel %
def ethanol_fuel_percent(messages):
    return Astart100div255(messages)


# Evap system vapor pressure
def evap_system_vapor_pressure(messages):
    return Astar256plusB(messages) - 32768


# aux input status
def aux_input_status(messages):
    d = int(messages[4:5], 16)
    return ((d >> 7) & 1) == 1  # first bit indicate PTO status


# engine RPM
def engine_RPM(messages):
    x = Astar256plusB(messages) / 4
    print(x)
    return x


# Engine Coolant temperature
def engine_coolant_temperature(messages):
    d = messages[4:]
    d = int(d, 16)
    d = d - 40
    return d


# Engine Load Valued
def engine_load_value(messages):
    return Astart100div255(messages)


# Throttle Position
def throttle_position(messages):
    return Astart100div255(messages)


# Absolute throttle position B or C
def absolute_throttle_position(messages):
    return Astart100div255(messages)


# Absolute pedal position d or E or F
def absolute_pedal_position(messages):
    return Astart100div255(messages)


# Runtime since engine start
def runtime_since_engine_start(messages):
    return Astar256plusB(messages)


# Distance since codes Cleared
def distance_since_codes_cleared(messages):
    return Astar256plusB(messages)


# Distance since MIL on
def distance_with_mil_on(messages):
    return Astar256plusB(messages)


# Commanded throttle actuator
def commanded_throttle_actuator(messages):
    return Astart100div255(messages)


# Time run with MIL on
def time_run_with_mil_on(messages):
    return Astar256plusB(messages)


# Time since trouble codes cleared 0
def time_since_trouble_codes_cleared(messages):
    return Astar256plusB(messages)


# Maximum value for air flow rate from mass air flow sensor
def max_value_air_flow_rate(messages):
    return int(messages[4:], 16) * 10


# of warm-ups since codes cleared
def warmups_since_codes_cleared(messages):
    return messages[2]


# Barometric Pressure
def barometric_pressure(messages):
    return int(messages[4:], 16)


# Vehicle Speed
def vehicle_speed(messages):
    d = int(messages[4:], 16)
    return d


# Fuel Level Input
def fuel_level_input(messages):
    return Astart100div255(messages)


# Commanded EGR
def commandedEGR(messages):
    return Astart100div255(messages)


# Intake manifold absolute pressure
def intake_manifold_absolute_pressure(messages):
    d = messages[4:]
    d = int(d, 16)
    return d


# Intake air Temperature
def intake_air_temperature(messages):
    d = messages[4:]
    d = int(d, 16)-40
    return d


# MAF_air_flow_rate
def MAF_air_flow_rate(messages):
    d = Astar256plusB(messages)
    return d / 100


# Absolute Load Value
def absolute_load_value(messages):
    v = Astar256plusB(messages) * 100 / 255
    return v


# Command equivalence ratio
def command_equivalence_ratio(messages):
    return Astar256plusB(messages) / 32768


# Relative Accelerator Pedal Position
def accelerator_pedal_position(messages):
    return Astart100div255(messages)


# Engine oil temperature
def engine_oil_temperature(messages):
    v = int(messages[4:], 16)
    return v - 40


# number of warm-ups since codes cleared
def warm_ups_since_code_cleared(messages):
    return int(messages[4:], 16)


# Relative Throttle Position
def relative_throttle_position(messages):
    return Astart100div255(messages)


def fuel_injection_timing(messages):
    d = Astar256plusB(messages) - 26880
    d = d / 128
    return d


# Fuel rail pressure (absolute)
def fuel_rail_pressure(messages):
    return Astar256plusB(messages) * 10


# Fuel Rail Pressure (relative to manifold vacuum)
def fuel_rail_pressure_manifold(messages):
    return Astar256plusB(messages) * 0.079


# Fuel Rail Pressure (diesel, or gasoline direct inject)
def fuel_rail_pressure_injection(messages):
    return Astar256plusB(messages) * 10


# Engine fuel rate
def engine_fuel_rate(messages):
    v = Astar256plusB(messages) * 0.05
    return v


# Hybrid battery remaining
def battery_remaining(messages):
    return Astart100div255(messages)


# Driver's demand engine - percent torque
def engine_torque_percent(messages):
    d = int(messages[4:], 16) - 125
    return d


# Actual engine - percent torque
def engine_percent_torque(messages):
    d = int(messages[4:], 16) - 125
    return d


# Engine reference torque
def engine_reference_torque(messages):
    return Astar256plusB(messages)


# Short term fuel % trim—Bank 1 (A-128) * 100/128
def short_long_term_bank_1_2(messages):
    d = int(messages[4:], 16) - 128
    d = d * 100 / 128
    return d


# Catalyst Temperature Bank 1, Sensor 1, Bank 2, sensor 2
def catalyst_temp_bank1(messages):
    d = Astar256plusB(messages) / 10
    d = d - 40
    return d


# EGR Error
def EGR_error(messages):
    d = int(messages[4:], 16) - 128
    d = d * 100 / 128
    return d


# Ambient Air Temp
def air_temp(messages):
    d = int(messages[4:], 16) - 40
    return d
