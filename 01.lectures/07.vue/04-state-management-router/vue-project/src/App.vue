<template>
  <div>
    <p> {{ counterStore.count }}</p>
    <p> {{ counterStore.doubleCount }}</p>
    <button @click="onClick">+</button>
  </div>
</template>

<script setup>
import {useCounterStore} from '@/stores/counter'
const counterStore = useCounterStore()
console.log(counterStore)

</script>

<style scoped>

</style>