""" Provide default arguments for functions. """

import argparse
import yaml
import os


def load_config(config_path):
    """Load YAML config file."""
    # check if the file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config


def get_config_from_yaml_with_arg(description="Machine Learning Python Template"):
    """get config from yaml with -c/--config argument"""

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        required=True,
        help="Path to YAML configuration file",
    )
    # Parse arguments
    args = parser.parse_args()

    # Load config
    config = load_config(args.config)

    return config
