<template>
  <v-scale-transition>
    <v-main v-if="$props.showMe">
      <div class="d-flex align-center justify-center w-100">
        <v-card width="80%" max-width="650" elevation="6">
          <v-card-title>Let's Add Some Users!</v-card-title>
          <v-card-subtitle
            >This step is optional -- you can do it later via the Tableau Server
            UI</v-card-subtitle
          >
          <v-card-text>
            <v-row no-gutters="">
              <span class="text-subtitle-2"
                >Add users to your groups below by adding one email per line in
                the corresponding text box(es).</span
              >
            </v-row>
            <v-row no-gutters class="pt-10">
              <v-col class="px-4">
                <v-textarea
                  variant="outlined"
                  no-resize
                  :label="$props.groupInfo.devGroupName"
                  v-model="devGroupUsers"
                  rows="2"
                  auto-grow
                ></v-textarea>

                <v-textarea
                  variant="outlined"
                  no-resize
                  :label="$props.groupInfo.uatGroupName"
                  v-model="uatGroupUsers"
                  rows="2"
                  auto-grow
                ></v-textarea>

                <v-textarea
                  variant="outlined"
                  no-resize
                  :label="$props.groupInfo.prodGroupName"
                  v-model="prodGroupUsers"
                  rows="2"
                  auto-grow
                ></v-textarea>
              </v-col>
            </v-row>
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
    devGroupUsers: "",
    uatGroupUsers: "",
    prodGroupUsers: "",
  }),
  methods: {
    emitFormData() {
      let emitObj = {
        devGroupUsers: this.devGroupUsers,
        uatGroupUsers: this.uatGroupUsers,
        prodGroupUsers: this.prodGroupUsers,
      };

      this.$emit("formSubmit", emitObj);
    },
  },
  props: { showMe: Boolean, groupInfo: Object },
};
</script>

<style></style>
