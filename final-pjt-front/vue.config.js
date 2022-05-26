const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  css : {
    loaderOptions : {
      sass : {
        sassOption: `
          @import "@/assets/scss/abstracts/abstracts.scss";
        `
      }
    }
  }
})
