"""This file contains the 3 main colors for all 32 NFL teams that the game can
Call upton to customize the different views and buttons in the game for the user
based on the team that they select and the teams that they will play."""

nfl_team_colors = {
    'Arizona Cardinals': {
        'primary': (155, 35, 63),    # Cardinal Red
        'secondary': (255, 255, 255), # White
        'tertiary': (0, 0, 0)         # Black
    },
    'Atlanta Falcons': {
        'primary': (196, 20, 28),    # Red
        'secondary': (0, 0, 0),       # Black
        'tertiary': (152, 157, 159)   # Silver
    },
    'Baltimore Ravens': {
        'primary': (26, 25, 95),      # Purple
        'secondary': (0, 0, 0),       # Black
        'tertiary': (255, 121, 0)     # Gold
    },
    'Buffalo Bills': {
        'primary': (0, 51, 141),      # Royal Blue
        'secondary': (198, 12, 48),   # Red
        'tertiary': (0, 0, 0)         # Black
    },
    'Carolina Panthers': {
        'primary': (0, 133, 202),     # Panther Blue
        'secondary': (0, 0, 0),       # Black
        'tertiary': (138, 141, 144)   # Silver
    },
    'Chicago Bears': {
        'primary': (12, 35, 64),      # Navy Blue
        'secondary': (221, 72, 20),   # Orange
        'tertiary': (0, 0, 0)         # Black
    },
    'Cincinnati Bengals': {
        'primary': (252, 76, 2),      # Orange
        'secondary': (0, 0, 0),       # Black
        'tertiary': (247, 151, 30)    # White
    },
    'Cleveland Browns': {
        'primary': (61, 31, 6),       # Seal Brown
        'secondary': (255, 255, 255), # White
        'tertiary': (165, 42, 42)     # Orange
    },
    'Dallas Cowboys': {
        'primary': (0, 34, 68),       # Navy Blue
        'secondary': (165, 172, 175), # Silver
        'tertiary': (255, 255, 255)   # White
    },
    'Denver Broncos': {
        'primary': (0, 34, 68),       # Broncos Orange
        'secondary': (251, 79, 20),   # Navy Blue
        'tertiary': (255, 255, 255)   # White
    },
    'Detroit Lions': {
        'primary': (0, 118, 182),     # Honolulu Blue
        'secondary': (176, 183, 188), # Silver
        'tertiary': (0, 0, 0)         # Black
    },
    'Green Bay Packers': {
        'primary': (24, 48, 40),      # Dark Green
        'secondary': (255, 184, 28),  # Gold
        'tertiary': (255, 255, 255)   # White
    },
    'Houston Texans': {
        'primary': (0, 34, 68),       # Deep Steel Blue
        'secondary': (166, 25, 46),   # Battle Red
        'tertiary': (255, 255, 255)   # White
    },
    'Indianapolis Colts': {
        'primary': (0, 44, 95),       # Speed Blue
        'secondary': (162, 170, 173), # Gray
        'tertiary': (255, 255, 255)   # White
    },
    'Jacksonville Jaguars': {
        'primary': (0, 103, 120),     # Teal
        'secondary': (16, 24, 32),    # Black
        'tertiary': (145, 153, 161)   # Gold
    },
    'Kansas City Chiefs': {
        'primary': (227, 24, 55),     # Red
        'secondary': (198, 12, 48),   # Gold
        'tertiary': (255, 255, 255)   # White
    },
    'Las Vegas Raiders': {
        'primary': (0, 0, 0),         # Black
        'secondary': (165, 172, 175), # Silver
        'tertiary': (255, 255, 255)   # White
    },
    'Los Angeles Chargers': {
        'primary': (0, 42, 94),       # Powder Blue
        'secondary': (255, 255, 255), # White
        'tertiary': (198, 12, 48)     # Gold
    },
    'Los Angeles Rams': {
        'primary': (0, 53, 148),      # Rams Royal
        'secondary': (0, 0, 0),       # Sol
        'tertiary': (255, 209, 0)     # Millenium Gold
    },
    'Miami Dolphins': {
        'primary': (0, 142, 151),     # Aqua Green
        'secondary': (252, 76, 2),    # Orange
        'tertiary': (255, 255, 255)   # White
    },
    'Minnesota Vikings': {
        'primary': (79, 38, 131),     # Purple
        'secondary': (0, 0, 0),       # Gold
        'tertiary': (255, 255, 255)   # White
    },
    'New England Patriots': {
        'primary': (0, 34, 68),       # Nautical Blue
        'secondary': (176, 183, 188), # New Century Silver
        'tertiary': (207, 20, 43)     # Red
    },
    'New Orleans Saints': {
        'primary': (211, 188, 141),   # Old Gold
        'secondary': (16, 24, 32),    # Black
        'tertiary': (255, 255, 255)   # White
    },
    'New York Giants': {
        'primary': (1, 35, 82),       # Giants Blue
        'secondary': (163, 13, 45),   # Red
        'tertiary': (255, 255, 255)   # White
    },
    'New York Jets': {
        'primary': (0, 0, 0),         # Gotham Green
        'secondary': (14, 104, 43),   # Spotlight White
        'tertiary': (203, 164, 126)   # Stealth Black
    },
    'Philadelphia Eagles': {
        'primary': (0, 76, 84),       # Midnight Green
        'secondary': (163, 13, 45),   # Eagle Green
        'tertiary': (255, 255, 255)   # White
    },
    'Pittsburgh Steelers': {
        'primary': (0, 0, 0),         # Black
        'secondary': (255, 182, 18),  # Gold
        'tertiary': (255, 255, 255)   # White
    },
    'San Francisco 49ers': {
        'primary': (170, 0, 0),       # Scarlet Red
        'secondary': (75, 146, 219),  # Gold
        'tertiary': (255, 255, 255)   # White
    },
    'Seattle Seahawks': {
        'primary': (0, 34, 68),       # College Navy
        'secondary': (75, 146, 219),  # Action Green
        'tertiary': (163, 177, 178)   # Wolf Gray
    },
    'Tampa Bay Buccaneers': {
        'primary': (213, 10, 10),     # Bay Red
        'secondary': (10, 54, 108),   # Pewter
        'tertiary': (0, 0, 0)         # Black
    },
    'Tennessee Titans': {
        'primary': (12, 35, 64),      # Navy Blue
        'secondary': (0, 0, 0),       # Titans Blue
        'tertiary': (162, 170, 173)   # White
    },
    'Washington Commanders': {
        'primary': (19, 37, 94),      # Dark Burgundy
        'secondary': (255, 184, 28),  # Buff Gold
        'tertiary': (255, 255, 255)   # White
    }
}
