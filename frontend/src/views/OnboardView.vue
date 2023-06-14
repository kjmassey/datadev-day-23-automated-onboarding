<template>
  <v-main>
    <v-tabs align-tabs="center" v-model="activeTab" color="#000080">
      <v-tab :value="1"
        >Project Information
        <v-icon
          icon="mdi-check-circle"
          color="green"
          class="pl-2"
          v-if="projValidated"
        ></v-icon
      ></v-tab>
      <v-tab :value="2"
        >Groups
        <v-icon
          icon="mdi-check-circle"
          color="green"
          class="pl-2"
          v-if="groupValidated"
        ></v-icon
      ></v-tab>
      <v-tab :value="3"
        >Users
        <v-icon
          icon="mdi-check-circle"
          color="green"
          class="pl-2"
          v-if="userValidated"
        ></v-icon
      ></v-tab>
      <v-tab :value="4"
        >Confirm & Onboard<v-icon
          icon="mdi-check-circle"
          color="green"
          class="pl-2"
          v-if="requestCompleted"
        ></v-icon
      ></v-tab>
    </v-tabs>

    <ProjectInfo
      :showMe="showProjInfo"
      v-on:formSubmit="projFormSubmit($event)"
    />
    <GroupInfo
      :showMe="showGroupInfo"
      :projInfo="projInfo"
      v-on:formSubmit="groupFormSubmit($event)"
    />
    <UserInfo
      :showMe="showUserInfo"
      :groupInfo="groupInfo"
      v-on:formSubmit="userFormSubmit($event)"
    />
    <ReviewAndSubmit
      :showMe="showConfirm"
      :projInfo="projInfo"
      :groupInfo="groupInfo"
      :userInfo="userInfo"
      v-on:requestCompleted="showCompletedDialog()"
    />
    <RequestCompleted
      :showMe="showCompleted"
      v-on:toggleShow="
        showCompleted = !showCompleted;
        refreshPage();
      "
    />
    <div class="d-flex justify-center" v-if="showCompleted">
      <ConfettiExplosion />
    </div>
  </v-main>
</template>

<script>
import ProjectInfo from "@/components/ProjectInfo.vue";
import GroupInfo from "@/components/GroupInfo.vue";
import UserInfo from "@/components/UserInfo.vue";
import ReviewAndSubmit from "@/components/ReviewAndSubmit.vue";
import RequestCompleted from "@/components/RequestCompleted.vue";
import ConfettiExplosion from "vue-confetti-explosion";

export default {
  data: () => ({
    activeTab: 1,
    projValidated: false,
    groupValidated: false,
    userValidated: false,
    projInfo: {},
    groupInfo: {},
    userInfo: {},
    showCompleted: false,
  }),
  components: {
    ProjectInfo,
    GroupInfo,
    UserInfo,
    ReviewAndSubmit,
    RequestCompleted,
    ConfettiExplosion,
  },
  computed: {
    showProjInfo() {
      return this.activeTab == 1;
    },
    showGroupInfo() {
      return this.activeTab == 2;
    },
    showUserInfo() {
      return this.activeTab == 3;
    },
    showConfirm() {
      return this.activeTab == 4;
    },
  },
  methods: {
    projFormSubmit(data) {
      this.projInfo = data;
      this.projValidated = true;

      this.activeTab += 1;
    },
    groupFormSubmit(data) {
      this.groupInfo = data;
      this.groupValidated = true;
      this.activeTab += 1;
    },
    userFormSubmit(data) {
      this.userInfo = data;
      this.userValidated = true;
      this.activeTab += 1;
    },
    showCompletedDialog() {
      this.showCompleted = true;
      this.requestCompleted = true;
    },
    refreshPage() {
      location.reload();
    },
  },
};
</script>

<style></style>
