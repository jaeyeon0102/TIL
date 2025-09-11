<template>
  <div class="parent-box">
  <h1>부모 페이지입니다.</h1>
  <ChildPage
  v-for="child in children"
  :name = "child.name"
  :age = "child.age"
/>
  </div>
</template>

<script setup>
import {ref} from "vue"
import ChildPage from './ChildPage.vue';

const children = ref([
  {name: '김하나', age: 30},
  {name: '김두리', age: 20},
  {name: '김서이', age: 10}
])


</script>

<style scoped>
.parent-box{
  border: 1px solid black;
  margin: 5px;
}

</style>