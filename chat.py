import requests, json, security

messages = {
        "max_tokens": 8,
        "messages": [
            {"role": "system", "content": "Você é um assistente virtual de chats. Responda o usuário em seu respectivo idioma."}
        ]
}

def generate(message:str, context:dict, model:str = "@cf/meta/llama-3-8b-instruct") -> str:
    url = f"https://api.cloudflare.com/client/v4/accounts/{security.account_id}/ai/run/{model}"
    headers = {
        "Authorization": security.token
    }
    context
    
    rJson = requests.post(url=url, headers=headers, json=context)