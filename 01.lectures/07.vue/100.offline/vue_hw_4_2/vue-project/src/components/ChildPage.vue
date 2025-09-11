<template>
  <div class="child">
    <h3>자식 페이지</h3>
    <p>{{child.name}}</p>
  </div>
</template>

<script setup>
defineProps({child: Object})

</script>


<style scoped>
.child{
  background-color: white;
  width:auto;
  justify-content: center;
  align-items: center;
  border: 1px solid grey;
  margin: 10px;
}


</style>