import requests

url = input("Digite o nome do site")

if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

response = requests.get(url)

if response.status_code == 200:
    print("o site está funcionando corretamente!")
else:
    print("Houve um problema com o site, COD", response.status_code)