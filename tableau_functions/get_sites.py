import tableauserverclient as TSC
from tableau_functions import creds


def get_site_dicts() -> list:
    """
    Use tableauserverclient to get a list dictionaries containing information about sites

    NOTE: This call cannot be made to Tableau Cloud, it will be blocked!
    """

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    with server.auth.sign_in(tab_auth):
        sites, paginator = server.sites.get()

    return [site.__dict__ for site in sites]


def get_site_dict_by_name(site_name) -> list:
    """
    Use tableauserverclient to get a dictionary containing information about the specified site
    """

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    with server.auth.sign_in(tab_auth):
        site = server.sites.get_by_name(site_name)

    return site.__dict__
