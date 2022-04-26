import unittest
from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.MarketBridge.MarketProxyBridge import MarketProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge
from Service.MarketService import MarketService
from Service.UserService import UserService


class UseCaseAppointStoreManager(unittest.TestCase):
    # use-case 4.6

    def setUp(self):
        self.proxy_market = MarketProxyBridge(MarketService())
        self.proxy_user = UserProxyBridge(UserRealBridge(UserService(), MarketService()))

        # username, password, phone, account_number, branch, country, city, street, apartment_num, bank, ICart
        self.owner_id = self.proxy_user.register("testUser", "1243", "0540000000", 123,[] ,"Israel", "Beer Sheva", "Rager", 1, "testBank", None)
        self.manager_id = self.proxy_user.register("testUser2", "1245", "0540000001", 124, [], "Israel", "Beer Sheva", "Rager", 1, "testBank", None)
        # store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code
        self.store_id = self.proxy_user.open_store("testStore", self.owner_id , 123, None, "Israel", "Beer Sheva", "Rager", 1, 00000)

    def test_AppointStoreManagerPositive(self):
        # store_id, assigner_id, assignee_id
        self.assertEqual(self.proxy_market.appoint_store_manager(self.store_id, self.owner_id, self.manager_id), True)

    def test_AppointStoreManagerNoStore(self):
        self.assertEqual(self.proxy_market.appoint_store_manager(-1, self.owner_id, self.manager_id), False)

    def test_AppointStoreManagerNoOwner(self):
        self.assertEqual(self.proxy_market.appoint_store_manager(self.store_id, -1, self.manager_id), False)

    def test_AppointStoreManagerNoNewManager(self):
        self.assertEqual(self.proxy_market.appoint_store_manager(self.store_id, self.owner_id, -1), False)

    def tearDown(self):
        self.proxy_market.close_store(self.store_id)


if __name__ == '__main__':
    unittest.main()
