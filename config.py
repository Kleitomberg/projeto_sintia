import os
from typing import Final

import yaml


class Config:
    def __init__(self) -> None:
        path_config_file = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(path_config_file, "r") as f:
            variables = yaml.safe_load(f)

            # DJANGO
            self.secret_key: Final = variables["settings"]["secret_key"]
            self.debug: Final = True if variables["settings"]["debug"] == "1" else "0"
            self.hosts: Final = variables["settings"]["hosts"]
            self.CSRF: Final = variables["settings"]["hosts_CSRF"]
            self.database: Final = variables["settings"]["database_url"]

            # chatBot
            self.chatbot_url: Final = variables["chatbot"]["url"]
            self.chatbot_password: Final = variables["chatbot"]["password"]
            self.chatbot_username: Final = variables["chatbot"]["username"]

            # Email
            self.email: Final = variables["email"]["email"]
            self.mail_password: Final = variables["email"]["password"]
