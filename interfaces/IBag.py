from interface import Interface


class IBag(Interface):

    def isEmpty(self):
        pass

    def addProduct(self, productId, quantity):
        pass

    def removeProduct(self, productId):
        pass

    def removeProductQuantity(self, productId, quantity):
        pass

    def getProducts(self):
        pass

    def getProductQuantity(self, productId):
        pass

    def calcSum(self):
        pass
