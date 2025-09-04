<template>
  <div>
    <h3>이름: {{ balance.name }}</h3>
    <p>{{ balance.balance }}</p>
    <button @click="goToUpdate">UpdateButton</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const props = defineProps({
  balance: Object
})

const router = useRouter()

const goToUpdate = () => {
  router.push({
    name: 'update',
    params: {name:props.balance.name}
  })
}
</script>

<style scoped>


</style>