<template>
  <div>
    <form @submit.prevent="sendMessage" class="p-4">
      <div class="flex">
        <div class="inline-block relative w-64">
          <select
            name="lang"
            @change="onChange($event)"
            class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2.5 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline"
          >
            <option value="">English - Engish</option>
            <option>German - English</option>
            <option>English - German</option>
          </select>
          <div
            class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
          >
            <svg
              class="fill-current h-4 w-4"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
            >
              <path
                d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
              />
            </svg>
          </div>
        </div>

        <div class="relative w-full">
          <input
            v-model="word"
            @focus="clear_text"
            type="search"
            id="search-dropdown"
            class="block p-2.5 w-full z-20 text-sm text-gray-900 bg-gray-50 rounded-r-lg border-l-gray-50 border-l-2 border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-500 dark:border-l-gray-500 dark:border-gray-400 dark:placeholder-gray-400 dark:text-white dark:focus:border-blue-500"
            placeholder="Search words here..."
            required
          />
          <button
            type="submit"
            class="absolute top-0 right-0 p-2.5 text-sm font-medium text-white bg-blue-700 rounded-r-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              ></path>
            </svg>
            <span class="sr-only">Search</span>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "SearchForm",

  props: ["message"],

  data() {
    return {
      word: this.$props.message,
    };
  },

  methods: {
    sendMessage() {
      this.$emit("search_for", this.word);
    },

    clear_text(){
      this.word=''
    },

    onChange(e) {
      console.log("For now, we support just English - English!");
      console.log(e.target.value);
      this.language = e.target.value;
    },
  },
};
</script>
