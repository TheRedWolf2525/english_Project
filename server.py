import google.generativeai as genai
from flask import Flask, request, jsonify


# Lire la clé API
with open("API_KEY.txt") as f:
    API_KEY = f.read().strip()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def requester(name, coopLvl, facts, question, exchange):
    #copoLvl imdique le niveau de coopération du suspect : 0 = Meurtrier -> 2 = Très coopératif
    if (coopLvl == 0):
        coopromt = "You are not very cooperative, and will distribute clues only if explicitely asked. "
    else:
        coopromt = "You are and willing to cooperate. "

    promtp = (
    f"Your name is {name}. You are being interrogated in connection with the murder of your teacher Mr. Koro. {coopromt}"
    f"You should always deny being the muurderer. "
    f"You should reply only if you are spoken to in correct enough english. Else feign incomprehension. All your answers must be in english. "
    f"You hold the following facts: {facts}. You must act accordingly. "
    f"Here are your last exchanges (empty at the beginning): {exchange}"
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
    exchanges = data.get("exchanges", [])
    question = data.get("question", "")

    try:
        response = requester(name, coop_prompt, facts, question, exchanges)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
