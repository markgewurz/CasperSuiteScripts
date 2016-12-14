import subprocess
import logging

LOG_FILENAME = '/var/log/search_domain.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    )
logging.getLogger().addHandler(logging.StreamHandler())
interface_set_devices = ["Wi-Fi", "Airport", "Ethernet"]
interface_names = []
search_domain='setsearchdomainhere.com'

interfaces = subprocess.check_output(['networksetup -listallnetworkservices | tail +2'],shell = True).splitlines()

interface_names = [s for s in interfaces if any(xs in s for xs in interface_set_devices)]

for i in interface_names:
    if search_domain in subprocess.check_output("networksetup -getsearchdomains '{}'".format(i), shell=True):
        logging.info('Search Domain already configured for {}'.format(i))
    else:
        try:
            subprocess.check_output("networksetup -setsearchdomains '{}' '{}'".format(i, search_domain), shell=True)
        except subprocess.CalledProcessError:
            logging.info('Error Applying Search Domain on {}'.format(i))
