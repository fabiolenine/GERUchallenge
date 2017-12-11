import http.client
import json
import random as r

def request_get(concat=""):

    conn = http.client.HTTPSConnection("1c22eh3aj8.execute-api.us-east-1.amazonaws.com")

    headers = {'cache-control': "no-cache", 'Geru': "Fabio Lenine"}

    conn.request("GET", "/challenge/quotes" + concat, headers=headers)

    res = conn.getresponse()
    retorno = res.read()

    return retorno.decode("utf-8")


def get_quotes():
    return json.loads(request_get())

def get_quote(data):
    ccat = "/" + data["value"]

    if (data["value"] == "" or data["value"] == "random"):
        ccat = ""

    retorno = json.loads(request_get(ccat))

    if data["value"] == "random":
        quotes = retorno["quotes"]
        number_random = r.randint(0,len(quotes)-1)
        retorno = {"quote_number": number_random, "quote": quotes[number_random]}

    return retorno
