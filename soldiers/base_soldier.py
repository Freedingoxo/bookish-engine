from datetime import datetime
from typing import Dict

class BaseSoldier:
    def __init__(self, name: str, rank: str, division: str, specialty: str):
        self.name = name
        self.rank = rank
        self.division = division
        self.specialty = specialty
        self.status = "active"
        self.missions_completed = 0
        self.logs = []
    
    def log(self, message: str):
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "soldier": self.name,
            "message": message
        })
    
    def execute_mission(self, mission: Dict) -> Dict:
        self.log(f"تنفيذ مهمة: {mission.get('action', 'unknown')}")
        self.missions_completed += 1
        return {
            "status": "success",
            "soldier": self.name,
            "rank": self.rank,
            "division": self.division,
            "mission": mission,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_report(self) -> Dict:
        return {
            "name": self.name,
            "rank": self.rank,
            "division": self.division,
            "specialty": self.specialty,
            "status": self.status,
            "missions_completed": self.missions_completed
        }
