<template>
  <div>
    <h1>상품 목록 페이지</h1>
    <div class="container">

      <ProductDetail 
      v-for="item in productStore.favoriteProducts"
      :key="item.name"
      :product="item"
      />
    </div>
  </div>
</template>

<script setup>
import ProductDetail from './ProductDetail.vue';
import { useProductStore } from '@/stores/products';

const productStore = useProductStore()
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
}


</style>