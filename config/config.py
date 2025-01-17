# 默认配置
DEFAULT_API_KEY = ""
DEFAULT_APP_ID = ""
DEFAULT_WORKSPACE = ""

# 示例用法
#load_config_from_file(r"config/key_config.txt")
def load_config_from_file(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config


def creat_config_to_file(file_path, api_key, app_id, workspace):
    with open(file_path, 'w') as file:
        file.write(f"DEFAULT_API_KEY={api_key}\n")
        file.write(f"DEFAULT_APP_ID={app_id}\n")
        file.write(f"DEFAULT_WORKSPACE={workspace}\n")


