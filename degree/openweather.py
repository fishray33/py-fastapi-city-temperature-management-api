import httpx


API_KEY = "432fe9e768469ec38b71d2f20145ab01"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


async def get_temperature(city: str) -> float | str | Exception:
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["main"]["temp"]
        else:
            return f"Can't fetch temperature for '{city}'"
