import google.generativeai as genai


# Lire la clé API
with open('API_KEY.txt', 'r') as f:
    API_KEY = f.read().strip()

# Configurer l'API
genai.configure(api_key=API_KEY)

# Générer une réponse avec le modèle Gemini
model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content(
    "Récite la tirade du nez de cyrano de bergerac (telle que dite par gérard depardieu dans le film). ne dis rien d'autre"
)

print(response.text)

