<template>
  <div class="parent">
    <div>
      <h2>부모 컴포넌트</h2>
      <p>{{family.familyName}}</p>
      <p>{{family.father}}</p>
      <p>{{family.mother}}</p>
    </div>
    <ChildPage 
      v-for="child in family.children"
      :key="child.name"
      :child="child"/>
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';

defineProps({family: Object})

</script>

<style scoped>
.parent{
  border: 1px solid grey;
  text-align: center;
  justify-content: center;
  align-items: center;
  background-color: whitesmoke;
  margin: 5px;
}

</style>