import unittest

from AcceptanceTests.Bridges.MarketBridge.MarketProxyBridge import MarketProxyBridge
from AcceptanceTests.Bridges.MarketBridge.MarketRealBridge import MarketRealBridge
from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge


class UseCaseGetStoresInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proxy_market = MarketProxyBridge(MarketRealBridge())
        cls.proxy_user = UserProxyBridge(UserRealBridge())

        cls.proxy_user.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva", "Ben Gurion", 1, 1)
        cls.__guestId1 = cls.proxy_user.login_guest().getData().getUserID()
        cls.proxy_user.register("testUser", "1234", "0540000000", 123, 1, "Israel", "Beer Sheva", "Rager", 1, 0)
        # store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code
        cls.user_id = cls.proxy_user.login_member(cls.__guestId1, "testUser", "1234").getData().getUserID()
        cls.store_id = cls.proxy_user.open_store("testStore", cls.user_id, 123, 1, "Israel", "Beer Sheva", "Rager",
                                                   1, 00000).getData().getStoreId()
        cls.store_id1 = cls.proxy_user.open_store("testStore1", cls.user_id, 123, 1, "Israel", "Beer Sheva", "Rager", 1,
                                                  00000).getData().getStoreId()
        cls.__guestId2 = cls.proxy_user.login_guest().getData().getUserID()
        cls.proxy_user.register("testUser2", "1234", "0540000000", 123, 1, "Israel", "Beer Sheva", "Rager", 1, 0)
        cls.manager_id = cls.proxy_user.login_member(cls.__guestId2, "testUser2", "1234").getData().getUserID()
        cls.proxy_market.appoint_store_manager(cls.store_id, cls.user_id, "testUser2")

    # not passing due to storePermissionDTO - userId
    def test_get_stores_info_positive(self):
        permissions = self.proxy_market.get_store_info(self.store_id, self.user_id).getData()
        for permission in permissions:
            print(permission)

    def test_get_store_by_id(self):
        print(self.proxy_market.get_store_by_ID(self.store_id).getData())

    def test_get_all_stores(self):
        stores = self.proxy_market.getAllStores().getData()
        for store in stores:
            print(store)

    def test_user_store(self):
        userStores = self.proxy_market.getUserStore(self.user_id).getData()
        for us in userStores:
            print(us)


if __name__ == '__main__':
    unittest.main()