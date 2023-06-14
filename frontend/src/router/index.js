import { createRouter, createWebHistory } from "vue-router";
import GetStartedView from "@/views/GetStartedView.vue";
import OnboardView from "@/views/OnboardView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: GetStartedView,
  },
  {
    path: "/onboard",
    name: "onboard",
    component: OnboardView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
