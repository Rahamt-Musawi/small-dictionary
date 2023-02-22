<template>
  <div class="border-solid border-2 p-10 md:max-lg:flex m-auto">
    <div class="bg-slate-300 m-auto">
      <AppHeader @about="aboutMe" />

      <SearchForm
        :message="message"
        @search_for="sendMessage"
        v-if="!showAbout"
      />

      <div role="alert" v-if="not_found.length > 0 && !showAbout">
        <div class="bg-red-500 text-white font-bold rounded-t px-4 py-2">
          Error
        </div>
        <div
          class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"
        >
          <p>{{ not_found }}</p>
        </div>
      </div>

      <div
        class="w-full bg-custom-text-bg"
        v-if="word.length > 0 && !showAbout && not_found.length == 0"
      >
        <!-- <h2 class="mb-2 text-lg font-semibold text-gray-900 dark:text-white">definitions: </h2> -->
        <ul
          class="list-disc marker:text-blue-500 flex flex-col space-y-3 list-outside mt-7 p-10 leading-relaxed text-gray-800 dark:text-gray-800"
        >
          <li>
            <p
              v-if="word[0]"
              class="text-2xl font-semibold text-gray-700"
            >
              {{ wrd }}
            </p>
          </li>
          <li v-if="definition || web_definition">
            <span class="text-indigo-900 font-semibold">Definitions </span>
            <p>{{ definition }}</p>
            <p>{{ web_definition }}</p>
          </li>
          <li v-if="synonyms">
            <span class="text-indigo-900 font-semibold">Synonyms </span>
            <p>{{ synonyms }}</p>
          </li>
          <li v-if="antonyms">
            <span class="text-indigo-900 font-semibold">Antonyms </span>
            <p>{{ antonyms }}</p>
          </li>
          <li v-if="examples || web_examples">
            <span class="text-indigo-900 font-semibold">Examples </span>
            <p>{{ examples }}</p>
            <br />
            <p>{{ web_examples }}</p>
          </li>
        </ul>
      </div>

      <AboutMe v-if="showAbout" />
      <span class="text-center content-center">© 2023 Rahmatullah Musawi</span>
    </div>
  </div>
</template>

<script>
import { io } from "socket.io-client";
import AppHeader from "./components/AppHeader.vue";
import SearchForm from "./components/SearchForm.vue";
import AboutMe from "./components/AboutMe.vue";
const socket = io("http://localhost:5000");
export default {
  name: "App",
  components: { AppHeader, SearchForm, AboutMe },
  data() {
    return {
      message: "welcome",
      word: "",
      showAbout: false,
      not_found: "",
    };
  },

  mounted() {
    socket.on("connect", () => {
      console.log("connected to server");
      socket.emit("message", this.message);
    });

    socket.on("not_found", (data) => {
      this.not_found = data;
      console.log(data);
    });
    socket.on("response", (data) => {
      this.word = data;
      console.log("received message: " + data);
    });
  },

  methods: {
    sendMessage(data) {
      socket.emit("message", data);
      this.not_found = "";
    },

    aboutMe() {
      this.showAbout = true;
    },
  },

  computed: {
    wrd() {
      return (
        this.word[0].word.charAt(0).toUpperCase() + this.word[0].word.slice(1)
      );
    },

    definition() {
      return this.word[1].definition;
    },
    web_definition() {
      return this.word[1].web_definition[0];
    },

    synonyms() {
      return this.word[2].synonyms;
    },

    antonyms() {
      return this.word[3].antonyms;
    },

    examples() {
      return this.word[4].examples;
    },

    web_examples() {
      return this.word[4].web_examples;
    },
  },
};
</script>
