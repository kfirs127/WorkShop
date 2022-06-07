import zope


from AcceptanceTests.Bridges.UserBridge.IUserBridge import IUserBridge
from Backend.Service.MemberService import MemberService
from Backend.Service.RoleService import RoleService
from Backend.Service.UserService import UserService


@zope.interface.implementer(IUserBridge)
class UserRealBridge:
    def __init__(self):
        self._roleService = RoleService()
        self._memberService = MemberService()
        self._userService = UserService()


    def request(self) -> bool:
        if self.check_access():
            self._real_subject.request()
        else:
            return True

    def login_guest(self):
        return self._userService.enterSystem()

    def register(self,username, password, phone, account_number, branch, country,
                 city, street, apartment_num, zip_code):
        return self._userService.memberSignUp(username, password, phone, account_number, branch,
                                               country, city, street, apartment_num, zip_code)

    def login_member(self, oldUserId, user_name, password):
        return self._userService.memberLogin(oldUserId, user_name, password)

    def add_product_to_cart(self, user_id, store_id, product_id, quantity):
        return self._userService.addProductToCart(user_id, store_id, product_id, quantity)

    def purchaseProductWithoutAddress(self, userID, cardNumber, month, year, holderCardName, cvv, holderID,
                                      country, city, street, apartmentNum, zipCode):
        return self._userService.purchaseCartWithoutAddress(userID, cardNumber, month, year, holderCardName, cvv, holderID,
                                                            country, city, street, apartmentNum, zipCode)

    def purchase_product(self, user_id, cardNumber, month, year, holderCardName, cvv, holderID):
        return self._userService.purchaseCart(user_id, cardNumber, month, year, holderCardName, cvv, holderID)

    def logout_member(self, userName):
        return self._memberService.logoutMember(userName)

    def removeSystemManger_forTests(self, systemMangerName):
        return self._userService.removeSystemManger_forTests(systemMangerName)

    def removeMember(self, systemManagerName, memberName):
        return self._roleService.removeMember(systemManagerName, memberName)

    def getAllActiveUsers(self, systemManagerName):
        return self._roleService.getAllActiveUsers(systemManagerName)

    def open_store(self, store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code):
        return self._memberService.createStore(store_name, founder_id, account_num, branch, country, city, street, apartment_num, zip_code)

    def removeStore(self,store_id, user_id):
        return self._memberService.removeStore(store_id,user_id)

    def recreateStore(self,user_id, store_id):
        return self._memberService.recreateStore(user_id,store_id)

    def appoint_system_manager(self, userName, password, phone, accountNumber, brunch, country, city, street, apartmentNum, zipCode):
        return self._userService.systemManagerSignUp(userName, password, phone, accountNumber, brunch, country, city, street, apartmentNum, zipCode)

    def enter_system(self):
        return self._userService.enterSystem()

    def exit_system(self, guest_id):
        return self._userService.exitSystem(guest_id)

    def remove_product_from_cart(self, user_id, store_id, prod_id):
        return self._userService.removeProductFromCart(user_id, store_id, prod_id)

    def update_prod_from_cart(self, user_id, store_id, prod_id, quantity):
        return self._userService.updateProductFromCart(user_id, store_id, prod_id, quantity)

    def get_cart(self, user_id):
        return self._userService.getCart(user_id)

    def get_sum_after_discount(self, user_id):
        return self._userService.getSumAfterDiscount(user_id)

    def get_member_transaction(self, user_id):
        return self._memberService.getMemberTransactions(user_id)


