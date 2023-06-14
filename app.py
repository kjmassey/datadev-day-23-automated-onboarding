from flask import Flask, render_template, request
from tableau_functions.get_sites import get_site_dicts, get_site_dict_by_name
from tableau_functions.create_project import create_tableau_server_project
from tableau_functions.create_group import create_tableau_server_group
from tableau_functions.add_users_to_site import add_users_to_site
from tableau_functions.add_users_to_group import add_user_to_server_group
from tableau_functions.apply_group_permissions import apply_group_permissions_by_type

# Be sure to include this, although when going to production, consider your CORS strategy seriously ;)
from flask_cors import CORS, cross_origin


###
### ALL OF THIS IS FLASK BOILER PLATE STUFF

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

####
####


# The @cross_origin() decorator allows us to use cross-origin requests locally -- don't use this setting in a production environment without knowing what you're doing!
@cross_origin()
@app.route("/getSites", methods=["GET"])
def get_sites():
    return [get_site_dict_by_name("KJM-dev-797388")]


@cross_origin
@app.route("/createProject", methods=["POST"])
def create_project():
    projs_created = {}

    if request.json.get("create_dev"):
        projs_created["DEV"] = create_tableau_server_project(request.json, "DEV")

    if request.json.get("create_uat"):
        projs_created["UAT"] = create_tableau_server_project(request.json, "UAT")

    projs_created["PROD"] = create_tableau_server_project(request.json, "PROD")

    return projs_created


@cross_origin
@app.route("/createGroups", methods=["POST"])
def create_groups():
    req_json = request.json
    groups_created = {}

    for group in req_json:
        groups_created[group["group_type"]] = create_tableau_server_group(
            group["group_name"], group["group_type"]
        )

    return groups_created


@cross_origin
@app.route("/addUsersToSite", methods=["POST"])
def add_site_users():
    req_json = request.json

    return add_users_to_site(req_json)


@cross_origin
@app.route("/addUsersToGroups", methods=["POST"])
def add_group_users():
    req_json = request.json
    users_to_groups = []

    for k, v in req_json.items():
        for user in v:
            if user != "":
                users_to_groups.append(add_user_to_server_group(k, user))

    return users_to_groups


@cross_origin
@app.route("/applyGroupPermissions", methods=["POST"])
def apply_perms():
    req_json = request.json
    perms_updated = []

    for group in req_json:
        perms_updated.append(
            apply_group_permissions_by_type(
                group.get("project_name"),
                group.get("group_name"),
                group.get("group_type"),
            )
        )

    return perms_updated


if __name__ == "__main__":
    app.run(debug=True)
