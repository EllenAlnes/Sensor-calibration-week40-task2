import json
from typing import Any

import pandas as pd
import yaml


def read_config() -> dict[str, Any]:
    """Reading settings from the YAML configuration file."""
    with open("config.yml") as file:
        config: dict[str, Any] = yaml.safe_load(file)

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


def export_to_json(data: pd.DataFrame, filename: str) -> None:
    """Export sensor data to a formatted JSON file."""
    records = data.to_dict(orient="records")

    # Write the JSON file
    with open(filename, "w") as file:
        json.dump(records, file, indent=2)


config = read_config()

sensors = read_sensors()

calibrations = read_calibrations()

data = join_sensor_data(sensors, calibrations)

overdue = filter_overdue_sensors(data, config["max_days_since_calibration"])

export_to_json(overdue, config["output_file"])
