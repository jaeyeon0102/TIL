<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav>
    <RouterLink to="/">Main</RouterLink>
  </nav>
  <header>
    <h1>pinia + router 연습하기</h1>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #eee;
}

</style>
