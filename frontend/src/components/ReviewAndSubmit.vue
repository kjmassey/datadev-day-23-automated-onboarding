<template>
  <v-overlay
    v-model="showLoader"
    scroll-strategy="block"
    class="align-center justify-center"
    persistent
  >
    <div class="d-flex flex-column align-center justify-center">
      <v-progress-circular
        indeterminate
        color="#0000B0"
        size="55"
      ></v-progress-circular>
      <div class="pt-2">
        <span class="text-subtitle-2">{{ loadingMsg }}...</span>
      </div>
    </div>
  </v-overlay>
  <v-scale-transition>
    <v-main v-if="$props.showMe">
      <div class="d-flex align-center justify-center w-100">
        <v-card width="80%" max-width="650" elevation="6">
          <v-card-title> Confirm and Submit</v-card-title>
          <v-card-subtitle
            >Make sure everything looks correct -- then we'll be up in running
            in moments!</v-card-subtitle
          >
          <v-card-text>
            <span class="text-h6">Project Info:</span>
            <div class="pl-6 pt-2">
              <ul>
                <li class="text-subtitle">
                  <u>Name:</u> {{ $props.projInfo.proj_name }}
                </li>
                <li class="text-subtitle">
                  <u>Site Name:</u> {{ $props.projInfo.site_name._name }}
                </li>
                <li class="text-subtitle">
                  <u>Permissions:</u> {{ $props.projInfo.perms_type }}
                </li>
                <li class="text-subtitle">
                  <u>Environments:</u> {{ envsList }}
                </li>
              </ul>
            </div>
          </v-card-text>
          <v-card-text>
            <span class="text-h6">Groups Info:</span>
            <div class="pl-6 pt-2">
              <ul>
                <li class="text-subtitle">
                  <u>Developers:</u> {{ $props.groupInfo.devGroupName }}
                  <span v-if="devUserCount > 0"
                    >(adding {{ devUserCount }}
                    {{ devUserCount > 1 ? "users" : "user" }})</span
                  >
                </li>
                <li class="text-subtitle">
                  <u>UAT Testers:</u>
                  {{ $props.groupInfo.uatGroupName }}
                  <span v-if="uatUserCount > 0"
                    >(adding {{ uatUserCount }}
                    {{ uatUserCount > 1 ? "users" : "user" }})</span
                  >
                </li>
                <li class="text-subtitle">
                  <u>Production Users:</u>
                  {{ $props.groupInfo.prodGroupName }}
                  <span v-if="prodUserCount > 0"
                    >(adding {{ prodUserCount }}
                    {{ prodUserCount > 1 ? "users" : "user" }})</span
                  >
                </li>
              </ul>
            </div>
          </v-card-text>

          <v-card-actions>
            <div class="d-flex align-center justify-end w-100">
              <v-btn
                variant="flat"
                color="#000080"
                class="text-white"
                @click="submitOnboardRequest()"
                >Submit</v-btn
              >
            </div>
          </v-card-actions>
        </v-card>
      </div>
    </v-main>
  </v-scale-transition>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    showLoader: false,
    loadingMsg: "",
    projsCreated: {},
    groupsCreated: {},
    usersCreated: [],
    usersAddedToGroups: [],
    permsApplied: [],
  }),
  computed: {
    emailList() {
      return this.$props.userInfo.us;
    },
    envsList() {
      let envStr = "";

      if (this.$props.projInfo.create_dev) {
        if (envStr == "") {
          envStr = "DEV";
        } else {
          envStr += ", DEV";
        }
      }
      if (this.$props.projInfo.create_uat) {
        if (envStr == "") {
          envStr = "UAT";
        } else {
          envStr += ", UAT";
        }
      }

      envStr += ", PROD";
      return envStr;
    },
    devUserCount() {
      if (this.$props.userInfo.devGroupUsers == "") {
        return 0;
      } else {
        return (
          (this.$props.userInfo.devGroupUsers.match(/\n/g) || "").length + 1
        );
      }
    },
    uatUserCount() {
      if (this.$props.userInfo.uatGroupUsers == "") {
        return 0;
      } else {
        return (
          (this.$props.userInfo.uatGroupUsers.match(/\n/g) || "").length + 1
        );
      }
    },
    prodUserCount() {
      if (this.$props.userInfo.prodGroupUsers == "") {
        return 0;
      } else {
        return (
          (this.$props.userInfo.prodGroupUsers.match(/\n/g) || "").length + 1
        );
      }
    },
  },
  methods: {
    async createNewProjects() {
      this.loadingMsg = "Creating projects";

      let projReq = {
        proj_name: this.$props.projInfo.proj_name,
        perms_type: this.$props.projInfo.perms_type,
        create_dev: this.$props.projInfo.create_dev,
        create_uat: this.$props.projInfo.create_uat,
        create_prod: this.$props.projInfo.create_prod,
      };

      await axios
        .post("http://localhost:5000/createProject", projReq)
        .then((projResp) => {
          this.projsCreated = projResp.data;
        });
    },
    async createNewGroups() {
      this.loadingMsg = "Creating groups";

      let groupReq = [];

      if (this.$props.projInfo.create_dev) {
        groupReq.push({
          group_name: this.$props.groupInfo.devGroupName,
          group_type: "DEV",
        });
      }

      if (this.$props.projInfo.create_uat) {
        groupReq.push({
          group_name: this.$props.groupInfo.uatGroupName,
          group_type: "UAT",
        });
      }

      if (this.$props.projInfo.create_prod) {
        groupReq.push({
          group_name: this.$props.groupInfo.prodGroupName,
          group_type: "PROD",
        });
      }

      await axios
        .post("http://localhost:5000/createGroups", groupReq)
        .then((groupResp) => {
          this.groupsCreated = groupResp.data;
        });
    },

    async addUsersToSite() {
      this.loadingMsg = "Adding users to site";

      let userEmails = [];

      this.$props.userInfo.devGroupUsers.split(/\n/g).forEach((e) => {
        if (e != "") {
          userEmails.push(e);
        }
      });

      this.$props.userInfo.uatGroupUsers.split(/\n/g).forEach((e) => {
        if (e != "") {
          userEmails.push(e);
        }
      });

      this.$props.userInfo.prodGroupUsers.split(/\n/g).forEach((e) => {
        if (e != "") {
          userEmails.push(e);
        }
      });

      await axios
        .post("http://localhost:5000/addUsersToSite", userEmails)
        .then((userResp) => {
          this.usersCreated = userResp.data;
        });
    },

    async addUsersToGroups() {
      this.loadingMsg = "Adding users to groups";

      let reqObj = {};

      reqObj[this.$props.groupInfo.devGroupName] =
        this.$props.userInfo.devGroupUsers.split(/\n/g);

      reqObj[this.$props.groupInfo.uatGroupName] =
        this.$props.userInfo.uatGroupUsers.split(/\n/g);

      reqObj[this.$props.groupInfo.prodGroupName] =
        this.$props.userInfo.prodGroupUsers.split(/\n/g);

      await axios
        .post("http://localhost:5000/addUsersToGroups", reqObj)
        .then((resp) => {
          this.usersAddedToGroups = resp.data;
        });
    },
    async applyGroupPermissions() {
      this.loadingMsg = "Applying group permissions";

      let reqObj = [
        {
          project_name: `${this.$props.projInfo.proj_name} DEV`,
          group_name: this.$props.groupInfo.devGroupName,
          group_type: "DEV",
        },
        {
          project_name: `${this.$props.projInfo.proj_name} UAT`,
          group_name: this.$props.groupInfo.devGroupName,
          group_type: "DEV",
        },
        {
          project_name: `${this.$props.projInfo.proj_name} UAT`,
          group_name: this.$props.groupInfo.uatGroupName,
          group_type: "UAT",
        },
        {
          project_name: `${this.$props.projInfo.proj_name} PROD`,
          group_name: this.$props.groupInfo.prodGroupName,
          group_type: "PROD",
        },
      ];

      await axios
        .post("http://localhost:5000/applyGroupPermissions", reqObj)
        .then((resp) => {
          this.permsApplied = resp.data;
        });
    },

    async submitOnboardRequest() {
      // DISPLAY OVERLAY/LOADER
      this.showLoader = true;

      await this.createNewProjects();
      await this.createNewGroups();
      await this.addUsersToSite();
      await this.addUsersToGroups();
      await this.applyGroupPermissions();

      this.showLoader = false;
      this.$emit("requestCompleted");
    },
  },
  props: {
    showMe: Boolean,
    projInfo: Object,
    groupInfo: Object,
    userInfo: Object,
  },
};
</script>

<style></style>
