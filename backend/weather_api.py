import requests

def weather(location):

    try:
        url=f"https://wttr.in/{location}?format=j1"
        r=requests.get(url)
        data=r.json()
        rain=data["current_condition"][0]["precipMM"]

        if float(rain) > 5:
            return "Heavy Rainfall Risk"
        else:
            return "Moderate Weather Risk"

    except:
        return "Weather API unavailable"
