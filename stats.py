import os
from dotenv import load_dotenv
import requests
from pprint import pprint
from mojang import MojangAPI
load_dotenv()

from utils import swXPtoLVL

class Player(object):
    def __init__(self, ign):
        super().__init__()
        self.uuid = MojangAPI.get_uuid(str(ign))
        self.api = os.getenv("API_KEY")
        self.link = f"https://api.hypixel.net/player?key={self.api}&uuid={self.uuid}"
        self.hydata = requests.get(self.link).json()
        self.stats = self.hydata["player"]["stats"]

    def rawStats(self):
        raw = {"bw": {},
                 "sw": {},
                 "duels": {}}

        # Bedwars
        raw["bw"]["level"] = self.hydata["player"]["achievements"]["bedwars_level"]
        raw["bw"]["kills"] = self.stats["Bedwars"]["kills_bedwars"]
        raw["bw"]["deaths"] = self.stats["Bedwars"]["deaths_bedwars"]
        raw["bw"]["fkills"] = self.stats["Bedwars"]["final_kills_bedwars"]
        raw["bw"]["fdeaths"] = self.stats["Bedwars"]["final_deaths_bedwars"]

        # SkyWars
        raw["sw"]["level"] = round(swXPtoLVL(self.stats["SkyWars"]["skywars_experience"]), 2)
        raw["sw"]["kills"] = self.stats["SkyWars"]["kills"]
        raw["sw"]["deaths"] = self.stats["SkyWars"]["deaths"]
        raw["sw"]["wins"] = self.stats["SkyWars"]["wins"]
        raw["sw"]["losses"] = self.stats["SkyWars"]["losses"]

        # Duels
        raw["duels"]["kills"] = self.stats["Duels"]["kills"]
        raw["duels"]["wins"] = self.stats["Duels"]["wins"]
        raw["duels"]["losses"] = self.stats["Duels"]["losses"]

        return raw


angad = Player("xAngad")
pprint(angad.rawStats())