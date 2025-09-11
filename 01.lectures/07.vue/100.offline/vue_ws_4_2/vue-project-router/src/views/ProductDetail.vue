<template>
  <div class="item">
      <h3>{{ product.name }}</h3>
      <p>{{ product.price }}</p>
      <img :src="product.imagePath" :alt="product.name">
  </div>
</template>

<script setup>
defineProps({
  product: Object
})

</script>

<style scoped>
.item {
  width: 200px;
  margin: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  text-align: center;
}

img {
  width: 100%;
  height: auto;
  object-fit: cover;
}
</style>