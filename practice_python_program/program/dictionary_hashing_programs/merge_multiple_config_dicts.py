"""
Interview Question: How do you merge multiple configuration dictionaries with precedence in Python?

Interview Explanation:
"In automation frameworks, configuration values cascade from default -> environment -> CLI arguments.
I can use `dict1 | dict2 | dict3` in Python 3.9+, or a custom recursive deep merge helper to merge nested config dicts."
"""

def merge_configs(*configs: dict) -> dict:
    merged = {}
    for config in configs:
        merged.update(config)
    return merged

if __name__ == "__main__":
    default_config = {"browser": "chrome", "timeout": 10, "headless": False}
    env_config = {"timeout": 30, "env": "staging"}
    cli_config = {"headless": True}

    final_config = merge_configs(default_config, env_config, cli_config)
    print("Final Cascaded Config:", final_config)
