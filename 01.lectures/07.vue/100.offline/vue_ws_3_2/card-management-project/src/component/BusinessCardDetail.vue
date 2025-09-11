<template>
  <div class="card">
    <p class="border">이름: {{ person.name }}</p>
    <p>타이틀: {{ person.title }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  person: {
    type: Object,
    required: true,
  },
})



</script>

<style scoped>

.card{
  background-color: rgb(244, 242, 242);
  border: 1px solid grey;
  display: flex;
  flex-direction: column;
  width: 400px;
  height: 120px;
  margin: 10px;
  justify-content: center;
  align-items: center;
}

.border{
  font-weight: bold;
}

</style>