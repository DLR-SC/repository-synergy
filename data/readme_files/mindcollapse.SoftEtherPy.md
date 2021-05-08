SoftEtherPy
===========

SoftEther VPN Server Python Management API.

Python implementation of SoftEther VPN management protocol. Can be used for controlling remote server, automation or statistics.

Usage example
-------------
```python
from softether.api import SoftEtherAPI

api = SoftEtherAPI('vpn.whitehouse.gov', 443, '123456password')

api.connect()
api.authenticate()

print(api.test())
# {'UniStrValue': ['world\x00'], 'IntValue': [1], 'Int64Value': [2], 'StrValue': ['1']}

print(api.get_server_info())
# {'OsVendorName': ['Unknown Vendor'], 'OsProductName': ['Linux'], 'KernelName': ['Linux Kernel'], 'ServerType': [0], 'ServerHostName': ['vpnserver'], 'OsServicePack': [0], 'ServerBuildDate': [1413977090000], 'OsSystemName': ['Linux'], 'ServerBuildInt': [9506], 'ServerVerInt': [411], 'ServerProductName': ['SoftEther VPN Server (64 bit)'], 'OsType': [3100], 'ServerFamilyName': ['SoftEther'], 'ServerBuildInfoString': ['Compiled 2014/10/22 20:24:50 by yagi at pc25'], 'ServerVersionString': ['Version 4.11 Build 9506   (English)'], 'OsVersion': ['Unknown Linux Version']}

print(api.get_server_status())
# {'TotalMemory': [0], 'NumSessionsTotal': [0], 'NumTcpConnectionsRemote': [0], 'Send.UnicastBytes': [577743326], 'Recv.BroadcastCount': [1224620], 'NumHubStatic': [0], 'FreePhys': [0], 'ServerType': [0], 'UsedPhys': [0], 'NumHubDynamic': [0], 'Send.BroadcastCount': [43225], 'NumTcpConnections': [49], 'AssignedBridgeLicensesTotal': [0], 'Send.UnicastCount': [1746888], 'AssignedBridgeLicenses': [0], 'NumSessionsLocal': [0], 'AssignedClientLicenses': [0], 'Send.BroadcastBytes': [3140072], 'NumHubStandalone': [1], 'Recv.UnicastCount': [1752958], 'NumHubTotal': [1], 'AssignedClientLicensesTotal': [0], 'NumGroups': [0], 'Recv.BroadcastBytes': [74615494], 'CurrentTime': [1418792416592], 'UsedMemory': [0], 'Recv.UnicastBytes': [580004599], 'FreeMemory': [0], 'CurrentTick': [3039999042], 'TotalPhys': [0], 'NumSessionsRemote': [0], 'NumUsers': [3], 'StartTime': [1415753738050], 'NumTcpConnectionsLocal': [49], 'NumIpTables': [1], 'NumMacTables': [1]}

api.disconnect()
```
