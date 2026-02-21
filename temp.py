import requests

apikey = "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"

word = input("Enter your word:")

res = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

print("status code:",res.status_code)

if res.status_code ==200:
    meanings = res.json()[0]["meanings"]
    for meaning in meanings:
        defn = meaning["definitions"]
        for d in defn:
            print(d["definition"])

else:
    print("word not found in dictionary")
