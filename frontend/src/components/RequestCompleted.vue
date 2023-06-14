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
          <span>Congratulations - Your onboarding is complete!</span>

          <v-btn
            icon="mdi-close"
            size="small"
            elevation="0"
            @click="$emit('toggleShow')"
          ></v-btn></div
      ></v-card-title>
      <v-card-subtitle>Wasn't that easy??</v-card-subtitle>
      <v-card-text
        >Your projects, groups and users have been created. Users have been
        added to the groups you specified, and those groups' permissions have
        been applied. You're ready to go!</v-card-text
      >
      <v-card-text
        ><a
          href="https://10ax.online.tableau.com/#/site/kjmdev797388/explore"
          target="_blank"
          >Click here</a
        >
        to start exploring!</v-card-text
      >
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "RequestCompleted",
  data: () => ({}),
  props: { showMe: Boolean },
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
