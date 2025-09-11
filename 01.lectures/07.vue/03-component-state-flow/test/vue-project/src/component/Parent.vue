<template>
  <section>
    <h1>Parent</h1>
    <ParentChild 
    my-msg="message"
    :my-balance="balance"/>

    <ParentItem 
      v-for="info in children"
      :key = "info.name"
      :my-info="info"
    />
  </section>
  
</template>


<script setup>
import ParentChild from './ParentChild.vue';
import {ref} from 'vue'
import ParentItem from './ParentItem.vue';


const balance = ref(10000)
const children = ref([
  {name: 'Alice', balance: 1000},
  {name: 'Bella', balance: 10000},
  {name: 'Chalie', balance: 100000},
])
</script>

<style scoped></style>
