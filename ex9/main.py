import json

if __name__ == "__main__":
    fdile = open("car_config.json")
    something = json.load(fdile)
    print(something)