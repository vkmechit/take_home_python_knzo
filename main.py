import json

import pandas as pd


def load_config(config_path):
    """
    Load configuration from a JSON file.

    Args:
        config_path (str): Path to the JSON configuration file.

    Returns:
        dict: Loaded configuration dictionary.
    """
    with open(config_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded data as a pandas DataFrame.
    """
    return pd.read_csv(file_path)


def calculate_risk_score(row, config):
    """
    Calculate the risk score for a given alert based on various factors.

    Args:
        row (dict): Dictionary containing alert details.
        config (dict): Config dictionary containing weights and thresholds.

    Returns:
        float: Calculated risk score.
    """
    # Dynamic risk score calculation based on config
    alert_type_weight = config['alert_type_weights'].get(row['alert_type'], 1)

    severity_weight = config.get('severity_weight', 0.4)
    frequency_weight = config.get('frequency_weight', 0.3)
    role_weight = config.get('role_weight', 0.3)

    severity_score = row['severity'] * severity_weight

    frequency_score = 0
    if row['alert_count'] >= config['frequency_threshold']['count']:
        frequency_score = frequency_weight

    role_score = config['role_weights'].get(row['user_role'], 1) * role_weight

    source_ip_score = 5 if row['source_ip'] in config['ip_blacklist'] else 0

    # Calculate total risk score
    risk_score = (alert_type_weight + severity_score + frequency_score +
                  role_score + source_ip_score)
    return round(risk_score, 2)


def classify_priority(risk_score):
    """
    Classify the priority of a risk score.

    Args:
        risk_score (float): The calculated risk score.

    Returns:
        str: The priority classification ('High', 'Medium', or 'Low').
    """
    # Hardcoded the risk_score classification criteria for now
    if risk_score >= 8:
        return 'High'
    elif risk_score >= 5:
        return 'Medium'
    else:
        return 'Low'


def process_alerts():
    """
    Process security alerts by calculating risk scores and
    classifying priorities.

    Args:
        input_csv (str): Path to the input CSV file containing alerts.
        config_path (str): Path to the JSON config file.
        output_csv (str): Path to save the processed CSV file.

    Returns:
        None: Saves the processed data to the specified output CSV file.
    """
    config_path = "config.json"
    input_csv = "sample_input.csv"
    output_csv = "sample_output.csv"

    config = load_config(config_path)
    alerts = load_data(input_csv)

    risk_scores = []
    priorities = []

    for _, row in alerts.iterrows():
        risk_score = calculate_risk_score(row, config)
        priority = classify_priority(risk_score)
        risk_scores.append(risk_score)
        priorities.append(priority)

    alerts['risk_score'] = risk_scores
    alerts['priority'] = priorities

    # Save results
    alerts[['alert_id', 'risk_score', 'priority']].to_csv(
        output_csv,
        index=False
    )

    # Summary of priorities
    summary = alerts['priority'].value_counts()
    print("Priority Summary:")
    for priority, count in summary.items():
        print(f"{priority}: {count}")


if __name__ == "__main__":
    process_alerts()
