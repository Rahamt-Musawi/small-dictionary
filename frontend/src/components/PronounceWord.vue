<template>
    <div>
      <img src="../assets/pronounce.png" @click="speak" class="cursor-pointer object-fill h-6 mb-1 w-6 inline-block ml-2"/>
    </div>
  </template>
  
  <script>
  export default {
    name: "PronounceWord",
    props: ["pronounce_word"],
    data() {
      return {
      }
    },
    methods: {
      speak() {
        const msg = new SpeechSynthesisUtterance(this.$props.pronounce_word);
        window.speechSynthesis.speak(msg);
      }
    }
  }
  </script>
  