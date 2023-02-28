<template>
  <div class="md:max-lg:flex m-auto bg-slate-50">
    <div class="bg-slate-300 m-auto">
      
      <!-- The header of the application that contains menu -->
      <AppHeader @about="aboutMe" />

      <!-- The component that takes words as input -->
      <SearchForm :message="message" @search_for="sendMessage" v-if="!showAbout"/>

      <!-- It is being shown in case of any error -->
      <div role="alert" v-if="not_found.length > 0 && !showAbout" class="m-10">
        <div class="bg-slate-400 text-white font-bold rounded-t px-4 py-2">
          Error
        </div>
        <div
          class="border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700"
        >
          <p>{{ not_found }}</p>
        </div>
      </div>

      <!-- Loading indicator -->
      <LoadingContent v-if="loading" />

      <!-- All the informations about the given word will be listed here -->
      <div class="w-full bg-white" v-if="word.length > 0 && !showAbout && not_found.length == 0">
        <ul class="list-disc marker:text-blue-500 flex flex-col space-y-3 list-outside mt-7 p-10 leading-relaxed 
          border-x-4 border-gray-100 text-gray-800 dark:text-gray-800">
          <li class="list-none">
            <span v-if="word[0]" class="text-2xl font-semibold text-gray-700">
              {{ searched_word }} 
            </span>
            <PronounceWord class="inline" v-if="word[0]" :pronounce_word="searched_word"/>
          </li>
          <li v-if="definition || web_definition">
            <span class="text-red-900 font-semibold">Definitions </span>
            <p>{{ definition }}</p>
            <p>{{ web_definition }}</p>
          </li>
          <li v-if="synonyms">
            <span class="text-red-900 font-semibold">Synonyms </span>
            <p>{{ synonyms }}</p>
          </li>
          <li v-if="antonyms">
            <span class="text-red-900 font-semibold">Antonyms </span>
            <p>{{ antonyms }}</p>
          </li>
          <li v-if="examples || web_examples">
            <span class="text-red-900 font-semibold">Examples </span>
            <p>{{ examples }}</p>
            <br />
            <p>{{ web_examples }}</p>
          </li>
        </ul>
      </div>

      <!-- Information about the application -->
      <AboutMe v-if="showAbout" />
      <span v-if="!loading" class="text-center content-center">© 2023 Rahmatullah Musawi</span>
    </div>
  </div>
</template>

<script>

/*  
* This component make the main page of the application and includes several components
* Socket.io is used for information exchange between frontend and backend
*/

import { io } from "socket.io-client";
import AppHeader from "./components/AppHeader.vue";
import SearchForm from "./components/SearchForm.vue";
import AboutMe from "./components/AboutMe.vue";
import LoadingContent from "./components/LoadingContent.vue";
import PronounceWord from "./components/PronounceWord.vue";
const socket = io("http://localhost:5000");

export default {
  name: "App",
  components: { AppHeader, SearchForm, AboutMe, LoadingContent, PronounceWord },

  data() {
    return {
      message: "welcome",
      word: "",
      showAbout: false,
      not_found: "",
      loading: false,
    };
  },

  // It send the word to the backend when the component is mounted
  mounted() {
    socket.on("connect", () => {
      console.log("connected to server");
      socket.emit("message", this.message);
      this.loading = true;
    });

    // Receives the error information if the given word is not found
    socket.on("not_found", (data) => {
      this.not_found = data;
      console.log(data);
      this.loading = false;
    });

    // Receives the information about the given word to show 
    socket.on("response", (data) => {
      this.word = data;
      this.loading = false;
      console.log("received message: " + data);
    });
  },

  methods: {
    // Send the given word to the backend by submitting the form
    sendMessage(data) {
      socket.emit("message", data);
      this.not_found = "";
      this.loading = true;
    },

    aboutMe() {
      this.showAbout = true;
    },
  },

  computed: {
    // Capitalize the first letter of the given word
    searched_word() {
      return (
        this.word[0].word.charAt(0).toUpperCase() + this.word[0].word.slice(1)
      );
    },
    // Definition of the word from NLTK wordnet
    definition() {
      return this.word[1].definition;
    },
    // Definition of the word given from the internet using BeautifulSoup
    web_definition() {
      return this.word[1].web_definition[0];
    },
    // Synonyms of the word from NLTK wordnet
    synonyms() {
      return this.word[2].synonyms;
    },
    // Antonyms of the word from NLTK wordent
    antonyms() {
      return this.word[3].antonyms;
    },
    // Example about the word from NLTK wordnet
    examples() {
      return this.word[4].examples;
    },
    // Examples about the word from the internent using BeautifulSoup
    web_examples() {
      return this.word[4].web_examples;
    },
  },
};
</script>
