<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <h3>{{ route.params.name }}</h3>

    <div v-if="userInfo">
      <p>이름 : {{ userInfo.name }}</p>
      <p>잔고 : {{ userInfo.balance }}</p>
      <button @click="onClick">+</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { useBalanceStore } from '@/stores/balance';

const route = useRoute()
const store = useBalanceStore()

const userInfo = computed(() => {
  return store.getBalanceByName(route.params.name)
})

const onClick = () => {
  store.increaseBalance(route.params.name)
}
</script>

<style scoped>

</style>