import configparser
import os

FONT = "Courier"
FONT_SIZE = 8

def createConfig(path):
    """
    Create a config file
    """

    config = configparser.ConfigParser()

    config.add_section("Settings") # section heading - eg: [Settings]
    # .set(HEADING, KEY, VALUE)
    config.set("Settings", "font", FONT) # font = Courier
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", f"You are using {FONT}s at {FONT_SIZE} pt")

    with open(path, "w") as config_file:
        config.write(config_file)

def get_config(path):
    """
    Returns the config object
    """
    #create config only if it doesn't exist;
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """
    Get a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    return value

# It may not make any sense, but it exists
def get_setting_interpolation(path, section, setting, some_dict):
    """
    Get a setting using interpolation: change values of properties
    on the fly.
    """
    config = get_config(path)
    value = config.get(section, setting, vars = some_dict)
    return value

def set_or_update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)

def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    #--------------------------------------------------------
    current_dir = os.path.dirname(__file__)
    PATH = os.path.join(current_dir, 'settings.ini')
    #--------------------------------------------------------

    font = get_setting(PATH, 'Settings', 'font')
    font_size = get_setting(PATH, 'Settings', 'font_size')

    print(get_setting_interpolation(PATH, 'Settings', 'font', {"font": "Arial", "font_size": "100"})) # arial

    set_or_update_setting(PATH, "Settings", "font_size", "12")
    font_size = get_setting(PATH, 'Settings', 'font_size')

    delete_setting(PATH, "Settings", "font_style")
    font = get_setting(PATH, 'Settings', 'font_style')
