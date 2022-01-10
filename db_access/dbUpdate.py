from dbConnection import *

rootPath = "/home/steam/assetto/"
carPath = rootPath + "content/cars/"
trackPath = rootPath + "content/tracks/"
confPath = rootPath + "cfg/"

def updateCarTable(myDB):
    carPathList = next(os.walk(carPath))[1]

    for carP in carPathList:
        uiCarPath = carPath + carP + "/ui/ui_car.json"
         
        if not os.path.exists(uiCarPath):
            continue

        #get skin list
        skinCarPath = carPath + carP + "/skins/"
        if not os.path.exists(skinCarPath):
            print("This car has UI but no skins " + carP)
            continue #DLC CAR
        carSkins = next(os.walk(skinCarPath))[1]

        with open(uiCarPath, encoding="UTF-8") as json_file:
            json_data = json.load(json_file, strict=False)
            brand = json_data['brand']
            model = json_data['name']
            try:
                powerF = filter(str.isdigit, json_data['specs']['bhp'])
                power = int("".join(powerF))
            except:
                print("No power: " + model)
                power = 0
            try:
                weightF = filter(str.isdigit, json_data['specs']['weight'])
                weight = int("".join(weightF))
            except:
                print("No weight: " + model)
                weight = 0
            try: 
                country = json_data['country']
            except:
                print("No country: " + model)
                country = "None"
            try:
                year = int(json_data['year'])
            except:
                print("No year: " + model)
                year = 0
            path = str(carPath + carP)
        
        #add to table
        cursor = myDB.cursor()
        query = """REPLACE into car (brand, model, skins, power, weight, country, year, path) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (brand, model, str(carSkins), power, weight, country, year, path)
        cursor.execute(query, val)
        myDB.commit()



#def createTrackTable():


#def updateAll():
    #def createTrackTable()
    #def createServerTable()
    #def createCarListTable()
    #def createCarListJoinTable()

updateCarTable(connectDB())