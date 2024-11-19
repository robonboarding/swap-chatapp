from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Set up the Key Vault client
key_vault_name = "open-ai-keys-rob"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

# Retrieve the OpenAI API key from Key Vault
api_key_secret_name = "open-ai-resource-rob"
api_key = secret_client.get_secret(api_key_secret_name).value


import openai



from openai import AzureOpenAI



client = AzureOpenAI(azure_endpoint="https://open-ai-resource-rob.openai.azure.com/",
        api_version="2024-08-01-preview",api_key=api_key )


deployment_name='gpt-4o-mini'
msg=" who are you?"
print('Sending a text completion job')
message = [{"role":"system","content":str(msg)}]
print(str(message))
response = client.chat.completions.create(model=deployment_name, messages=message)
print(response.choices[0].message.content.strip())
    #  response.choices[0].message.content.strip()




