from BaseClass.BaseClass import baseClass
from Locators.SearchLocator import search


class SearchHotel():

    def searchHotel(self):
        b = baseClass()
        self.driver = b.chromeLaunch()
        b.urlLaunch("https://adactinhotelapp.com/")
        b.impWait(10)
        l = search(self.driver)
        b.sendKeys(l.getTxtuser(), "Ashwin07")
        b.dyWait(3)


s = SearchHotel()
s.searchHotel()
