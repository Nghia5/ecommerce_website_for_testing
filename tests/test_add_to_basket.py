import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://e-commerce-for-testing.onrender.com"

class TestAddToBasket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def login(self, email, password):
        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        login_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_btn.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys(email)

        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
        # Khi đăng nhập, trang web sẽ chuyển hướng sang trang /
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Products"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chakra-card"))
        )

    def test_require_login_to_add_to_basket(self):
        self.driver.get(BASE_URL)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chakra-card"))
        )

        try:
            add_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to Basket')]"))
            )
            add_btn.click()

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            self.assertIn("/signin", self.driver.current_url)
        except:
            self.driver.save_screenshot("error_login_redirect.png")
            raise AssertionError("Không bị chuyển hướng sang đăng nhập khi chưa đăng nhập.")

    def test_add_to_basket_when_logged_in(self):
        self.login("superadmin@gmail.com", "admin123")

        try:
            add_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//button[contains(text(), 'Add to Basket')]"))
            )
            add_buttons[0].click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Remove from Basket')]"))
            )
        except:
            self.driver.save_screenshot("error_add_after_login.png")
            raise AssertionError("Không thêm được sản phẩm sau khi đăng nhập.")

# 👉 Tuỳ chỉnh kết quả test để in PASS/FAIL
class VerboseTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"✅ PASS: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"❌ FAIL: {test}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"💥 ERROR: {test}")

class VerboseTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return VerboseTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == "__main__":
    unittest.main(testRunner=VerboseTestRunner(), verbosity=2)
