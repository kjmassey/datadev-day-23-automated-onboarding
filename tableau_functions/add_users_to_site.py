import tableauserverclient as TSC
from tableau_functions import creds


def add_users_to_site(user_list) -> list:
    """
    Use TSC to add users to a site on Tableau Server. Return a list of dictionaries with the user information
    """

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    users_added = []

    with server.auth.sign_in(tab_auth):
        for user in user_list:
            existing_users = server.users.filter(name=user)

            if len(existing_users) > 0:
                users_added.append(existing_users[0].__dict__)

            else:
                new_user = TSC.UserItem(name=user, site_role="Viewer")
                users_added.append(server.users.add(new_user).__dict__)

    return users_added
