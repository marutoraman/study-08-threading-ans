from common.driver import * 


def test_driver():
    driver = Driver(True)
    driver.driver.get("https://www.amazon.co.jp/dp/B06VW79S1L")
    driver.quit()
    
    driver = Driver(False)
    driver.driver.get("https://www.amazon.co.jp/dp/B06VW79S1L")
    driver.quit()
    