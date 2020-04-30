export default {
  mode: 'universal',
  srcDir: 'src/',
  /*
   ** Headers of the page
   */
  head: {
    htmlAttrs: {
      prefix: 'og: http://ogp.me/ns#'
    },
    title: 'Perfume AI画像診断',
    meta: [
      { charset: 'utf-8' },
      { 'http-equiv': 'X-UA-Compatible', content: 'IE=edge' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content:
          'Perfumeの画像をアップロードすると、のっち、あーちゃん、かしゆかを識別してくれるAIアプリです。'
      },
      {
        hid: 'description',
        name: 'description',
        content:
          'Perfumeの画像をアップロードすると、のっち、あーちゃん、かしゆかを識別してくれるAIアプリです。'
      },
      {
        hid: 'og:site_name',
        property: 'og:site_name',
        content: 'Perfume AI画像診断'
      },
      { hid: 'og:type', property: 'og:type', content: 'website' },
      {
        hid: 'og:url',
        property: 'og:url',
        content: 'https://perfume-ai.kikagaku.net/'
      },
      { hid: 'og:title', property: 'og:title', content: 'Perfume AI画像診断' },
      {
        hid: 'og:description',
        property: 'og:description',
        content:
          'Perfumeの画像をアップロードすると、のっち、あーちゃん、かしゆかを識別してくれるAIアプリです。'
      },
      { property: 'og:locale', content: 'ja_JP' },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://perfume-ai.kikagaku.net/ogp.png'
      },
      { property: 'fb:app_id', content: '630354674303647' },
      { name: 'twitter:card', content: 'summary_large_image' }
    ],
    link: [
      {
        rel: 'icon',
        type: 'image/x-icon',
        href: '/favicon.ico'
      }
    ]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['~/assets/css/buefy.scss'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: ['@nuxt/typescript-build', '@nuxt/typescript-build'],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
    '@nuxtjs/axios',
    [
      'nuxt-buefy',
      {
        css: false
      }
    ],
    [
      '@nuxtjs/google-gtag',
      {
        id: 'UA-165057486-1'
      }
    ]
  ],
  /*
   ** Build configuration
   */
  generate: {
    dir: 'docs'
  },
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
  // router: {
  //   base: '/perfume_classification/'
  // }
}
