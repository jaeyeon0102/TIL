<template>
  
  <div>
    <h2>메인 페이지</h2>
    <MainPage 
     v-for="balance in balanceStore.balances"
     :key="balance.name"
     :balance="balance"/>
  </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
import { useBalanceStore } from '@/stores/balance';

const balanceStore = useBalanceStore()

</script>

<style scoped>
div{
  margin: 20px;
}

</style>