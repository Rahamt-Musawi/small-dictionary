/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors:{
        "custom-text-bg": "#F3F9FE"
        // "custom-text-bg": "#F6FAFD"
      }
    },
  },
  plugins: [],
}
