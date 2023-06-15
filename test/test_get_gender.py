import unittest
from persian_gender_detection.persian_gender_detection import get_gender


class TestCleanName(unittest.TestCase):
    def test_detect_male(self):
        self.assertEqual(get_gender("محمدمسیحا", True), ("MALE", "محمد"))
        self.assertEqual(get_gender("محمدنیسنممدیتیس", True), ("MALE", "محمد"))
        self.assertEqual(get_gender("علي"), "MALE")
        self.assertEqual(get_gender("مسیحا"), "MALE")
        self.assertEqual(get_gender("سعید     "), "MALE")
        self.assertEqual(get_gender("هــــادی"), "MALE")
        self.assertEqual(get_gender("محمد   رضا"), "MALE")
        self.assertEqual(get_gender("احسا   ن"), "MALE")
        self.assertEqual(get_gender("كامران"), "MALE")
        self.assertEqual(get_gender("  پیمـــان  "), "MALE")
        self.assertEqual(get_gender("حســ😎ــن", True), ("MALE", "حسن"))
        self.assertEqual(get_gender("۱۲۳۹۹۳محمدعلی123"), "MALE")
        self.assertEqual(get_gender("<<محمد>>"), "MALE")

    def test_detect_female(self):
        self.assertEqual(get_gender("فاطمه"), "FEMALE")
        self.assertEqual(get_gender("آذر     "), "FEMALE")
        self.assertEqual(get_gender("الـــناز"), "FEMALE")
        self.assertEqual(get_gender("فاطمه زهرا", True), ("FEMALE", "فاطمه"))
        self.assertEqual(get_gender("یلـــ❤️ــدا"), "FEMALE")
        self.assertEqual(get_gender("  مریم  "), "FEMALE")
        self.assertEqual(get_gender("صغری"), "FEMALE")
        self.assertEqual(get_gender("حانیه"), "FEMALE")
        self.assertEqual(get_gender("جانان", True), ("FEMALE", "جانا"))
        self.assertEqual(get_gender("۱۲۳مهناز۱۲۳"), "FEMALE")
        self.assertEqual(get_gender("فاطی"), "FEMALE")

    def test_detect_unkown(self):
        self.assertEqual(get_gender("(فاطمه)"), "UNKNOWN")
        self.assertEqual(get_gender("fateme"), "UNKNOWN")
        self.assertEqual(get_gender("Ali"), "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
