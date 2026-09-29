import yaml
import pandas as pd


def read_config() -> dict[str, int | str]:
    """Reading settings from the YAML configuration file."""
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)

        return config


def read_sensors() -> pd.DataFrame:
    """Read sensor information from the Excel file."""
    sensors = pd.read_excel("sensors.xlsx")

    return sensors


def read_calibrations() -> pd.DataFrame:
    """Read calibration information form the CSV file."""
    calibrations = pd.read_csv("calibrations.csv")

    return calibrations


def join_sensor_data(sensors: pd.DataFrame, calibrations: pd.DataFrame) -> pd.DataFrame:
    """Join sensor information with calibration information."""
    data = sensors.merge(calibrations, on="sensor_id")

    return data


def filter_overdue_sensors(data: pd.DataFrame, max_days: int) -> pd.DataFrame:
    """Return sensors whose calibration is overdue."""
    condition = data["days_since_calibration"] > max_days
    overdue = data[condition]

    return overdue


config = read_config()
print(config)

sensors = read_sensors()
print(sensors)

calibrations = read_calibrations()
print(calibrations)

data = join_sensor_data(sensors, calibrations)
print(data)

overdue = filter_overdue_sensors(data, config["max_days_since_calibration"])
print(overdue)
