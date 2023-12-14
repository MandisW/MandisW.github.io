#gebruik de requests-module om gegevens op te halen van de "JSONPlaceholder" API (https://jsonplaceholder.typicode.com/)
#instructies:
# 1. haal de gegevens op van de API-endpoint /todos/1
# 2. Decodeer de JSON-reactie
# 3. Toon de titel van de taak in de console 

# import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# result = response.json()

# output = result["title"]
# print(output)

# ==================================================================================================

# Breid de vorige oefening uit door de taakstatus ("completed") van de opgehaalde taak te controleren
# instructies:
# 1. als de taak is voltooid, print dan "goed gedaan!" in de console. zo niet,
# print dan "Er moet nog werk worden gedaan."

# import requests

# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(api_url)
# result = response.json()

# output = result["completed"]
# if output == True :
#     print("goed gedaan!")
# else:
#     print("Er moet nog werk worden gedaan.")

# =======================================================================================================

# 1 scrijf een python-script dat de dog api gebruikt om een willekeurige katfoto op te halen
# 2. gebruik de requests module om de afbeelding op te halen en deze lokaal op te slaan of direct weer te geven in je script
# 3. voeg eventueel extra functionaliteit toe, zoals het opslaan van de afbeelding op de schijf of het openen in een webbrowser. (tip module webbrowser)

# import requests
# import webbrowser
# # import os

# api_url = "https://dog.ceo/api/breeds/image/random"
# response = requests.get(api_url)
# result = response.json()
# foto_url = result["message"]

# image_file_path = 'willekeurige_hondenfoto.jpg'

# image_response = requests.get(foto_url)
# with open(image_file_path, 'wb') as image_file:
#     image_file.write(image_response.content)
#     print("De afbeelding is opgeslagen als 'willekeurige_hondenfoto.jpg'")
# webbrowser.open_new(foto_url)

# ================================================================================================================

# maak gebruik van een api die moppen genereert. maak een python script waarin je input van een gebruiker vraagt en vervolgens willekeurige moppen tapt.
# deze moppen verkrijg je via de door jou gekozen api

# def haal_willekeurige_mop():
#     import requests
#     url = "https://moppenbot.nl/api/random/"
#     response = requests.get(url)
#     mop_data = response.json()
#     mop_lijst = mop_data["joke"]
#     mop = mop_lijst["joke"]
#     print (mop)


# while True:
#     input("Druk op Enter om een mop te horen...")
#     haal_willekeurige_mop()
#     doorgaan = input("Wil je nog een mop horen? (ja/nee): ")bido
#     if doorgaan.lower() != "ja":
#         break

# ======================================================================================================

# gebruik een nieuws-api zoals newsapi (https://newsapi.org/) om recent nieuws op te halen en weer te geven op basis van een bepaald trefwoord
# instructies
# 1. vraag de gebruiker om een trefwoor in te voeren (bijv. "technologie", "sport", etc.)
# 2. gebruik de nieuws api om recent nieuws op te halen met betrekking tot het opgegeven trefwoord.
# 3. toon de titels van de nieuwsartikelen in de console

import requests

def haal_recent_nieuws(trefwoord):
    api_key = 'f72470af2e794e6c92903bdfe09b544e' 
    base_url = 'https://newsapi.org/v2/everything'
    
    params = {
        'q': trefwoord,
        'apiKey': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        
        print(f"Recent nieuws over '{trefwoord}':\n")
        for article in articles:
            print(article['title'])
    else:
        print("Fout bij het ophalen van het nieuws.")

def main():
    trefwoord = input("Voer een trefwoord in voor het nieuws: ")
    haal_recent_nieuws(trefwoord)

if __name__ == "__main__":
    main()









































