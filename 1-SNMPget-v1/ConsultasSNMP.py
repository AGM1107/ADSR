from pysnmp.hlapi import *


def getinfo(oid):
    resp = ""
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('comunidadSNMP', mpModel=0),
        UdpTransportTarget(('localhost', 161)),
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


def hex_to_string(hex):
    if hex[:2] == '0x':
        hex = hex[2:]
    string_value = bytes.fromhex(hex).decode('utf-8')
    return string_value


res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
print(res.split(" = ")[1].split(": ")[2])
res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.4.0'))
print(res.split(" = ")[1])
res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.5.0'))
print(res.split(" = ")[1])
res = getinfo(ObjectIdentity('1.3.6.1.2.1.1.6.0'))
print(res.split(" = ")[1])
res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.1.0'))
print(res.split(" = ")[1])

for i in range(1, int(res.split(" = ")[1])):
    res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.2.1.7.' + str(i)))
    print(res.split(" = ")[1])
    res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.2.1.8.' + str(i)))
    print(res.split(" = ")[1])
    res = getinfo(ObjectIdentity('1.3.6.1.2.1.2.2.1.2.' + str(i)))
    print(hex_to_string(res.split(" = ")[1]))
