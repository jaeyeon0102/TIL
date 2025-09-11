<template>
  <article>
    <h3>Parent Child</h3>
    <p>{{ myMsg }}</p>
    <p>{{ myBalance }}</p>

  </article>
</template>

<script setup>
defineProps({
  myMsg: String,
  myBalance: Number
})

</script>

<style scoped>

</style>
