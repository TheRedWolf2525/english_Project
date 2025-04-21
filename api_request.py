import google.generativeai as genai


# Lire la clé API
with open('API_KEY.txt', 'r') as f:
    API_KEY = f.read().strip()

# Configurer l'API
genai.configure(api_key=API_KEY)

# Générer une réponse avec le modèle Gemini
model = genai.GenerativeModel("gemini-2.0-flash")

def request(Name, coopLvl, facts, question):
    #copoLvl imdique le niveau de coopération du suspect : 0 = Meurtrier -> 2 = Très coopératif
    if (coopLvl == 0):
        coopromt = "You are the murderer. You won't admit it but you are willing to cooperate not to raise suspitions"
    elif (coopLvl == 1):
        coopromt = "You are innocent. You are not very cooperative, and will distribute clues only if explicitely asked"
    else:
        coopromt = "You are innocent and willing to coopérate. "

    promtp = "Your name is "+Name+". You are being interrogated in connection with the murder of Mr. Koro. "+coopromt+ " "\
    "You hold the following facts, which you may reveal only if asked in English: " +str(facts)+ " "\

    "If you reveal a fact, you must end your sentence with the index of the revealed clue in square brackets."
    "If multiple clues are revealed in one response, include all their indices in order, separated by commas (e.g., [1,3])."
    "Never volunteer information — only respond based on what you're asked."
    "The policeman says: " +question
    return model.generate_content(promtp)


print(request("Maggie Mag", 1, ["you were at home last night"], "What'up ma'am"))

