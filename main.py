from file_handler import FileHandler
from utils import change_city_to_latitude_and_longitude
from utils import data_validation
from utils import request_from_weather_api, get_data_from_file


print("Welcome to the app which will let you check if certain day is rainy day or not")

file_handler = FileHandler("weather_data.json")
print(file_handler.data)

address = input("Provide the city in order to check the weather: ")
user_date = input("Provide the date in order to check the weather: ")
city_in_file = get_data_from_file(file_handler.data, address, user_date)
if city_in_file:
    print(city_in_file)
    print("Downloaded data from file")
else:
    latitude, longitude = change_city_to_latitude_and_longitude(address)
    valid_date = data_validation(user_date)
    if_rain = request_from_weather_api(latitude, longitude, valid_date)
    print(if_rain)
    print("Above data has been downloaded from API ")
    file_handler.upload_new_city_to_data(city=address, date=valid_date, result=if_rain)
    file_handler.save_data_to_file()


