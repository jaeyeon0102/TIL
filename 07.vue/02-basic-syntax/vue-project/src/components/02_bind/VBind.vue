<template>
  <div>
    <!-- v-bind의 경우 앞에 :만 붙여도 상관없음
    v-bind는 진짜 자주 쓰기 때문-->
    <img :src="imageSrc">
    <a :href="myUrl">Move to url</a>
    <!-- dynamicattr : [] 사용 -> 배열을 의미하는게 아닌 key-value 쌍 
     [key] = "value"-->
    <p :[dynamicattr]="dynamicValue">Dynamic Attr</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const imageSrc = ref('https://picsum.photos/200')
  const myUrl = ref('https://www.google.co.kr/')
  const dynamicattr = ref('title')
  const dynamicValue = ref('Hello Vue.js')
</script>

<style scoped>

</style>