// tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'cyan-line-a': '#04ACDF',
        'red-line-b': '#EE1B2E',
        'blue-line-c': '#0168B3',
        'green-line-d': '#008067',
        'purple-line-e': '#6D227F',
        'blue-walking': '#37A0FF',
      },
    },
  },
  safelist: [
    'bg-cyan-line-a',
    'bg-red-line-b',
    'bg-blue-line-c',
    'bg-green-line-d',
    'bg-purple-line-e',
    'bg-blue-walking'
  ],
  plugins: [],
}
