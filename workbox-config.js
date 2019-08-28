module.exports = {
  globDirectory: "dist/",
  globPatterns: ["**/*.{html,css,jpeg,jpg,js,map,ico,png}"],
  swDest: "dist/sw.js",
  skipWaiting: true,
  clientsClaim: true,
  runtimeCaching: [
    {
      urlPattern: /https:\/\/fonts\.googleapis\.com/,
      handler: "CacheFirst",

      options: {
        cacheName: "google-fonts"
      }
    }
  ],
  maximumFileSizeToCacheInBytes: 7000000
};
