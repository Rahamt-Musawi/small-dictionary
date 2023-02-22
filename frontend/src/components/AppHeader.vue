<template>
  <div>
    <nav class="flex items-center justify-between flex-wrap bg-slate-700 p-6">
      <div class="flex items-center flex-shrink-0 text-sky-50 mr-6">
        <img
          class="fill-current h-8 w-8 mr-2"
          width="54"
          height="54"
          viewBox="0 0 54 54"
          src="../assets/icon.png"
        />
        <span class="text-2xl font-bold font-outline-4">Small Dictionary</span>
      </div>

      <div class="float-right">
        <div class="text-sm border-solid flex-grow lg:flex float-right">
          <a
            href="http://localhost:8080/"
            class="text-l font-semibold block mt-4 lg:inline-block lg:mt-0 text-teal-50 hover:underline mr-4"
          >
            Home
          </a>
          <a
            href="https://github.com/Rahamt-Musawi?tab=repositories"
            class="text-l font-semibold block mt-4 lg:inline-block lg:mt-0 text-teal-50 hover:underline mr-4"
          >
            Github Page
          </a>
          <a
            @click="about"
            class="cursor-pointer text-l font-semibold block mt-4 lg:inline-block lg:mt-0 text-teal-50 hover:underline"
          >
            About
          </a>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "AppHeader",
  methods: {
    about() {
      this.$emit("about");
    },
  },
};
</script>
