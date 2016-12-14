import subprocess
import logging

LOG_FILENAME = '/var/log/SetPAC.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )
logging.getLogger().addHandler(logging.StreamHandler())
interface_set_devices = ["Wi-Fi", "Airport", "Ethernet"]
interface_names = []
proxy_url='http://domain.edu/proxy.pac'

interfaces = subprocess.check_output(['networksetup -listallnetworkservices | tail +2'],shell = True).splitlines()

interface_names = [s for s in interfaces if any(xs in s for xs in interface_set_devices)]

for i in interface_names:
    if proxy_url in subprocess.check_output("networksetup -getautoproxyurl '{}'".format(i), shell=True):
            logging.info('PAC URL Previously Configured for {}'.format(i))
    else:
        try:
            subprocess.check_output("networksetup -setautoproxyurl '{}' '{}'".format(i, proxy_url), shell=True)
            logging.info("Applying PAC URL on  {}".format(i))
        except subprocess.CalledProcessError:
            logging.info("Error Applying PAC URL on '{}'".format(i))
