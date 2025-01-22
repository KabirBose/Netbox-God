import pynetbox

from functions import *
from data import *

nb = pynetbox.api(
    'https://demo.netbox.dev/',
    token='ffbadca22c80f2b9f95a83e20eb7c2e5bb6d5262'
)

# create_device(nb)
create_devices_bulk(nb, devices)