import tableauserverclient as TSC
from tableau_functions import creds


def create_tableau_server_group(group_name, group_type) -> dict:
    """
    Use TSC to create a new group. Returns a dictionary of details about the new group.
    """

    role_by_type_dict = {
        "DEV": "ExplorerCanPublish",
        "UAT": "Explorer",
        "PROD": "Viewer",
    }

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    with server.auth.sign_in(tab_auth):
        new_group = TSC.GroupItem(name=group_name)
        new_group.minimum_site_role = role_by_type_dict[group_type]

        return server.groups.create(new_group).__dict__
