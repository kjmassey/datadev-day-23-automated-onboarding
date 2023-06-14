import tableauserverclient as TSC
from tableau_functions import creds

PROJ_PERMS_BY_GROUP_TYPE = {
    "DEV": {"Read": "Allow", "Write": "Allow"},
    "UAT": {
        TSC.Permission.Capability.Read: TSC.Permission.Mode.Allow,
    },
    "PROD": {
        TSC.Permission.Capability.Read: TSC.Permission.Mode.Allow,
    },
}

WB_PERMS_BY_GROUP_TYPE = {
    "DEV": {
        "RunExplainData": "Allow",
        "ViewComments": "Allow",
        "CreateRefreshMetrics": "Allow",
        "ExportData": "Allow",
        "ViewUnderlyingData": "Allow",
        "AddComment": "Allow",
        "Filter": "Allow",
        "Write": "Allow",
        "Delete": "Allow",
        "ExportXml": "Allow",
        "ChangeHierarchy": "Allow",
        "ChangePermissions": "Allow",
        "ExportImage": "Allow",
        "ShareView": "Allow",
        "Read": "Allow",
        "WebAuthoring": "Allow",
    },
    "UAT": {
        "RunExplainData": "Allow",
        "Filter": "Allow",
        "ViewUnderlyingData": "Allow",
        "Read": "Allow",
        "ExportImage": "Allow",
        "WebAuthoring": "Allow",
        "ExportData": "Allow",
        "AddComment": "Allow",
        "ShareView": "Allow",
        "ViewComments": "Allow",
    },
    "PROD": {
        "AddComment": "Allow",
        "ViewComments": "Allow",
        "Read": "Allow",
        "ExportImage": "Allow",
        "Filter": "Allow",
        "ExportData": "Allow",
    },
}

DS_PERMS_BY_GROUP_TYPE = {
    "DEV": {
        "SaveAs": "Allow",
        "Write": "Allow",
        "Delete": "Allow",
        "ExportXml": "Allow",
        "ChangeHierarchy": "Allow",
        "ChangePermissions": "Allow",
        "Connect": "Allow",
        "Read": "Allow",
    },
    "UAT": {"Connect": "Allow", "ExportXml": "Allow", "Read": "Allow"},
    "PROD": {"Read": "Allow", "Connect": "Allow"},
}


def apply_group_permissions_by_type(proj_name, group_name, group_type) -> dict:
    """
    Use TSC to apply a set of permissions to a group based on its type. Return a dictionary of what was applied.
    """

    server = TSC.Server(creds.URL, use_server_version=True)
    tab_auth = TSC.TableauAuth(creds.UID, creds.PW, site_id=creds.SITE_NAME)

    perms_applied = {"group_name": group_name}

    with server.auth.sign_in(tab_auth):
        projs = server.projects.filter(name=proj_name)

        if len([proj for proj in projs]) < 1:
            return "Project not found!"

        proj = projs[0]

        server.projects.populate_permissions(proj)
        server.projects.populate_workbook_default_permissions(proj)
        server.projects.populate_datasource_default_permissions(proj)

        groups = server.groups.filter(name=group_name)

        if len([group for group in groups]) < 1:
            return "Group not found!"

        group = groups[0]

        # Apply default permissions at the project level
        proj_rules = TSC.PermissionsRule(
            grantee=group, capabilities=PROJ_PERMS_BY_GROUP_TYPE[group_type]
        )

        server.projects.update_permission(proj, [proj_rules])
        perms_applied["project"] = PROJ_PERMS_BY_GROUP_TYPE[group_type]

        # Apply default permissions at the workbook level
        wb_rules = TSC.PermissionsRule(
            grantee=group, capabilities=WB_PERMS_BY_GROUP_TYPE[group_type]
        )

        server.projects.update_workbook_default_permissions(proj, [wb_rules])
        perms_applied["workbook"] = WB_PERMS_BY_GROUP_TYPE[group_type]

        # Apply default permissions at the datasource level
        ds_rules = TSC.PermissionsRule(
            grantee=group, capabilities=DS_PERMS_BY_GROUP_TYPE[group_type]
        )

        # Additional permissions for Metrics, Flows, etc. could be added here too!

        server.projects.update_datasource_default_permissions(proj, [ds_rules])
        perms_applied["datasource"] = DS_PERMS_BY_GROUP_TYPE[group_type]

        return perms_applied
