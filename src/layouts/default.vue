<template>
  <div>
    <header class="is-size-1 has-text-centered has-text-weight-bold">
      Perfume 画像診断
    </header>

    <nuxt />
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Perfume AI 診断</strong>
          by
          <a
            href="https://twitter.com/guru_taka"
            target="_blank"
            rel="noopener"
            class="link"
          >
            Gurutaka
          </a>
        </p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
header {
  margin-top: 20px;
  margin-bottom: 20px;
}
footer {
  padding: 20px;
  margin-top: 70px;
  font-weight: bold;
  background-color: rgb(190, 190, 190);
}

.link {
  color: rgb(59, 144, 255);
}

.link:hover {
  color: black;
}
</style>
