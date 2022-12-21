import json

from aos.client import AosClient
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AOS_IP = "10.10.10.10"
AOS_PORT = 443
AOS_USER = "admin"
AOS_PW = "password"

##Login

aos = AosClient(protocol="https", host=AOS_IP, port=AOS_PORT)
aos.auth.login(AOS_USER, AOS_PW)


##Find Blueprint by Name

bp1 = aos.blueprint.get_id_by_name(label="Elisabeth-1")

bp2 = aos.blueprint.get_id_by_name(label="Elisabeth-2")



##Find IP resource pool to use with the Routing-Zone, create name, VNI and vlan_id
leaf_lo_pool = aos.resources.ipv4_pools.find_by_name(name="vrf_loopbacks").pop()
sz_name = "VRF"
vni = 300000
vlan = 3000


##Create Routing-Zone DC1

aos.blueprint.create_security_zone(
    bp_id=bp1.id,
    name=sz_name,
    leaf_loopback_ip_pools=[leaf_lo_pool.id],
    vni_id=vni,
    vlan_id=vlan,
)


##Create Routing-Zone DC2

aos.blueprint.create_security_zone(
    bp_id=bp2.id,
    name=sz_name,
    leaf_loopback_ip_pools=[leaf_lo_pool.id],
    vni_id=vni,
    vlan_id=vlan,
)