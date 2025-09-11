<template>
  <div>

    <p>name: {{ myInfo.name }}</p>
    <p>balance: {{ myInfo.balance }}</p>
    <button @click="balanceUpdate">+</button>
    <hr></hr>
  </div>
  
</template>


<script setup>
const props = defineProps({
  myInfo : Object
})
// console.log(props.myInfo)
const balanceUpdate = function() {
  props.myInfo.balance += 1000
}
</script>

<style scoped></style>
