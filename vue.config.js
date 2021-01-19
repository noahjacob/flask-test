module.exports = {
  outputDir: "./dist",
  assetsDir: "static",
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: {
      '^/':
      {
        target: 'http://localhost:5000/',
        changeOrigin: true
      },
    }
  }


}