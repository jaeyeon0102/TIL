<template>
  <div class="child-box">
    <h3>자식 페이지입니다.</h3>
    <p> 이름: {{ name }}</p>
    <p> 나이: {{ age }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  name: String,
  age: Number
})

</script>

<style scoped>
.child-box{
  border: 1px solid black;
  padding: 10px;
  margin-bottom: 10px;
  margin: 10px;

}


</style>