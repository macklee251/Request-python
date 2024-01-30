import requests
 
class Swapi_api_consumer:
    
    @classmethod
    def get_starships(self, page: int) -> any:
        params = {'page':page}
        response  = requests.get('https://swapi.dev/api/starships/', params=params)
        return response.json()
     
    def __init__(self) -> None:
        pass
    