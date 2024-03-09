import json
import time
import clr
import os
import sys


class ElasticServerConnector:
    def __init__(self, userID, appName):
        """
        :param userID: user email address.
        :param appName: Get Appname From Elastic Server Admin.
        """
        self.flag = False
        self.userID = userID
        self.appName = appName
        try:
            self.connectorDLLPath = os.path.abspath('AutoServerConnector_DLLs\\AutoServerConnector.dll')
            self.connectorDLL = clr.AddReference(self.connectorDLLPath)
            print('Added AutoServerConnector.dll')

            dllFilesDir = r'AutoServerConnector_DLLs'

            for file in os.listdir(dllFilesDir):
                if file.endswith('.dll') and file != 'AutoServerConnector.dll':
                    # print(f'Adding DLL Dependency: {file}')
                    absPath = os.path.abspath(dllFilesDir + '\\' + file)
                    clr.AddReference(absPath)

        except Exception as e:
            print('DLL is missing OR broken! Exiting!')
            print(f'Error: {e}')
            sys.exit()

    def pushData(self, data):
        """
        :param data: Json Object
        :return: Output of DLL file -> True
        """
        sys.path.append(os.getcwd())
        print(self.connectorDLLPath)

        from System import Type
        clsName = self.connectorDLL.GetType('AutoServerConnector.PublishROIData')
        method = clsName.GetMethod('PublishROItoServer')
        RetType = None
        output = method.Invoke(RetType, [self.appName, self.userID, data])
        print(f'Elastic Server Data Push Status: {output}')
