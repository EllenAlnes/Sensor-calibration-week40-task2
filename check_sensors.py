import yaml


def read_config():
    with open("config.yml", "r") as file:
        config = yaml.safe_load(file)

        return config


config = read_config()
print(config)
