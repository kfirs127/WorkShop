import unittest
from AcceptanceTests.Bridges.MarketBridge.MarketProxyBridge import MarketProxyBridge
from AcceptanceTests.Bridges.MarketBridge.MarketRealBridge import MarketRealBridge
from AcceptanceTests.Bridges.UserBridge.UserProxyBridge import UserProxyBridge
from AcceptanceTests.Bridges.UserBridge.UserRealBridge import UserRealBridge
from AcceptanceTests.Tests.ThreadWithReturn import ThreadWithReturn


class UseCasePurchaseRules(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.proxy_market = MarketProxyBridge(MarketRealBridge())
    #     cls.proxy_user = UserProxyBridge(UserRealBridge())
    #
    #     cls.proxy_user.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva",
    #                                           "Ben Gurion", 1, 1)
    #     # username, password, phone, account_number, branch, country, city, street, apartment_num, bank, ICart
    #     cls.__guestId1 = cls.proxy_user.login_guest().getData().getUserID()
    #     cls.proxy_user.register("testUser1", "1234", "0540000000", 123, [], "Israel", "Beer Sheva",
    #                             "Rager", 1,
    #                             "testBank")
    #     cls.user_id1 = cls.proxy_user.login_member(cls.__guestId1, "testUser1", "1234").getData().getUserID()
    #
    #     # store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code
    #     cls.store_id1 = cls.proxy_user.open_store("testStore1", cls.user_id1, 123, None, "Israel", "Beer Sheva",
    #                                               "Rager", 1, 00000).getData().getStoreId()
    #
    #     cls.store_id2 = cls.proxy_user.open_store("testStore2", cls.user_id1, 123, None, "Israel", "Beer Sheva",
    #                                               "Rager", 1, 00000).getData().getStoreId()
    #
    #     cls.product_id = cls.proxy_market.add_product_to_store(cls.store_id1, cls.user_id1, "testProduct1", 10,
    #                                                            "testCategory", 20, ["test"]).getData().getProductId()
    #     cls.product_id_2 = cls.proxy_market.add_product_to_store(cls.store_id1, cls.user_id1, "testProduct2", 100,
    #                                                              "testCategory1", 17, ["test"]).getData().getProductId()
    #     cls.product_id_3 = cls.proxy_market.add_product_to_store(cls.store_id1, cls.user_id1, "testProduct3", 20,
    #                                                              "testCategory", 15, ["test"]).getData().getProductId()
    #     cls.product_id_4 = cls.proxy_market.add_product_to_store(cls.store_id2, cls.user_id1, "testProduct4", 10,
    #                                                              "testCategory", 15, ["test"]).getData().getProductId()
    #
    #     cls.proxy_market.add_quantity_to_store(cls.store_id1, cls.user_id1, cls.product_id, 100)
    #     cls.proxy_market.add_quantity_to_store(cls.store_id1, cls.user_id1, cls.product_id_2, 100)
    #     cls.proxy_market.add_quantity_to_store(cls.store_id1, cls.user_id1, cls.product_id_3, 100)
    #     cls.proxy_market.add_quantity_to_store(cls.store_id2, cls.user_id1, cls.product_id_4, 100)

    def setUp(self):
        self.proxy_market = MarketProxyBridge(MarketRealBridge())
        self.proxy_user = UserProxyBridge(UserRealBridge())

        self.proxy_user.appoint_system_manager("Manager", "1234", "0500000000", 1, 1, "Israel", "Beer Sheva",
                                              "Ben Gurion", 1, 1)
        # username, password, phone, account_number, branch, country, city, street, apartment_num, bank, ICart
        self.__guestId1 = self.proxy_user.login_guest().getData().getUserID()
        self.__guestId1 = self.proxy_user.login_guest().getData().getUserID()
        __guestId2 = self.proxy_user.login_guest().getData().getUserID()
        __guestId3 = self.proxy_user.login_guest().getData().getUserID()
        self.proxy_user.register("testUser1", "1234", "0540000000", 123, 1, "Israel", "Beer Sheva",
                                "Rager", 1, 0)
        self.proxy_user.register("testUser2", "1234", "0540000000", 123, 1, "Israel", "Beer Sheva",
                                 "Rager", 1, 0)
        self.proxy_user.register("testUser3", "1234", "0540000000", 123, 1, "Israel", "Beer Sheva",
                                 "Rager", 1, 0)
        self.user_id1 = self.proxy_user.login_member(self.__guestId1, "testUser1", "1234").getData().getUserID()
        self.user_id2 = self.proxy_user.login_member(self.__guestId1, "testUser2", "1234").getData().getUserID()
        self.user_id3 = self.proxy_user.login_member(self.__guestId1, "testUser3", "1234").getData().getUserID()

        # store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code
        self.store_id1 = self.proxy_user.open_store("testStore1", self.user_id1, 123, 1, "Israel", "Beer Sheva",
                                                  "Rager", 1, 00000).getData().getStoreId()

        self.store_id2 = self.proxy_user.open_store("testStore2", self.user_id1, 123, 1, "Israel", "Beer Sheva",
                                                  "Rager", 1, 00000).getData().getStoreId()

        self.product_id = self.proxy_market.add_product_to_store(self.store_id1, self.user_id1, "testProduct1", 10,
                                                               "testCategory", 20, ["test"]).getData().getProductId()
        self.product_id_2 = self.proxy_market.add_product_to_store(self.store_id1, self.user_id1, "testProduct2", 100,
                                                                 "testCategory1", 17, ["test"]).getData().getProductId()
        self.product_id_3 = self.proxy_market.add_product_to_store(self.store_id1, self.user_id1, "testProduct3", 20,
                                                                 "testCategory", 15, ["test"]).getData().getProductId()
        self.product_id_4 = self.proxy_market.add_product_to_store(self.store_id2, self.user_id1, "testProduct4", 10,
                                                                 "testCategory", 15, ["test"]).getData().getProductId()

        self.proxy_market.add_quantity_to_store(self.store_id1, self.user_id1, self.product_id, 100)
        self.proxy_market.add_quantity_to_store(self.store_id1, self.user_id1, self.product_id_2, 100)
        self.proxy_market.add_quantity_to_store(self.store_id1, self.user_id1, self.product_id_3, 100)
        self.proxy_market.add_quantity_to_store(self.store_id2, self.user_id1, self.product_id_4, 100)

    def test_addSimpleRuleStore(self):
        self.proxy_market.addStoreTotalAmountPurchaseRule(self.user_id1, self.store_id1, 100, 2000).getData()

        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id, 10)
        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id_2, 10)
        userTransaction = self.proxy_user.purchase_product(self.user_id1, 10, 10)

        self.assertEqual(1100, userTransaction.getData().getTotalAmount())

    def test_addSimpleRuleStore_NotPassing(self):
        self.proxy_market.addStoreTotalAmountPurchaseRule(self.user_id1, self.store_id1, 1500, 10000).getData()

        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id, 10)
        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id_2, 10)
        userTransaction = self.proxy_user.purchase_product(self.user_id1, 10, 10)

        self.assertEqual(0, userTransaction.getData().getTotalAmount())

    def test_addCondPurchaseRule_AND(self):
        rId1 = self.proxy_market.addProductWeightPurchaseRule(self.user_id1, self.store_id1, self.product_id, 100, 100000).getData().getRuleId()
        rId2 = self.proxy_market.addCategoryQuantityPurchaseRule(self.user_id1, self.store_id1, "testCategory", 0, 5).getData().getRuleId()
        self.proxy_market.addCompositeRulePurchaseAnd(self.user_id1, self.store_id1, rId1, rId2)

        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id, 10)
        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id_2, 10)
        userTransaction = self.proxy_user.purchase_product(self.user_id1, 10, 10)

        self.assertEqual(0, userTransaction.getData().getTotalAmount())

    def test_addCondDiscountRule_OR(self):
        rId1 = self.proxy_market.addProductQuantityPurchaseRule(self.user_id1, self.store_id1, self.product_id, 5, 100000).getData().getRuleId()
        rId2 = self.proxy_market.addStoreQuantityPurchaseRule(self.user_id1, self.store_id1, 0, 30).getData().getRuleId()
        self.proxy_market.addCompositeRulePurchaseAnd(self.user_id1, self.store_id1, rId1, rId2)

        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id, 10)
        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id_2, 10)
        userTransaction = self.proxy_user.purchase_product(self.user_id1, 10, 10)

        self.assertEqual(1100, userTransaction.getData().getTotalAmount())

    def test_addCondDiscountRule_OR_AND_with_discount(self):
        self.proxy_market.addSimpleDiscount_Product(self.user_id1, self.store_id1, self.product_id_2, 0.1).getData().getDiscountId()

        rId1 = self.proxy_market.addProductWeightPurchaseRule(self.user_id1, self.store_id1, self.product_id, 100, 100000).getData().getRuleId()
        rId2 = self.proxy_market.addCategoryQuantityPurchaseRule(self.user_id1, self.store_id1, "testCategory", 0, 5).getData().getRuleId()
        rId3 = self.proxy_market.addStoreTotalAmountPurchaseRule(self.user_id1, self.store_id1, 100, 100000).getData().getRuleId()

        rOr_id = self.proxy_market.addCompositeRulePurchaseOr(self.user_id1, self.store_id1, rId1, rId2).getData().getRuleId()
        self.proxy_market.addCompositeRulePurchaseAnd(self.user_id1, self.store_id1, rId3, rOr_id)

        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id, 10)
        self.proxy_user.add_product_to_cart(self.user_id1, self.store_id1, self.product_id_2, 10)
        userTransaction = self.proxy_user.purchase_product(self.user_id1, 10, 10)
        print(userTransaction)
        self.assertEqual(1000, userTransaction.getData().getTotalAmount())


if __name__ == '__main__':
    unittest.main()