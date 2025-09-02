<template>
  <h1>글꼴 테스트기</h1>

  <div v-for="font in fonts" :key="font.style" >
    <label>{{ font.style }}</label>

    <div>
      <input v-model="font.text"/>
    </div>

    <div v-if="font.text" :style="{ fontFamily: font.style}">
      {{ font.text }}
    </div>
  </div>
</template>

<script setup>
  import {ref} from "vue"

  const fonts = ref([
    {style: "바탕", text: null},
    {style: "휴먼엽서체", text: null},
    {style: "궁서체", text: null}
  ])

</script>

<style scoped>



</style>