<template>
  <v-scale-transition>
    <v-main v-if="$props.showMe">
      <div class="d-flex align-center justify-center w-100">
        <v-card width="80%" max-width="650" elevation="6">
          <v-card-title> New Groups Details: </v-card-title>
          <v-card-subtitle>All fields are required!</v-card-subtitle>
          <v-card-text>
            <div class="pt-2">
              <v-form ref="projForm">
                <v-row no-gutters="">
                  <span class="text-subtitle-2"
                    >Suggested group names have been entered for you. You can
                    change them here if you want!</span
                  >
                </v-row>
                <v-row class="pt-4"></v-row>
                <v-row no-gutters="" class="pt-4">
                  <v-text-field
                    v-model="devGroupName"
                    variant="outlined"
                    density="compact"
                    label="Developers"
                    prepend-inner-icon="mdi-account-group"
                    style="max-width: 550px"
                  ></v-text-field>
                  <v-btn variant="flat">
                    <v-icon icon="mdi-information-outline" size="22"></v-icon>
                    <v-tooltip activator="parent" location="bottom"
                      >The users in this group will be able to publish
                      workbooks/datasources in lower environments.</v-tooltip
                    >
                  </v-btn>
                </v-row>
                <v-row no-gutters="" class="pt-4">
                  <v-text-field
                    v-model="uatGroupName"
                    variant="outlined"
                    density="compact"
                    label="UAT Testers"
                    prepend-inner-icon="mdi-account-group"
                    style="max-width: 550px"
                  ></v-text-field>
                  <v-btn variant="flat">
                    <v-icon icon="mdi-information-outline" size="22"></v-icon>
                    <v-tooltip activator="parent" location="bottom"
                      >The users in this group will have read-only access in the
                      UAT/Test environment.</v-tooltip
                    >
                  </v-btn>
                </v-row>
                <v-row no-gutters="" class="pt-4">
                  <v-text-field
                    v-model="prodGroupName"
                    variant="outlined"
                    density="compact"
                    label="Users"
                    prepend-inner-icon="mdi-account-group"
                    style="max-width: 550px"
                  ></v-text-field>
                  <v-btn variant="flat">
                    <v-icon icon="mdi-information-outline" size="22"></v-icon>
                    <v-tooltip activator="parent" location="bottom"
                      >The users in this group will have read-only access in
                      production.</v-tooltip
                    >
                  </v-btn>
                </v-row>
              </v-form>
            </div>
          </v-card-text>
          <v-card-actions>
            <div class="d-flex align-center justify-end w-100">
              <v-btn
                variant="flat"
                color="#000080"
                class="text-white"
                @click="emitFormData()"
                >Next</v-btn
              >
            </div>
          </v-card-actions>
        </v-card>
      </div>
    </v-main>
  </v-scale-transition>
</template>

<script>
export default {
  data: () => ({
    devGroupName: "",
    uatGroupName: "",
    prodGroupName: "",
  }),
  methods: {
    emitFormData() {
      let emitObj = {
        devGroupName: this.devGroupName,
        uatGroupName: this.uatGroupName,
        prodGroupName: this.prodGroupName,
      };

      this.$emit("formSubmit", emitObj);
    },
  },

  props: { showMe: Boolean, projInfo: Object },
  updated() {
    this.devGroupName = `${this.$props.projInfo.proj_name} Developers`;
    this.uatGroupName = `${this.$props.projInfo.proj_name} UAT Testers`;
    this.prodGroupName = `${this.$props.projInfo.proj_name} Users`;
  },
};
</script>

<style></style>
