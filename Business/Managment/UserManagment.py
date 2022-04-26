from Business.Address import Address
from Business.Bank import Bank
from Business.Market import Market
from interfaces import IMarket
from typing import Dict
from Business.UserPackage.Member import Member
from interface import implements
from interfaces.IUser import IUser
from Business.UserPackage.SystemManager import SystemManager


class UserManagment(implements(IUser)):
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if UserManagment.__instance is None:
            UserManagment()
        return UserManagment.__instance

    def __init__(self):
        """ Virtually private constructor. """
        self.__market: IMarket = Market().getInstance()
        self.__members: Dict[str, Member] = {}
        self.__systemManager: Dict[str, SystemManager] = {}
        if UserManagment.__instance is None:
            UserManagment.__instance = self

    def getMembers(self):
        return self.__members

    def guestLogin(self):
        try:
            if len(self.__systemManager) > 0:
                return self.__market.addGuest()
            else:
                raise Exception("There no system manager!")
        except Exception as e:
            raise Exception(e)


    def guestLogOut(self, guestID):  # need to remove cart!
        self.__market.getActiveUsers().pop(guestID)
        return True


    def memberSignUp(self, userName, password, phone, address, bank, icart):  # Tested
        if self.__members.get(userName) is None:
            member = Member(userName, password, phone, address, bank)
            self.__members[userName] = member
            if icart is not None:
                  member.setICart(icart)
            return member.getUserID()
        return None



    def memberLogin(self, userName, password): #Tested
        try:
            if len(self.__systemManager) > 0:
                i: Member = Member(None, None, None, None, None)
                check = False
                for i in self.__members.values():
                    if i.getUserName() == userName:
                        if self.__market.getActiveUsers().get(i.getUserID()) is None:
                            if i.getPassword() == password:
                                self.__market.getActiveUsers()[i.getUserID()] = i
                                check = True
                                i.setLoggedIn(True)
                                i.setMemberCheck(True)
                                self.__market.loginUpdates(i.getUserID())
                                return i.getUserID()
                            else:
                                raise Exception("password not good!")
                        else:
                            raise Exception("member allready login")
                if check == False:
                    raise Exception("The user ID " + userName + " not registered!")
            else:
                raise Exception("There no system manager!")
        except Exception as e:
            raise Exception(e)

    def logoutMember(self, userName):
        user = self.__members.get(userName)
        self.__market.getActiveUsers().pop(user.getUserID())
        self.__members.get(user.getUserID()).setLoggedIn(False)
        self.__members.get(user.getUserID()).setMemberCheck(False)
        return self.guestLogin()

    def systemManagerSignUp(self, userName, password, phone, address, bank):
        if self.__members.get(userName) is None:
            systemManager: SystemManager = SystemManager(userName, password, phone, address, bank)
            if systemManager:
                self.__systemManager[userName] = systemManager
                return systemManager.getUserID()
        return None


    def createBankAcount(self, accountNumber, branch):
        return Bank(accountNumber, branch)

    def createAddress(self, country, city, street, apartmentNum, zipCode):
        return Address(country, city, street, apartmentNum, zipCode)

    def removeMember(self,userName,password):
        pass