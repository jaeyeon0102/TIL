<template>
  <div>
    <h1>조건문 연습하기</h1>

    <!-- 기본이 false -->
    <button @click="isSeen =!isSeen">Login/Logout</button>


    <template v-if="isSeen">
      <div>userName : admin</div>
      <div>isAdmin : true</div>
      <div>passWord : 1q2w3e4r</div>
    </template>

  </div>

</template>

<script setup>
  import { ref } from 'vue'

  const isSeen = ref(false)


</script>

<style scoped>

</style>