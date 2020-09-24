from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command
import pprint
import ipdb
import json

name = 'cisco'

nr = InitNornir(config_file="config.yaml")
get_info = nr.run(
           task=netmiko_send_command,
           command_string="show ip route"
            )

get_info_napalm = nr.run(
        task=napalm_get,
        getters=["facts"]
    )

# ipdb.set_trace()
print_result(get_info)
# pprint.pprint(get_info_napalm["rtr1"][0].result)





