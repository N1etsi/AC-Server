import os
import json

#Directory definition
rootPath = "/home/steam/assetto/"
carPath = rootPath + "content/cars/"
trackPath = rootPath + "content/tracks/"
confPath = rootPath + "cfg/"


def listCars():
    carList = []
    carPathList = next(os.walk(carPath))[1]

    for carP in carPathList:
        uiCarPath = carPath + carP + "/ui/ui_car.json"
         
        if not os.path.exists(uiCarPath):
            continue

        with open(uiCarPath, encoding="UTF-8") as json_file:
            json_data = json.load(json_file, strict=False)
            carList.append(json_data['name'])

def listCarSkins():
    carPathList = next(os.walk(carPath))[1]

    for carP in carPathList:
        SkinCarPath = carPath + carP + "/skins/"
        print(carP)
         
        if not os.path.exists(SkinCarPath):
            continue #DLC CAR

        carSkins = next(os.walk(SkinCarPath))[1]

        
        print(carSkins)

        

def listTracks():
    trackList = []
    trackPathList = next(os.walk(trackPath))[1]

    for trackP in trackPathList:
        uiTrackPath = trackPath + trackP + "/ui/ui_track.json"

        if trackP[0] == ".":
            continue
         
        if not os.path.exists(uiTrackPath):
            #Check for layouts
            layoutsPathList = next(os.walk(trackPath + trackP + "/ui/"))[1]
            
            for layoutP in layoutsPathList:
                uiLayoutPath = trackPath + trackP + "/ui/" + layoutP + "/ui_track.json"

                if layoutP[0] == ".":
                    continue

                if not os.path.exists(uiLayoutPath):
                    continue
                
                with open(uiLayoutPath, encoding="utf-8-sig") as json_file:
                    json_data = json.load(json_file, strict=False)
                    trackList.append(json_data['name'])


            continue

        with open(uiTrackPath, encoding="utf-8-sig") as json_file:
            json_data = json.load(json_file, strict=False)
            trackList.append(json_data['name'])

    for name in trackList:
        print(name)





listCarSkins()