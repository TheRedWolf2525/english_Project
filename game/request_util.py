import json
import urllib.request

def request_from_gemini(name, coop_prompt, facts, question):
    url = "http://127.0.0.1:5000/ask"
    headers = {"Content-Type": "application/json"}

    payload = {
        "name": name,
        "coop_prompt": coop_prompt,
        "facts": facts,
        "question": question
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            return result.get("response", "No response.")
    except Exception as e:
        return f"Error: {str(e)}"
