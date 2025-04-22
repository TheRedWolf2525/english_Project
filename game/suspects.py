import random
from itertools import combinations
# Assign genders and split first names accordingly
GENDERS = ["Male", "Female"]

MALE_FIRST_NAMES = [
    "Bob",
    "Charlie",
    "Frank",
    "Hank",
    "Jack",
    "Leo",
    "Mike",
    "Nate",
    "Ben"
]

FEMALE_FIRST_NAMES = [
    "Alice",
    "Diana",
    "Eve",
    "Grace",
    "Ivy",
    "Karen",
    "Olivia",
]

LAST_NAMES = [
    "Smith",
    "Dover",
    "Hawk",
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
DEVICES = ["Windows PC", "MacBook", "Linux ThinkPad", "Custom-built PC", "iPad Pro"]
FAVORITE_FOODS = ["Pizza", "Ramen", "Burger", "Sushi", "Tacos", "Pasta", "Salad"]
FAVORITE_DRINKS = ["Coffee", "Energy Drink", "Tea", "Soda", "Juice", "Milkshake"]
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
ALIBIS = [
    "Was at home",
    "Was at work",
    "Was with friends",
    "Has no alibi",
    "Was in a meeting",
]


# Classe qui décrit les suspects
class Suspect:
    def __init__(
        self,
        id,
        first_name,
        last_name,
        age,
        year,
        personality,
        club,
        favorite_subject,
        device,
        favorite_food,
        favorite_drink,
        favorite_activity,
        social_media,
        frequent_location,
        alibi,
        picture_label,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.year = year
        self.personality = personality
        self.club = club
        self.favorite_subject = favorite_subject
        self.device = device
        self.favorite_food = favorite_food
        self.favorite_drink = favorite_drink
        self.favorite_activity = favorite_activity
        self.social_media = social_media
        self.frequent_location = frequent_location
        self.alibi = alibi
        self.picture_label = picture_label

        self.coop = random.randint(0, 1)
        self.exchanges = [""]*5

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Alibi: {self.alibi})"

    def getName(self):
        return f"{self.first_name} {self.last_name}"

    def getPicture(self, expression):
        return f"{self.picture_label} {expression}"
    
    def add_entry(self, newEntry):
        self.exchanges.pop(0)
        self.exchanges.append(newEntry)
    
    def get_attributes(self):
        return {
            "age": self.age,
            "year": self.year,
            "personality": self.personality,
            "club": self.club,
            "favorite_subject": self.favorite_subject,
            "device": self.device,
            "favorite_food": self.favorite_food,
            "favorite_drink": self.favorite_drink,
            "favorite_activity": self.favorite_activity,
            "social_media": self.social_media,
            "frequent_location": self.frequent_location,
            "alibi": self.alibi,
        }


class SuspectManager:
    def __init__(self):
        self.suspects = []

    def __eq__(self, other):
        return isinstance(other, SuspectManager) and self.suspects == other.suspects
        
    def __ne__(self, other):
        return not self.__eq__(other)

    def generate_suspects(self, count=5):
        used_first_names = set()
        used_last_names = set()

        girls_count = 1
        boys_count = 1

        for id in range(count):
            gender = random.choice(GENDERS)
            if gender == "Male":
                first_name = random.choice(MALE_FIRST_NAMES)
            else:
                first_name = random.choice(FEMALE_FIRST_NAMES)
            # WARNING: Infinte loop if not enough names
            while first_name in used_first_names:
                if gender == "Male":
                    first_name = random.choice(MALE_FIRST_NAMES)
                else:
                    first_name = random.choice(FEMALE_FIRST_NAMES)
            used_first_names.add(first_name)

            last_name = random.choice(LAST_NAMES)
            while last_name in used_last_names:
                last_name = random.choice(LAST_NAMES)
            used_last_names.add(last_name)

            if gender == "Male":
                picture_label = "male " + str(boys_count)
                boys_count += 1
            elif gender == "Female":
                picture_label = "female " + str(girls_count)
                girls_count += 1

            suspect = Suspect(
                id=id,
                first_name=first_name,
                last_name=last_name,
                age=random.choice(AGES),
                year=random.choice(YEARS),
                personality=random.choice(PERSONALITIES),
                club=random.choice(CLUBS),
                favorite_subject=random.choice(FAVORITE_SUBJECTS),
                device=random.choice(DEVICES),
                favorite_food=random.choice(FAVORITE_FOODS),
                favorite_drink=random.choice(FAVORITE_DRINKS),
                favorite_activity=random.choice(FAVORITE_ACTIVITIES),
                social_media=random.choice(SOCIAL_MEDIA),
                frequent_location=random.choice(FREQUENT_LOCATIONS),
                alibi=random.choice(ALIBIS),
                picture_label=picture_label,
            
            )
            self.suspects.append(suspect)

    def get_suspects(self):
        return self.suspects
    
    def get_suspect_by_id(self, id):
        for s in self.suspects:
            if s.id == id:
                return s

    def validate_unique_murderer(self, murderer_id, indices_count=6):
        murderer = self.get_suspect_by_id(murderer_id)
        murderer_attrs = murderer.get_attributes()

        all_keys = list(murderer_attrs.keys())
        combos = list(combinations(all_keys, indices_count))

        for combo in combos:
            murderer_signature = tuple(murderer_attrs[k] for k in combo)

            match_count = 0
            for suspect in self.suspects:
                suspect_attrs = suspect.get_attributes()
                signature = tuple(suspect_attrs[k] for k in combo)
                if signature == murderer_signature:
                    match_count += 1
                if match_count > 1:
                    return False  # Une autre personne partage cette combinaison

        return True
    
    def generate_valid_suspects(self, count=5, max_attempts=1000):
        attempts = 0
        while attempts < max_attempts:
            self.suspects = []
            self.generate_suspects(count)

            for i in range(count):
                if self.validate_unique_murderer(murderer_id=i):
                    print(f"Suspect {i} can be a valid murderer.")
                    return i  # On retourne l'ID du coupable choisi

            attempts += 1

        raise Exception("Impossible de générer des suspects valides après plusieurs tentatives.")
    
    def find_unique_signature_combination(self, murderer_id, indices_count=6):

        murderer = self.get_suspect_by_id(murderer_id)
        murderer_attrs = murderer.get_attributes()
        keys = list(murderer_attrs.keys())

        for combo in combinations(keys, indices_count):
            murderer_signature = tuple(murderer_attrs[k] for k in combo)

            match_count = sum(
                1 for suspect in self.suspects
                if tuple(suspect.get_attributes()[k] for k in combo) == murderer_signature
            )
            if match_count == 1:
                return list(combo)  # Signature unique trouvée

        return None  # Aucun combo unique trouvé


