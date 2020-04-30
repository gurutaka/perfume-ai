<template>
  <div>
    <p class="has-text-centered has-text-weight-bold is-size-4">
      {{ ResultTxt }}
    </p>
    <div class="field is-grouped">
      <div class="control">
        <figure class="image is-128x128">
          <img :src="result.base64" />
        </figure>
      </div>
      <div class="control">
        <ul>
          <li v-for="member in members" :key="member.id">
            {{ member }}：{{ result[member] }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { ResultItem } from '../models/resultItem'

@Component
export default class Result extends Vue {
  members: Array<String> = ['あーちゃん', 'のっち', 'かしゆか']
  @Prop({
    default: {}
  })
  result!: ResultItem

  get ResultTxt() {
    const maxProbability = Math.max(
      ...Object.values(this.result).filter((el) => typeof el === 'number')
    ) as Number

    const predictMember = Object.keys(this.result)[
      Object.values(this.result).indexOf(maxProbability)
    ]

    switch (true) {
      // const prob = this.maxProbability.
      case maxProbability === 100:
        return `${predictMember}100%！`
      case maxProbability >= 95:
        return `${maxProbability.toString()}%：圧倒的${predictMember}！`
      case maxProbability >= 90:
        return `${maxProbability.toString()}%：${predictMember}の可能性大！`
      case maxProbability >= 80:
        return `${maxProbability.toString()}%：多分${predictMember}！`
      case maxProbability >= 70:
        return `${maxProbability.toString()}%：${predictMember}かも！`
      default:
        return `perfumeじゃないかも…`
    }
  }
}
</script>
