import time
import keyboard
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class baseClass():

    # Chrome Launch
    def chromeLaunch(self):
        self.driver = webdriver.Chrome()
        return self.driver

    # Edge Launch
    def edgeLaunch(self):
        self.driver = webdriver.Edge()
        return self.driver

    # URL Launch
    def urlLaunch(self,url):
        self.driver.get(url)

    # Imp Wait & Max Window
    def impWait(self,sec):
        self.driver.maximize_window()
        self.driver.implicitly_wait(sec)

    # Dynamic Wait
    def dyWait(self,sec):
        time.sleep(sec)

    # Send Keys
    def sendKeys(self,e,data):
        e.send_keys(data)

    # Get Current Url
    def getUrl(self):
        url = self.driver.current_url
        return url

    # Quit Browser
    def quit(self):
        self.driver.quit()

    # Move to element
    def moveToElement(self,dest):
        a = ActionChains(self.driver)
        a.move_to_element(dest).perform()

    # Click
    def actClick(self,e):
        a = ActionChains(self.driver)
        a.click(e).perform()

    # Double Click
    def doubleClick(self,e):
        a = ActionChains(self.driver)
        a.double_click(e).perform()

    # Right Click
    def rightClick(self,e):
        a = ActionChains(self.driver)
        a.context_click(e).perform()

    # Drag and Drop
    def dragAndDrop(self,source,target):
        a = ActionChains(self.driver)
        a.drag_and_drop(source,target).perform()

    # Click and Hold---> Move To---> Release
    def clickMoveRelease(self,source,target):
        a = ActionChains(self.driver)
        a.click_and_hold(source).move_to_element(target).release().perform()

    # Click and Hold ----> Release
    def clickAndRelease(self,source,target):
        a = ActionChains(self.driver)
        a.click_and_hold(source).release(target).perform()

    # Keyboard Class
    def keyboard(self,keys):
        keyboard.press(keys)
        keyboard.release(keys)

    # Simple Alert
    def simpleAlert(self):
        b = self.driver.switch_to.alert
        b.accept()

    # Confirm Alert
    def confirmAlert(self):
        b = self.driver.switch_to.alert
        b.accept()
        b.dismiss()

    # Prompt Alert
    def promptAlert(self):
        b = self.driver.switch_to.alert
        b.accept()
        b.dismiss()

    # Drop Down
    def dropDown(self,e):
        s = Select(e)
        return s

    # Select By Index
    def selectByIndex(self,e,index):
        s = Select(e)
        s.select_by_index(index)

    # Select By Value
    def selectByValue(self,e,value):
        s = Select(e)
        s.select_by_value(value)

    # Select By Visible Text
    def selectByVisibleText(self,e,text):
        s = Select(e)
        s.select_by_visible_text(text)

    # Deselect By Index
    def deselectByIndex(self,e,index):
        s = Select(e)
        s.deselect_by_index(index)

    # Deselect By Value
    def deselectByValue(self,e,value):
        s = Select(e)
        s.deselect_by_value(value)

    # Deselect By Visible Text
    def deselectByVisibleText(self,e,text):
        s = Select(e)
        s.deselect_by_visible_text(text)

    # Deselect All
    def deselectAll(self,e):
        s = Select(e)
        s.deselect_all()

    # Frames
    def switchIntoFrame(self,id):
        self.driver.switch_to.frame(id)

    def switchToDefault(self):
        self.driver.switch_to.default_content()

    def switchToParentFrame(self):
        self.driver.switch_to.parent_frame()

    # Navigation
    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    # Is Displayed
    def isDisplayed(self,e):
        d = e.is_displayed()
        return d

    # Is Enabled
    def isEnabled(self,e):
        d = e.is_enabled()
        return d

    # Is Selected
    def isSelected(self,e):
        d = e.is_selected()
        return d




