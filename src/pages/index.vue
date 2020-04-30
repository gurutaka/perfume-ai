<template>
  <div class="container is-fluid">
    <p class="has-text-centered is-size-5 msg">
      Perfumeの画像をアップロードすると、メンバーを識別してくれるAIアプリです！
    </p>
    <Loading v-if="isLoading"></Loading>
    <div class="tile is-ancestor">
      <div class="tile is-vertical is-7">
        <div class="tile is-parent">
          <article class="tile is-child notification is-light">
            <p class="title">画像</p>
            <img v-show="uploadedImage" :src="uploadedImage" />
          </article>
        </div>
      </div>

      <div class="tile is-parent">
        <article class="tile is-child notification is-primary">
          <div class="content">
            <p class="title">結果</p>
            <div class="content">
              <div v-for="result in results" :key="result.id" class="result">
                <Result :result="result"></Result>
              </div>
            </div>
          </div>
        </article>
      </div>
    </div>

    <div class="notification upload-wrapper has-text-centered">
      <b-field class="is-centered">
        <b-upload v-model="dropFiles" multiple drag-drop accept="image/*">
          <section class="section">
            <div class="content has-text-centered">
              <p>
                <b-icon icon="upload" size="is-large"></b-icon>
              </p>
              <p>画像をアップロードしてね！</p>
              <p>※画像は保存されません。</p>
            </div>
          </section>
        </b-upload>
      </b-field>
    </div>
    <div class="box">
      <p class="has-text-centered is-size-5">
        ※ Perfume以外の画像の場合、特徴が似ているメンバーの確率が表示されます。
        <br />
        <strong>
          頻繁におかしな数字を叩き出しますので、ご注意下さい！！！
        </strong>
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator'
import Compressor from 'compressorjs'
import { ResultItem } from '../models/resultItem'
import Result from '@/components/Result.vue'
import Loading from '@/components/Loading.vue'

@Component({
  components: {
    Loading,
    Result
  }
})
export default class Index extends Vue {
  uploadedImage: string = ''
  isLoading: boolean = false
  base64Type: string = ''
  dropFiles: Array<File> = []
  results: ResultItem[] = []

  head() {
    return {
      titleTemplate: null,
      title: 'Perfume AI画像診断'
    }
  }

  @Watch('dropFiles')
  onUploadFiles(newFiles: Array<File>) {
    if (newFiles.length === 0) return
    this.results = []
    this.compressUploadedImg(newFiles[0])
  }

  postCompressedImg(blob: Blob) {
    const reader = new FileReader()
    reader.readAsDataURL(blob)
    this.isLoading = true
    reader.onload = async (e: any) => {
      this.uploadedImage = e.target.result
      this.base64Type = this.uploadedImage.split(',')[0]
      const body = {
        base_64: this.uploadedImage.split(',')[1]
      }

      const res = await this.$axios.$post(
        process.env.api ? process.env.api : '',
        body
      )
      if (!res.results) {
        this.isLoading = false
        return
      }
      this.uploadedImage = this.base64Type + ',' + res.face_img
      this.results = res.results

      this.results = this.results.map((el) => {
        el.base64 = this.base64Type + ',' + el.base64
        return el
      })
      this.isLoading = false
    }
  }

  // アップロードした画像を圧縮
  compressUploadedImg(file: File) {
    const payload: Compressor.Options = {
      maxWidth: 1000,
      maxHeight: 1000,
      mimeType: 'image/jpeg',
      success: this.postCompressedImg,
      error(err: Error): void {
        alert('アップロードで何かしらのエラーが出ました')
        console.log(err.message)
      }
    }

    new Compressor(file, payload)
    this.dropFiles = []
  }
}
</script>

<style scoped>
.result + .result {
  margin-top: 20px;
}

.notification {
  margin-top: 30px;
}
.upload-wrapper {
  background-color: #fff;
}

.box {
  background-color: rgb(253, 203, 203);
  margin: 30px 0;
}

.msg {
  margin-bottom: 50px;
  padding: 0 20px;
}

@media only screen and (max-device-width: 480px) {
  .is-parent {
    padding: 10px 0px;
  }
}
</style>
