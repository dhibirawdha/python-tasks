def nat():
    NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    return NAT.replace("FastEthernet", "GigabitEthernet")


def vlan():
    CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    v = CONFIG.strip().split()
    return v[-1]

def duplicatevlan():
    VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    return sorted(set(VLANS))


def intersectionvlan():
    command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
    command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
    c1 = command1.strip().split()[-1]
    l1 = c1.split(",")
    set1 = set(l1)
    print(set1)
    c2 = command2.strip().split()[-1]
    l2 = c2.split(",")
    set2 = set(l2)
    print(set2)
    return set1.intersection(set2)


def ospfroute():
    ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
    list1 = ospf_route.split()
    template = """
                    Protocol: OSPF
                    Prefix: {}
                    AD/Metric: {}
                    Next-Hop: {}
                    Last update {}
                    Outbound Interface {}
                    """.format(list1[1], list1[2], list1[4], list1[5], list1[6])
    return template

def binmac():
    MAC = 'AAAA:BBBB:CCCC'
    s = "".join(MAC.split(":"))
    return " ".join(format(ord(x), "b") for x in s)

def ipinbin():
    ip = "192.168.3.1"
    newip = ip.split(".")
    s = ""
    template = """
    {}
    {}
    """
    for i in newip:
        s = s + template.format(i, bin(int(i)))
    return s

def main():
    print(nat())
    print(vlan())
     print(duplicatevlan())
    print(intersectionvlan())
    print(ospfroute())
    print(binmac())
    print(ipinbin())

if __name__ == "__main__":
    main()
