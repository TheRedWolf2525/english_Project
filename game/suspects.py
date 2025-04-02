import random

# Listes de caractéristiques des suspects
FIRST_NAMES = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Eve",
    "Frank",
    "Grace",
    "Hank",
    "Ivy",
    "Jack",
    "Karen",
    "Leo",
    "Mike",
    "Nate",
    "Olivia",
]
LAST_NAMES = [
    "Smith",
    "Johnson",
    "Brown",
    "Williams",
    "Jones",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Oxlong",
]
AGES = list(range(18, 30))
YEARS = ["1st year", "2nd year", "3rd year", "Master", "PhD"]
SPECIALIZATIONS = [
    "Cybersecurity",
    "AI",
    "Development",
    "Networks",
    "Data Science",
    "Embedded Systems",
]
PERSONALITIES = [
    "Introvert",
    "Extravert",
    "Calm",
    "Nervous",
    "Skeptical",
    "Friendly",
    "Secretive",
]
CLUBS = [
    "AI Club",
    "Robotics",
    "Gaming Club",
    "BDE",
    "Photography Club",
    "Music Club",
    "Sports Club",
]
FAVORITE_SUBJECTS = [
    "Programming",
    "Maths",
    "Networks",
    "Security",
    "Machine Learning",
    "Algorithms",
    "Cryptography",
]
FAVORITE_LANGUAGES = [
    "Python",
    "C++",
    "Java",
    "Rust",
    "Go",
    "JavaScript",
    "Swift",
    "Haskell",
]
FAVORITE_EDITORS = [
    "VS Code",
    "IntelliJ",
    "Vim",
    "Emacs",
    "Sublime Text",
    "Eclipse",
    "Atom",
]
DEVICES = ["Windows PC", "MacBook", "Linux ThinkPad", "Custom-built PC", "iPad Pro"]
FAVORITE_FOODS = ["Pizza", "Ramen", "Burger", "Sushi", "Tacos", "Pasta", "Salad"]
FAVORITE_DRINKS = ["Coffee", "Energy Drink", "Tea", "Soda", "Juice", "Milkshake"]
FAVORITE_MUSIC = ["Rock", "Rap", "Electronic", "Jazz", "Classical", "Pop", "Metal"]
FAVORITE_GAMES = [
    "LoL",
    "CS:GO",
    "Minecraft",
    "Dark Souls",
    "Valorant",
    "The Witcher",
    "Elden Ring",
]
FAVORITE_ACTIVITIES = [
    "Sports",
    "Drawing",
    "Music",
    "Reading",
    "Hiking",
    "Dancing",
    "Photography",
]
SOCIAL_MEDIA = ["Twitter/X", "Discord", "Mastodon", "Reddit", "Instagram", "LinkedIn"]
FREQUENT_LOCATIONS = [
    "Library",
    "Gaming Room",
    "Hackerspace",
    "Cafeteria",
    "Dormitory",
    "Lecture Hall",
]
SLEEP_CYCLES = ["Early Bird", "Night Owl", "Insomniac", "Sleeps Anytime"]
ALIBIS = [
    "Was at home",
    "Was at work",
    "Was with friends",
    "Has no alibi",
    "Was in a meeting",
]
MOTIVES = [
    "Revenge",
    "Got a bad grade",
    "Jealousy",
    "Greed",
    "Self-defense",
    "Blackmail",
    "Accidental",
    "Framed",
]


# Classe qui décrit les suspects
class Suspect:
    def __init__(
        self,
        first_name,
        last_name,
        age,
        year,
        specialization,
        personality,
        club,
        favorite_subject,
        favorite_language,
        favorite_editor,
        device,
        favorite_food,
        favorite_drink,
        favorite_music,
        favorite_game,
        favorite_activity,
        social_media,
        frequent_location,
        sleep_cycle,
        alibi,
        motive,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.specialization = specialization
        self.personality = personality
        self.club = club
        self.favorite_subject = favorite_subject
        self.favorite_language = favorite_language
        self.favorite_editor = favorite_editor
        self.device = device
        self.favorite_food = favorite_food
        self.favorite_drink = favorite_drink
        self.favorite_music = favorite_music
        self.favorite_game = favorite_game
        self.favorite_activity = favorite_activity
        self.social_media = social_media
        self.frequent_location = frequent_location
        self.sleep_cycle = sleep_cycle
        self.alibi = alibi
        self.motive = motive

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Alibi: {self.alibi}, Motive: {self.motive})"


class SuspectManager:
    def __init__(self):
        self.suspects = []

    def generate_suspects(self, count=5):
        for _ in range(count):
            suspect = Suspect(
                first_name=random.choice(FIRST_NAMES),
                last_name=random.choice(LAST_NAMES),
                age=random.choice(AGES),
                year=random.choice(YEARS),
                specialization=random.choice(SPECIALIZATIONS),
                personality=random.choice(PERSONALITIES),
                club=random.choice(CLUBS),
                favorite_subject=random.choice(FAVORITE_SUBJECTS),
                favorite_language=random.choice(FAVORITE_LANGUAGES),
                favorite_editor=random.choice(FAVORITE_EDITORS),
                device=random.choice(DEVICES),
                favorite_food=random.choice(FAVORITE_FOODS),
                favorite_drink=random.choice(FAVORITE_DRINKS),
                favorite_music=random.choice(FAVORITE_MUSIC),
                favorite_game=random.choice(FAVORITE_GAMES),
                favorite_activity=random.choice(FAVORITE_ACTIVITIES),
                social_media=random.choice(SOCIAL_MEDIA),
                frequent_location=random.choice(FREQUENT_LOCATIONS),
                sleep_cycle=random.choice(SLEEP_CYCLES),
                alibi=random.choice(ALIBIS),
                motive=random.choice(MOTIVES),
            )
            self.suspects.append(suspect)

    def get_suspects(self):
        return self.suspects
