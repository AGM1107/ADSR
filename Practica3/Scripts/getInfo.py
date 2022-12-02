from pysnmp.hlapi import *

def getinfo(oid, ipaddress="192.168.1.79", puerto=161, comunidad="comunidadSNMP"):
    resp = ""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(comunidad, mpModel=0),
        UdpTransportTarget((ipaddress, puerto)),
        ContextData(),
        ObjectType(oid)
    )

    errorindication, errorstatus, errorindex, varbinds = next(iterator)

    if errorindication:
        print(errorindication)

    elif errorstatus:
        print('%s at %s' % (errorstatus.prettyPrint(),
                            errorindex and varbinds[int(errorindex) - 1][0] or '?'))

    else:
        for varBind in varbinds:
            resp = (' = '.join([x.prettyPrint() for x in varBind]))
    return resp