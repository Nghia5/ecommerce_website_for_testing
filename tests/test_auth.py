import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://e-commerce-for-testing.onrender.com"

class AuthTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def go_to_signin(self):
        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()

    def test_login_success(self):
        self.go_to_signin()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("superadmin@gmail.com")

        self.driver.find_element(By.NAME, "password").send_keys("admin123")

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Sign In')]")
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("/"))
        self.assertIn("", self.driver.current_url)

    def test_login_wrong_password(self):
        self.go_to_signin()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("superadmin@gmail.com")

        self.driver.find_element(By.NAME, "password").send_keys("wrongpassword")

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Sign In')]")
        login_button.click()

        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__desc"))
        )
        self.assertIn("Invalid credentials", error.text)

    def test_login_wrong_email(self):
        self.go_to_signin()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("wrong@email.com")

        self.driver.find_element(By.NAME, "password").send_keys("admin123")

        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Sign In')]")
        login_button.click()

        error = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__desc"))
        )
        self.assertIn("Invalid credentials", error.text)

    def test_register_success(self):
        self.driver.get(BASE_URL)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("abc123@gmail.com")

        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.NAME, "passwordConfirm").send_keys("admin123")

        self.driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("/signin"))
        self.assertIn("/signin", self.driver.current_url)
    
    def test_register_with_admin_account(self):
        self.driver.get(BASE_URL)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "email"))
        ).send_keys("superadmin@gmail.com")

        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.NAME, "passwordConfirm").send_keys("admin123")

        self.driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("/signin"))
        self.assertIn("/signin", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
