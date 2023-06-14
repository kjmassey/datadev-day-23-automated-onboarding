<template>
  <v-dialog
    max-width="575"
    transition="dialog-bottom-transition"
    persistent
    v-model="$props.showMe"
  >
    <v-card max-width="575">
      <v-card-title>
        <div class="d-flex align-center justify-space-between">
          <span>Automated Tableau Onboarding Portal</span>

          <v-btn
            icon="mdi-close"
            size="small"
            elevation="0"
            @click="$emit('toggleShow')"
          ></v-btn></div
      ></v-card-title>
      <v-card-subtitle>Created for Tableau DataDev Day 2023</v-card-subtitle>
      <v-card-text
        >This is an example of an application that can automate Tableau project,
        group and user onboarding!</v-card-text
      >
      <v-card-text>
        <div>Created by Kyle Massey</div>
        <div class="pt-4 pb-2">
          <v-icon icon="mdi-twitter" color="#1DA1F2"></v-icon>
          <a href="https://twitter.com/UpInYourVizness" target="_blank">
            @UpInYourVizness
          </a>
        </div>
        <div>
          <v-icon icon="mdi-linkedin" color="#0077b5"></v-icon>
          <a href="https://www.linkedin.com/in/kylejmassey" target="_blank">
            kylejmassey
          </a>
        </div>
      </v-card-text>
      <v-card-actions></v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "AboutInfo",
  data: () => ({}),
  props: { showMe: Boolean },
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
