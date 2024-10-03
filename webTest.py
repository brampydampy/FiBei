from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#set-wait-time
WAIT = 5

driver = webdriver.Chrome()
driver.maximize_window() #maximize the chrome window

#driver.minimize_window() #minimize the chrome window

time.sleep(2)
#openFibeiGreetingsWebsite
driver.get("https://fibeigreetings.com")
time.sleep(WAIT)

#Navigate to 'Gifts Page'
#click-gifts page
driver.find_element(By.XPATH,"//a[@href='/gifts']").click()
time.sleep(WAIT)
print('gifts page test done')

#scrolldowntoHygiene
hygiene=driver.find_element(By.XPATH,"//div[@class='row']//div[1]//app-gift-event[1]//div[1]//div[1]//img[1]")
driver.execute_script("arguments[0].scrollIntoView();",hygiene)
time.sleep(3)

#click-HygienicKits
driver.find_element(By.XPATH,"//div[@class='row']//div[1]//app-gift-event[1]//div[1]//div[1]//img[1]").click()
time.sleep(WAIT)
print('hygienic kits page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click() #back to all categories
time.sleep(WAIT)

#click-Flowers
driver.find_element(By.XPATH,"//div[2]//app-gift-event[1]//div[1]//div[1]//img[1]").click()
time.sleep(WAIT)
print('flowers page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[normalize-space()='Back to All Categories']").click()#back to all categories
time.sleep(WAIT)

#click-BathAndBody
driver.find_element(By.XPATH,"//div[3]//app-gift-event[1]//div[1]//div[1]//img[1]").click()
time.sleep(WAIT)
print('bnb page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#click-StuffedToys
driver.find_element(By.XPATH,"//div[4]//app-gift-event[1]//div[1]//div[1]//img[1]").click()
time.sleep(WAIT)
print('stuffed toys page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#scrolldowntoMugs
mugs=driver.find_element(By.XPATH,"//div[5]//app-gift-event[1]//div[1]//div[1]//img[1]")
driver.execute_script("arguments[0].scrollIntoView();",mugs)
time.sleep(3)

#click-MugsAndTeacups
driver.find_element(By.XPATH,"//div[5]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('mugs and teacups page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#click-FruitBaskets
driver.find_element(By.XPATH,"//div[6]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('fruit baskets page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#click-ComputersAndPeripherals
driver.find_element(By.XPATH,"//div[7]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('computer and peripherals page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#click-CandlesAndFragrances
driver.find_element(By.XPATH,"//div[8]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('candles and fragrances page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#scrolldowntoGiftSet
giftset=driver.find_element(By.XPATH,"//div[9]//app-gift-event[1]//div[1]//div[1]//img[1]")
driver.execute_script("arguments[0].scrollIntoView();",giftset)
time.sleep(3)

#click-GiftSet
driver.find_element(By.XPATH,"//div[9]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('gift set page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#click-PictureFrame
driver.find_element(By.XPATH,"//div[10]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('picture frame page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)

#click-CandiesAndCookies
driver.find_element(By.XPATH,"//div[11]//app-gift-event[1]//div[1]//div[1]//img[1]").click()#back to all categories
time.sleep(WAIT)
print('candies and cookies page test done')

#click-BackToAllCategories
driver.find_element(By.XPATH,"//button[@class='btn rounded-0']").click()#back to all categories
time.sleep(WAIT)


###########################CART-PAGE-FOOT-NOTES###########################
#click-CartPage
driver.find_element(By.XPATH,"//i[@class='fa fa-shopping-cart']").click()#back to all categories
time.sleep(WAIT)
print('cart page test done')

#scrollToContactUs
contact=driver.find_element(By.XPATH,"//app-carts[@class='ion-page']//a[normalize-space()='Contact Us']")
driver.execute_script("arguments[0].scrollIntoView();",contact)
time.sleep(3)

#click-ContactUsHyperlink
driver.find_element(By.XPATH,"//app-carts[@class='ion-page']//a[normalize-space()='Contact Us']").click()#back to all categories
time.sleep(WAIT)
print('contact us page test done')

#scrollToChatNow
chat=driver.find_element(By.CSS_SELECTOR,"app-page[class='ion-page'] div[class='row mt-5'] div:nth-child(1) div:nth-child(2) a:nth-child(1)")
driver.execute_script("arguments[0].scrollIntoView();",chat)
time.sleep(3)

#click-ChatNowHyperlink
driver.find_element(By.CSS_SELECTOR,"app-page[class='ion-page'] div[class='row mt-5'] div:nth-child(1) div:nth-child(2) a:nth-child(1)").click()#back to all categories
time.sleep(WAIT)
print('chat now page test done')

#scrollToReview
review=driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Review Product']")
driver.execute_script("arguments[0].scrollIntoView();",review)
time.sleep(3)

#click-ReviewProductHyperlink
driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Review Product']").click()#back to all categories
time.sleep(WAIT)
print('review page test done')

#scrollToAbout
about=driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='About FibeiGreetings']")
driver.execute_script("arguments[0].scrollIntoView();",about)
time.sleep(3)

#click-AboutFibeiHyperlink
driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='About FibeiGreetings']").click()#back to all categories
time.sleep(WAIT)
print('about page test done')

#scrollToPress
press=driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Press Page']")
driver.execute_script("arguments[0].scrollIntoView();",press)
time.sleep(3)

#click-PressPageHyperlink
driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Press Page']").click()#back to all categories
time.sleep(WAIT)
print('press page test done')

#scrollToSign
sign=driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Sign And Send']")
driver.execute_script("arguments[0].scrollIntoView();",sign)
time.sleep(3)

#click-SignAndSendHyperlink
driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Sign And Send']").click()#back to all categories
time.sleep(WAIT)
print('sns page test done')

#scrollToShip
ship=driver.find_element(By.XPATH,"//app-sign-and-send-page[@class='ion-page']//a[normalize-space()='Shipping and Delivery']")
driver.execute_script("arguments[0].scrollIntoView();",ship)
time.sleep(3)

#click-ShippingAndDeliveryHyperlink
driver.find_element(By.XPATH,"//app-sign-and-send-page[@class='ion-page']//a[normalize-space()='Shipping and Delivery']").click()#back to all categories
time.sleep(WAIT)
print('snd page test done')

#scrollToTerms
terms=driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Terms and Conditions']")
driver.execute_script("arguments[0].scrollIntoView();",terms)
time.sleep(3)

#click-TermsAndConditionsHyperlink
driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Terms and Conditions']").click()#back to all categories
time.sleep(WAIT)
print('t&c page test done')

#scrollToPrivacy
privacy=driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Privacy Policy']")
driver.execute_script("arguments[0].scrollIntoView();",privacy)
time.sleep(3)

#click-PrivacyPolicyHyperlink
driver.find_element(By.XPATH,"//app-page[@class='ion-page']//a[normalize-space()='Privacy Policy']").click()#back to all categories
time.sleep(WAIT)
print('privacy and policy page test done')

print('No Errors in the Web Page')
print('Testing Complete')



time.sleep(2)
driver.quit()





