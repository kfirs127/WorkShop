from Business.Rules.Rule import Rule
from Business.Managment.UserManagment import UserManagment
from Business.StorePackage.Bag import Bag
from datetime import datetime


class ruleCreator:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ruleCreator.__instance is None:
            ruleCreator()
        return ruleCreator.__instance

    def __init__(self):
        if ruleCreator.__instance is None:
            ruleCreator.__instance = self

    def createStoreWeightRule(self, storeid, less_than, bigger_than):  # weight of the products in store
        f = lambda bag: self.weightStoreHelper(storeid, less_than, bag) and not self.weightStoreHelper(storeid,
                                                                                                       bigger_than, bag)
        return Rule(f)

    def weightStoreHelper(self, sid, less_than, bag: Bag):
        if bag.getStoreId() == sid:
            products = bag.getProducts()
            sum_product_weight = 0
            for prod, quantity in products.items():
                sum_product_weight += prod.getProductWeight() * quantity
            return sum_product_weight <= less_than
        else:
            return False

    def createProductWeightRule(self, pid, storeId, less_than, bigger_than):  # weight of 1 product
        f = lambda bag: self.weightProductHelper(pid, storeId, less_than, bag) and not \
                        self.weightProductHelper(pid, storeId, bigger_than, bag)
        return Rule(f)

    def weightProductHelper(self, pid, storeId, less_than, bag: Bag):
        if bag.getStoreId() == storeId:
            products = bag.getProducts()
            sum_product_weight = 0
            for prod, quantity in products.items():
                if prod.getProductId() == pid:
                    sum_product_weight += prod.getProductWeight() * quantity
            return sum_product_weight <= less_than
        else:
            return False

    def createStoreQuantityRule(self, storeId, less_than, bigger_than):
        f = lambda bag: self.storeTotalPriceRuleHelper(bag, storeId, less_than) and not self.storeTotalPriceRuleHelper(
            bag, storeId, bigger_than)
        return Rule(f)

    def storeQuantityRuleHelper(self, bag, storeId, less_than):
        if bag.getStoreId() == storeId:
            products = bag.getProducts()
            sum_product = 0
            for prod, quantity in products.items():
                sum_product += quantity
            return sum_product <= less_than
        else:
            return False

    def createCategoryRule(self, storeId, category, less_than, bigger_than):  # quantity of catagory
        f = lambda bag: self.categoryRuleHelper(bag, storeId, category, less_than) and not \
                         self.categoryRuleHelper(bag, storeId, category, bigger_than)
        return Rule(f)

    def categoryRuleHelper(self, bag, storeId, category, less_than):
        if bag.getStoreId() == storeId:
            products = bag.getProducts()
            sum_product = 0
            for prod, quantity in products.items():
                if prod.getProductCategory() == category:
                    sum_product += quantity
            return sum_product <= less_than
        else:
            return False

    def createProductRule(self, storeId, pid, less_than, bigger_than):  # quantity of products
        f = lambda bag: self.productRuleHelper(bag, storeId, less_than, pid) and not \
                        self.productRuleHelper(bag, storeId, bigger_than, pid)
        return Rule(f)

    def productRuleHelper(self, bag, storeId, less_than, pid):
        if bag.getStoreId() == storeId:
            products = bag.getProducts()
            sum_product = 0
            for prod, quantity in products.items():
                if prod.getProductId() == pid:
                    sum_product += quantity
            return sum_product <= less_than
        else:
            return False

    def createStorePriceRule(self, storeId, less_than, bigger_than):  # total price of store
        f = lambda bag: self.storeTotalPriceRuleHelper(bag, storeId, less_than) and not self.storeTotalPriceRuleHelper(
            bag, storeId, bigger_than)
        return Rule(f)

    def storeTotalPriceRuleHelper(self, bag, storeId, less_than):
        if bag.getStoreId() == storeId:
            products = bag.getProducts()
            sum_product = 0
            for prod, quantity in products.items():
                sum_product += quantity * prod.getProductPrice()
            return sum_product <= less_than
        else:
            return False