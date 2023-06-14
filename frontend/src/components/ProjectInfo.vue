<template>
  <v-scale-transition>
    <v-main v-if="$props.showMe">
      <div class="d-flex align-center justify-center w-100">
        <v-card width="80%" max-width="650" elevation="6">
          <v-card-title> New Project Details: </v-card-title>
          <v-card-subtitle>All fields are required!</v-card-subtitle>
          <v-card-text>
            <div class="pt-4">
              <v-form ref="projForm">
                <v-row no-gutters="">
                  <v-col>
                    <div>
                      <span class="text-body-1 d-block pb-2">Site Name:</span>
                      <v-select
                        variant="outlined"
                        density="compact"
                        :items="sitesList"
                        v-model="siteName"
                        return-object
                        item-title="_name"
                      ></v-select>
                    </div>
                  </v-col>
                </v-row>
                <v-row no-gutters="">
                  <v-col>
                    <div>
                      <span class="text-body-1 d-block pb-2"
                        >Project Name:</span
                      >
                      <v-text-field
                        variant="outlined"
                        density="compact"
                        hint='No special characters besides "_" and "-"!'
                        class="pb-4"
                        v-model="projName"
                      ></v-text-field>
                    </div>
                  </v-col>
                </v-row>
                <v-row no-gutters="">
                  <v-col>
                    <div>
                      <span class="text-body-1 d-block pb-2"
                        >Permissions Type:</span
                      >
                      <v-radio-group
                        density="compact"
                        inline
                        class="pt-1"
                        v-model="permsType"
                        color="#000080"
                      >
                        <v-radio
                          value="locked"
                          label="Locked"
                          class="pr-4"
                          model-value="locked"
                        ></v-radio>
                        <v-radio
                          value="customizable"
                          label="Customizable"
                          model-value="customizable"
                        ></v-radio>
                      </v-radio-group>
                    </div>
                  </v-col>
                </v-row>
                <v-row no-gutters="">
                  <v-col>
                    <div class="pt-1">
                      <span class="text-body-1 d-block pb-2"
                        >Environments:</span
                      >
                      <div class="d-flex align-center justify-start ml-n2">
                        <v-checkbox
                          label="DEV"
                          color="#000080"
                          v-model="createDev"
                        ></v-checkbox>
                        <v-checkbox
                          label="TEST/UAT"
                          color="#000080"
                          v-model="createUat"
                        ></v-checkbox>
                        <v-checkbox
                          label="PROD"
                          color="#000080"
                          v-model="createProd"
                          disabled
                        ></v-checkbox>
                      </div>
                    </div>
                  </v-col>
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
import axios from "axios";

export default {
  data: () => ({
    sitesList: [],
    siteName: "",
    projName: "",
    permsType: "locked",
    validated: false,
    createDev: true,
    createUat: true,
    createProd: true,
  }),
  props: { showMe: Boolean },
  methods: {
    emitFormData() {
      let emitObj = {
        site_name: this.siteName,
        proj_name: this.projName,
        perms_type: this.permsType,
        create_dev: this.createDev,
        create_uat: this.createUat,
        create_prod: this.createProd,
      };

      this.$emit("formSubmit", emitObj);
    },
    getSites() {
      axios.get("http://localhost:5000/getSites").then((response) => {
        this.sitesList = response.data;
      });
    },
  },
  mounted() {
    this.getSites();
  },
};
</script>

<style></style>
