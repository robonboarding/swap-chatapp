from flask import Flask, request, jsonify
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


# Set up the Key Vault client
key_vault_name = "open-ai-keys-rob"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

# Retrieve the OpenAI API key from Key Vault
api_key_secret_name ="open-ai-resource-rob"
api_key = secret_client.get_secret(api_key_secret_name).value


print(api_key)


from openai import AzureOpenAI
def getResponse( msg="who are you?"):
    client = AzureOpenAI(azure_endpoint="https://open-ai-resource-rob.openai.azure.com/",
        api_version="2024-08-01-preview",api_key=api_key )


    deployment_name='gpt-4o-mini'
    
    print('Sending a text completion job')
    message = [{"role":"system","content":str(msg)}]
    print(str(message))
    response = client.chat.completions.create(model=deployment_name, messages=message)
    print(response.choices[0].message.content.strip())
        #  response.choices[0].message.content.strip()
    return response.choices[0].message.content.strip()



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    
    # Check if 'question' is in the JSON data
    if not data or 'question' not in data:
        return jsonify({"error": "Please provide a question."}), 400
    
    question = data["question"]
    print(question)
    # Here you could call an LLM model or use a static response for testing
    # For demonstration, we’ll return a simple response
    rsp=getResponse(msg=str(question))
    response = f"You asked: {question}. Answer: {rsp}"
    
    return 

    

if __name__ == "__main__":
    print('running app')
    app.run(debug=True)

