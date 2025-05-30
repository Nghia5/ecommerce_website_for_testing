# test_load_more_html_change_verbose.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestLoadMoreHTMLChange(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://e-commerce-for-testing.onrender.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_load_more_by_html_change(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        try:
            print("🔍 Đang tìm nút 'Load More'...")
            load_more_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Load More')]")))

            # Lưu nội dung HTML trước khi click
            before_html = driver.page_source
            print("📄 Đã lưu nội dung trang trước khi click Load More.")

            # Click nút Load More
            print("🖱️ Đang click vào nút 'Load More'...")
            driver.execute_script("arguments[0].scrollIntoView(true);", load_more_btn)
            load_more_btn.click()

            # Chờ đến khi nội dung HTML thay đổi
            print("⏳ Đang chờ nội dung trang thay đổi sau khi load thêm...")
            wait.until(lambda d: d.page_source != before_html)

            # Kiểm tra và in thông báo kết quả
            after_html = driver.page_source
            if after_html != before_html:
                print("✅ TEST PASSED: Nội dung trang đã thay đổi sau khi nhấn Load More.")
            else:
                print("❌ TEST FAILED: Nội dung trang không thay đổi.")

        except Exception as e:
            print(f"❌ TEST FAILED: Gặp lỗi khi kiểm tra Load More: {e}")
            raise

if __name__ == "__main__":
    unittest.main()
