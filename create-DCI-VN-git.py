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



##create variables
vn_name = "VLAN-30"
vni = "300030"
vlan = 30
vrf = "VRF"


##Define rack nodes for Virtual-Network association. In this case its all nodes with role "leaf"

bound_to_1 = list()
tor_nodes_1 = aos.blueprint.get_all_tor_nodes(bp1.id)

for node in tor_nodes_1:
    bound_to_1.append({"system_id": node["id"],"vlan_id": vlan})
    
    
bound_to_2 = list()
tor_nodes_2 = aos.blueprint.get_all_tor_nodes(bp2.id)

for node in tor_nodes_2:
    bound_to_2.append({"system_id": node["id"],"vlan_id": vlan})

##Create VLAN-30 DC1

aos.blueprint.create_virtual_network(
    bp_id=bp1.id,
    name=vn_name,
    vn_id=vni,
    sz_name=vrf,
    bound_to=bound_to_1,
    tagged_ct=True,
    ipv4_subnet="10.0.30.0/24",
    ipv4_gateway="10.0.30.254",
)


##Create VLAN-30 DC2

aos.blueprint.create_virtual_network(
    bp_id=bp2.id,
    name=vn_name,
    vn_id=vni,
    sz_name=vrf,
    bound_to=bound_to_2,
    tagged_ct=True,
    ipv4_subnet="10.0.30.0/24",
    ipv4_gateway="10.0.30.254",
)
