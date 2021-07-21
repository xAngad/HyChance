import os
from dotenv import load_dotenv
import requests
from pprint import pprint
from mojang import MojangAPI
load_dotenv()

class Player(object):
    def __init__(self, ign):
        super().__init__()
        self.uuid = MojangAPI.get_uuid(str(ign))
        self.api = os.getenv("API_KEY")
        self.link = f"https://api.hypixel.net/player?key={self.api}&uuid={self.uuid}"
        self.hydata = requests.get(self.link).json()
        self.stats = self.hydata["player"]["stats"]

    def rawStats(self):
        from utils import swXPtoLVL
        raw = {"bw": {},
               "sw": {},
               "duels": {}}

        # Bedwars
        raw["bw"]["level"] = self.hydata["player"]["achievements"]["bedwars_level"]
        raw["bw"]["kills"] = self.stats["Bedwars"]["kills_bedwars"]
        raw["bw"]["deaths"] = self.stats["Bedwars"]["deaths_bedwars"]
        raw["bw"]["fkills"] = self.stats["Bedwars"]["final_kills_bedwars"]
        raw["bw"]["fdeaths"] = self.stats["Bedwars"]["final_deaths_bedwars"]
        raw["bw"]["wins"] = self.stats["Bedwars"]["wins_bedwars"]
        raw["bw"]["losses"] = self.stats["Bedwars"]["losses_bedwars"]

        # SkyWars
        raw["sw"]["level"] = round(swXPtoLVL(self.stats["SkyWars"]["skywars_experience"]), 2) if "skywars_experience" in self.stats["SkyWars"] else 0
        raw["sw"]["kills"] = self.stats["SkyWars"]["kills"] if "kills" in self.stats["SkyWars"] else 0
        raw["sw"]["deaths"] = self.stats["SkyWars"]["deaths"] if "deaths" in self.stats["SkyWars"] else 0
        raw["sw"]["wins"] = self.stats["SkyWars"]["wins"] if "wins" in self.stats["SkyWars"] else 0
        raw["sw"]["losses"] = self.stats["SkyWars"]["losses"] if "losses" in self.stats["SkyWars"] else 0

        # Duels
        raw["duels"]["kills"] = self.stats["Duels"]["kills"]
        raw["duels"]["deaths"] = self.stats["Duels"]["deaths"]
        raw["duels"]["wins"] = self.stats["Duels"]["wins"]
        raw["duels"]["losses"] = self.stats["Duels"]["losses"]
        raw["duels"]["games"] = self.stats["Duels"]["games_played_duels"]

        return raw

    def predict(self):
        from utils import toPercentage
        raw = self.rawStats()
        predictions = {}

        predictions["sw"] = toPercentage(raw["sw"]["kills"], raw["sw"]["deaths"])
        predictions["bw"] = (toPercentage(raw["bw"]["kills"], raw["bw"]["deaths"]) + toPercentage(raw["bw"]["fkills"], raw["bw"]["fdeaths"])) / 2
        predictions["duels"] = toPercentage(raw["duels"]["wins"], raw["duels"]["losses"])

        return predictions