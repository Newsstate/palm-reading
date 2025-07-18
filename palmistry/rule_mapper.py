import json

def map_features_to_prediction(features):
    with open('data/palmistry_rules.json') as f:
        rules = json.load(f)

    if features['line_count'] > 10:
        return rules.get('complex_hand', 'Unknown')
    else:
        return rules.get('simple_hand', 'Unknown')