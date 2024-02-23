"""
This file allows for access to the stats of the current season. The user can view the
current standings, the statistical leaders, and the recent and upcoming games. The user
can also access the managerial settings to make any adjustments to the team.
"""

import json

class Season:

    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {'standings': {}, 'stats': {}}
        
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)
    
