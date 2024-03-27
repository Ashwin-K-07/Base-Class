from selenium.webdriver.common.by import By

class search():

    def __init__(self,driver):
        self.__txtuser = driver.find_element(By.NAME,"username")
        self.__txtpass = driver.find_element(By.NAME, "password")
        self.__location = driver.find_element(By.NAME, "location")
        self.__hotel = driver.find_element(By.NAME, "hotels")
        self.__room = driver.find_element(By.NAME, "room_type")
        self.__roomsNeed = driver.find_element(By.NAME, "room_nos")
        self.__inDate = driver.find_element(By.NAME, "datepick_in")
        self.__outDate = driver.find_element(By.NAME, "datepick_out")
        self.__adultPerRoom = driver.find_element(By.NAME, "adult_room")
        self.__childPerRoom = driver.find_element(By.NAME, "child_room")
        self.__searchBtn = driver.find_element(By.NAME, "Submit")

    def getTxtuser(self):
        return self.__txtuser

    def getTxpass(self):
        return self.__txtpass

    def getLocation(self):
        return self.__location

    def getHotel(self):
        return self.__hotel

    def getRoom(self):
        return self.__room

    def getRoomsNeed(self):
        return self.__roomsNeed

    def getInDate(self):
        return self.__inDate

    def getOutDate(self):
        return self.__outDate

    def getAdultPerRoom(self):
        return self.__adultPerRoom

    def getChildPerRoom(self):
        return self.__childPerRoom

    def getSearch(self):
        return self.__searchBtn
