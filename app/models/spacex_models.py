import requests
from datetime import datetime

class Mission:
    def __init__(self, id, name, date_utc, success):
        self.id = id
        self.name = name
        self.date = datetime.fromisoformat(date_utc.replace('Z', '+00:00'))
        self.success = success
        self.details = ""
        self.links = {}
        self.rocket_name = ""
        self.rocket_image = ""

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date.strftime('%Y-%m-%d %H:%M:%S'), 
            "success": self.success,
            "details": self.details,
            "links": self.links,
            "rocket_name": self.rocket_name,
            "rocket_image": self.rocket_image
        }

class DataManager:
    def __init__(self):
        self.api_base_url = "https://api.spacexdata.com/v4"
    
    def fetch_all_missions(self):
            reponse = requests.get(f"{self.api_base_url}/launches")
            donnees_lancements = reponse.json()

            missions = []
            for lancement in donnees_lancements:
                mission = Mission(
                    lancement['id'],
                    lancement['name'],
                    lancement['date_utc'],
                    lancement.get('success', False)
                )
                
                mission.details = lancement.get('details', '')
                mission.links = lancement.get('links', {})
                
                missions.append(mission)
            
            return missions