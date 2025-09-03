<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p> 이름: {{ person.name }}</p>
    <p> 나이: {{ person.age }}</p>
    <p> 용돈: {{ person.balance }}</p>
    <button @click="$emit('giveMeAllowance',person)">용돈 주세요</button>
  </div>
</template>

<script setup>
const props = defineProps({
  person: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['giveMeAllowance'])

</script>

<style scoped>

</style>