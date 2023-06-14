<template>
  <v-app>
    <v-main>
      <v-app-bar color="#D3D3D3" elevation="1" rounded="">
        <v-app-bar-nav-icon @click="$router.push('/')">
          <v-icon
            icon="mdi-chart-bar-stacked"
            size="36"
            color="#000080"
          ></v-icon>
        </v-app-bar-nav-icon>
        <v-app-bar-title @click="$router.push('/')" style="cursor: pointer"
          >Automated Tableau Onboarding</v-app-bar-title
        >
        <v-spacer />
        <v-btn icon="mdi-dots-vertical" @click="showAboutInfo = !showAboutInfo">
        </v-btn>
      </v-app-bar>
      <AboutInfo
        v-on:toggleShow="showAboutInfo = !showAboutInfo"
        :showMe="showAboutInfo"
      />
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import AboutInfo from "@/components/AboutInfo.vue";

export default {
  name: "App",
  components: { AboutInfo },

  data: () => ({
    showAboutInfo: false,

    //
  }),
};
</script>

<style scoped></style>
