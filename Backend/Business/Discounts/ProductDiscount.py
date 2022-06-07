from typing import Dict

import zope


from Backend.Business.Rules.DiscountRuleComposite import DiscountRuleComposite
from Backend.Business.Rules.RuleCreator import RuleCreator
from Backend.Exceptions.CustomExceptions import NotFoundException
from Backend.Interfaces.IDiscount import IDiscount
from ModelsBackend.models import DiscountModel, DiscountRulesModel, RuleModel, ProductModel, ProductsInBagModel


@zope.interface.implementer(IDiscount)
class ProductDiscount:

    def __init__(self, discountId=None, productId=None, percent=None, model=None):
        # self.__discountId = discountId
        # self.__productId = productId
        # self.__percent = percent
        # self.__rules: Dict[int: IRule] = {}

        if model is None:
            self.__model = DiscountModel.objects.get_or_create(discountID=discountId, productID=productId, percent=percent,
                                                               type='Product')[0]
        else:
            self.__model = model

    def calculate(self, bag):  # return the new price for each product
        isCheck = self.check(bag)
        newProductPrices: Dict[ProductModel, float] = {}
        products = bag.getProducts()
        for prod in products:
            if prod.getProductId() == self.__model.productID and isCheck:
                newProductPrices[prod] = self.__model.percent
            else:
                newProductPrices[prod] = 0
        return newProductPrices

        # isCheck = self.check(bag)
        # newProductPrices: Dict[Product, float] = {}
        # products: Dict[Product, int] = bag.getProducts()  # [product: quantity]
        # for prod in products.keys():
        #     if prod.getProductId() == self.__productId and isCheck:
        #         newProductPrices[prod] = self.__percent
        #     else:
        #         newProductPrices[prod] = 0
        # return newProductPrices

    def addSimpleRuleDiscount(self, rule):
        DiscountRulesModel.objects.get_or_create(discountID=self.__model, ruleID=rule.getModel())

    def addCompositeRuleDiscount(self, ruleId, rId1, rId2, ruleType, ruleKind):
        if len(RuleModel.objects.filter(ruleID=rId1)) != 1:
            raise NotFoundException("rule1 is not an existing discount")
        if len(RuleModel.objects.filter(ruleID=rId2)) != 1:
            raise NotFoundException("rule1 is not an existing discount")

        r1 = RuleModel.objects.get(ruleID=rId1)
        r2 = RuleModel.objects.get(ruleID=rId2)

        rule = RuleModel.objects.get_or_create(ruleID=ruleId, ruleID1=r1, ruleID2=r2, composite_rule_type=ruleType,
                                               rule_kind=ruleKind)[0]
        DiscountRulesModel.objects.get_or_create(discountID=self.__model, ruleID=rule)
        DiscountRulesModel.objects.get(discountID=self.__model, ruleID=r1).delete()
        DiscountRulesModel.objects.get(discountID=self.__model, ruleID=r2).delete()
        return DiscountRuleComposite(model=rule)

        # r1 = self.__rules.get(rId1)
        # r2 = self.__rules.get(rId2)
        # if r1 is None:
        #     raise Exception("rule1 is not an existing discount")
        # if r2 is None:
        #     raise Exception("rule2 is not an existing discount")
        # rule = DiscountRuleComposite(ruleId, r1, r2, ruleType, ruleKind)
        # self.__rules[rule.getRuleId()] = rule
        # self.__rules.pop(rId1)
        # self.__rules.pop(rId2)
        # return rule

    def removeDiscountRule(self, rId):
        if len(RuleModel.objects.filter(ruleID=rId)) != 1:
            raise NotFoundException("rule1 is not an existing discount")
        rule = RuleModel.objects.get(ruleID=rId)

        if len(DiscountRulesModel.objects.filter(discountID=self.__model, ruleID=rule)) != 1:
            raise NotFoundException("rule hasn't been connected to any discount")
        DiscountRulesModel.objects.get(discountID=self.__model, ruleID=rule).delete()

    def check(self, bag):
        rules = [RuleCreator.getInstance().buildRule(rule.ruleID)
                 for rule in DiscountRulesModel.objects.filter(discountID=self.__model.discountID)]
        for rule in rules:
            if not rule.check(bag):
                return False
        return True

    def getTotalPrice(self, bag):
        newPrices = self.calculate(bag)
        totalPrice = 0.0
        for product, quantity in bag.getProducts().items():
            if product.getProductId() == self.__model.productID:
                totalPrice += (1 - newPrices.get(product)) * product.getProductPrice() * quantity
            else:
                totalPrice += product.getProductPrice() * quantity
        return totalPrice

    def getAllDiscountRules(self):
        rules = []
        for discountRule in DiscountRulesModel.objects.filter(discountID=self.__model):
            rule = RuleCreator.getInstance().buildRule(discountRule.ruleID)
            rules.append(rule)
        return rules

    def getDiscountId(self):
        return self.__model.discountID

    def getProductId(self):
        return self.__model.productID

    def getDiscountPercent(self):
        return self.__model.percent

    def getModel(self):
        return self.__model

    def remove(self):
        for rule in self.getAllDiscountRules():
            rule.removeRule()
        self.__model.delete()

    def __eq__(self, other):
        return isinstance(other, ProductDiscount) and self.__model == other.getModel()

    def __hash__(self):
        return hash(self.__model.ruleID)
