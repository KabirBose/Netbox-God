def create_device(nb):
    name = input("Name (ex. TOR-T09NE-FE002-1): ")
    status = input("Status (ex. active): ")
    role = input("Role (ex. Core Switch): ")
    _type = input("Type (C9200-48P): ")
    site_name = input("Site (Toronto): ")
    rack_name = input("Rack (T09NC): ")
    position = input("Position (5): ")

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

def create_devices_bulk(nb, devices):
    for device in devices:
        try:
            site = nb.dcim.sites.get(name=device["site_name"])
            if not site:
                print(f"Site '{device["site_name"]}' not found.")
                return

            rack = nb.dcim.racks.get(name=device["rack_name"], site_id=site.id)
            if not rack:
                print(f"Rack '{device["rack_name"]}' not found in site '{device["site_name"]}'.")
                return

            device = nb.dcim.devices.create(
                name=device["name"],
                status=device["status"],
                role=nb.dcim.device_roles.get(name=device["role"]).id,
                device_type=nb.dcim.device_types.get(model=device["_type"]).id,
                site=site.id,
                rack=rack.id,
                position=device["position"],
                face="front"
            )
            print(f"\nDevice '{device["name"]}' created successfully.")

        except Exception as err:
            print(f"Device creation failed: {err}")