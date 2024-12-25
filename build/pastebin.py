import requests
import xml.etree.ElementTree as ET

class PastebinManager:
    def __init__(self, api_dev_key, api_user_name, api_user_password):
        self.api_dev_key = api_dev_key
        self.user_key = self.get_user_key(api_user_name, api_user_password)

    def get_user_key(self, username, password):
        url = "https://pastebin.com/api/api_login.php"
        payload = {
            "api_dev_key": self.api_dev_key,
            "api_user_name": username,
            "api_user_password": password,
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.text

    def create_paste(self, content, name, private=0, expire="N"):
        url = "https://pastebin.com/api/api_post.php"
        payload = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.user_key,
            "api_option": "paste",
            "api_paste_code": content,
            "api_paste_name": name,
            "api_paste_private": private,
            "api_paste_expire_date": expire,
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        return response.text

    def delete_paste(self, paste_id):
        url = "https://pastebin.com/api/api_post.php"
        payload = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.user_key,
            "api_option": "delete",
            "api_paste_key": paste_id,
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()

    def fetch_user_pastes(self):
        """
        Fetch a list of all pastes for the authenticated user.
        """
        url = "https://pastebin.com/api/api_post.php"
        payload = {
            "api_dev_key": self.api_dev_key,
            "api_user_key": self.user_key,
            "api_option": "list",
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()

        # Parse XML response
        pastes = []
        root = ET.fromstring(response.text)
        for paste in root.findall("paste"):
            pastes.append({
                "paste_key": paste.find("paste_key").text,
                "paste_title": paste.find("paste_title").text,
            })
        return pastes

    def get_paste_id_by_name(self, name):
        """
        Search for a paste by name and return its ID if found.
        """
        pastes = self.fetch_user_pastes()
        for paste in pastes:
            if paste["paste_title"] == name:
                return paste["paste_key"]
        return None
