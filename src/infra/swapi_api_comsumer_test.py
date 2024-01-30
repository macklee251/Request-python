from .swapi_api_comsumer import Swapi_api_consumer

def test_get_starship():
    swapi_api_consumer = Swapi_api_consumer()
    response = swapi_api_consumer.get_starships(page=1)
    
    print(response)