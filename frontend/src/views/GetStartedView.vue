<template>
  <div class="d-flex align-center justify-center flex-column flex-wrap pt-16">
    <span class="text-h4">Welcome to Automated Onboarding</span>
    <span class="text-subtitle"
      >Answer a few questions and we'll get you up and running!</span
    >
    <div class="pt-8">
      <v-btn
        size="x-large"
        elevation="0"
        variant="flat"
        color="#000080"
        class="text-white"
        @click="this.$router.push('onboard')"
        >Get Started!</v-btn
      >
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style></style>
