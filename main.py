import pynetbox

nb = pynetbox.api(
    'https://demo.netbox.dev/',
    token='c582ab825448249cf6e80575639050517a5c0d5d'
)

def create_device():
    name = input("Name: ")
    status = input("Status: ")
    role = input("Role: ")
    _type = input("Type: ")
    site_name = input("Site: ")
    rack_name = input("Rack: ")
    position = input("Position: ")

    try:
        site = nb.dcim.sites.get(name=site_name)
        if not site:
            print(f"Site '{site_name}' not found.")
            return

        rack = nb.dcim.racks.get(name=rack_name, site_id=site.id)
        if not rack:
            print(f"Rack '{rack_name}' not found in site '{site_name}'.")
            return

        device = nb.dcim.devices.create(
            name=name,
            status=status,
            role=nb.dcim.device_roles.get(name=role).id,
            device_type=nb.dcim.device_types.get(model=_type).id,
            site=site.id,
            rack=rack.id,
            position=position,
            face="front"
        )
        print(f"\nDevice '{name}' created successfully.")

    except Exception as err:
        print(f"Device creation failed: {err}")


create_device()