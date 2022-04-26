import unittest

from AcceptanceTests.Bridges.MarketBridge.MarketProxyBridge import MarketProxyBridge
from AcceptanceTests.Bridges.MarketBridge.MarketRealBridge import MarketRealBridge
from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge
from Service.MarketService import MarketService
from Service.UserService import UserService


class UseCaseGetEditUserCart(unittest.TestCase):
    def setUp(self):
        self.market_proxy = MarketProxyBridge(MarketRealBridge(MarketService()))
        self.user_proxy = UserProxyBridge(UserRealBridge(UserService(), MarketService()))
        self.user_proxy.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva",
                                          "Ben Gurion", 1, 1)
        self.user_id = self.user_proxy.register("user1", "1234", "0500000000", "500", "20", "Israel", "Beer Sheva",
                                                "Ben Gurion", 0, "HaPoalim", None)
        self.user_proxy.login_member("user1", "1234")
        self.store_id = self.user_proxy.open_store("store", self.user_id, 0, 0, "israel", "Beer-Sheva", "Ben-Gurion",
                                                   0, "000000")
        self.product1 = self.market_proxy.add_product_to_store(self.store_id, self.user_id, "Product", 500,
                                                               "Category", ["Test1", "Test2"])

    def test_get_cart_info_positive1(self):
        self.assertEqual(self.market_proxy.get_cart_info(self.user_id), True)

    def test_get_cart_info_negative1(self):
        self.assertEqual(self.market_proxy.get_cart_info(-999), False)

    def test_edit_cart_info_positive1(self):
        old_info = self.user_proxy.get_cart_info("User1")
        self.user_proxy.add_product_to_cart(self.user_id, self.store_id, self.product1, 50)
        new_info = self.user_proxy.get_cart_info("User1")
        self.assertNotEqual(old_info, new_info)

    # def test_edit_cart_info_negative1(self):  # NEED TO EDIT THIS
    #     old_info = self.user_proxy.get_cart_info("User1")
    #     new_info = self.user_proxy.add_product_to_cart(1, 0, 5)
    #     self.assertEqual(old_info, new_info)


if __name__ == '__main__':
    unittest.main()
