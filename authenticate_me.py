import time
import clr
import os
import sys


class InvalidUserException(Exception):
    pass


class AuthenticateMe:
    """
    This Class will authenticate an Employee Of Ubisoft
    Pre-requisite
    Add MFA dir in same directory as of this class
    Add MFA.dll and Microsoft.Identity.Client.dll in MFA dir.
    If Invalid User Login is found then application will crash.
    """

    def __init__(self):
        self.flag = False
        self.userEmailID = ''
        try:
            self.MFADLL = os.path.abspath(r'MFA/MFA.dll')
            self.mircrosoftIdentityDLL = os.path.abspath(r'MFA/Microsoft.Identity.Client.dll')
        except Exception as e:
            print('Authentication DLL is missing OR broken! Exiting!')
            print(f'Error: {e}')
            sys.exit()

        self.authenticate

    @property
    def authenticate(self):
        # from asyncio.windows_events import NULL
        sys.path.append(os.getcwd())

        clr.AddReference(self.mircrosoftIdentityDLL)
        mfaDLL = clr.AddReference(self.MFADLL)

        # from System import Type
        my_type = mfaDLL.GetType('MFA.Authentication')
        method = my_type.GetMethod('IsValidAuthenticatication')

        RetType = ""
        self.userEmailID = method.Invoke(RetType, None)
        self.userEmailID = self.userEmailID.lower()
        print(f'Username:{self.userEmailID}')
        if not self.userEmailID:
            raise InvalidUserException('Either Invalid User Login detected OR Blank Credentials were provided.')

        return self.userEmailID


if __name__ == '__main__':
    auth = AuthenticateMe()
