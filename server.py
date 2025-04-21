import google.generativeai as genai
from flask import Flask, request, jsonify


# Lire la clé API
with open("API_KEY.txt") as f:
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def requester(name, coopLvl, facts, question):
    #copoLvl imdique le niveau de coopération du suspect : 0 = Meurtrier -> 2 = Très coopératif
    if (coopLvl == 0):
        coopromt = "You are the murderer. You won't admit it but you are willing to cooperate not to raise suspitions"
    elif (coopLvl == 1):
        coopromt = "You are innocent. You are not very cooperative, and will distribute clues only if explicitely asked"
    else:
        coopromt = "You are innocent and willing to cooperate. "

    promtp = (
    f"Your name is {name}. You are being interrogated in connection with the murder of Mr. Koro. {coopromt}"
    f"You should reply only if you are spoken to in correct english. Else fain incomprehension"
    f"You hold the following facts: {facts} "
    f"If you reveal a fact, you must end your sentence with the index of the revealed clue in square brackets (it must be after everything else, even ponctuation). "
    f"If multiple clues are revealed in one response, include all their indices in order, separated by commas (e.g., [0,3]). "
    f"Never volunteer information — only respond based on what you're asked. "
    f"The policeman says: {question}" )

    return model.generate_content(promtp)


app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()

    name = data.get("name", "Unknown")
    coop_prompt = data.get("coop_prompt", "")
    facts = data.get("facts", [])
    question = data.get("question", "")

    try:
        response = requester(name, coop_prompt, facts, question)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
