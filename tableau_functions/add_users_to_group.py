import tableauserverclient as TSC
from tableau_functions import creds


def add_user_to_server_group(group_name, user_name) -> dict:
    """
    Use TSC to add an existing user to an existing group on Tableau Server. Returns a dictionary with details
    """

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    with server.auth.sign_in(tab_auth):
        groups = server.groups.filter(name=group_name)

        if len(groups) < 1:
            return "Group not found!"

        group = groups[0]

        users = server.users.filter(name=user_name)

        if len(users) < 1:
            return "User not found"

        user = users[0]

        return server.groups.add_user(group, user._id).__dict__
