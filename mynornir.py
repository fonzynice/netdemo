from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_netmiko.tasks.netmiko_send_command import netmiko_send_command
import pprint

name = 'cisco'

nr = InitNornir(config_file="config.yaml")
r2 = nr.run(
    task=netmiko_send_command,
    command_string="show ip route"
)

r = nr.run(
    task=napalm_get,
    getters=["facts"]
)
pprint.pprint(r["rtr1"][0].result)





