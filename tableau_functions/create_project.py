import tableauserverclient as TSC
from tableau_functions import creds


def create_tableau_server_project(request, env) -> dict:
    """
    Use tableauserver client to create a new project on Tableau Server/Cloud. Returns a dictionary of details about the new project.
    """

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    with server.auth.sign_in(tab_auth):
        perms_str = (
            "LockedToProject" if request["perms_type"] == "locked" else "ManagedByOwner"
        )

        new_proj = TSC.ProjectItem(
            name=f"{request['proj_name']} {env}", content_permissions=perms_str
        )

        return server.projects.create(new_proj).__dict__
