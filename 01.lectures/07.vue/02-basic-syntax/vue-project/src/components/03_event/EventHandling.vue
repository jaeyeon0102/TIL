<template>
  <div>
    <!-- Inline Handlers -->
    <!-- <button @click="count++">Add 1</button> -->
    <button @click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @click="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <button @click="greeting('hello')">Say hello</button>
    <button @click="greeting('bye')">Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <button @click="warning('경고입니다.', $event)">Submit</button>

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">...</form>
    <a @click.stop.prevent="onLink">...</a>

    <!-- key modifiers -->
    <!-- 키보드를 사람이 눌렀다. -> keydown
     눌렀다 뗐다 -> keyup
     누르고 있다 -> keypress-->
    <input @keyup.enter="onSubmit">
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  // 변동사항 만들고 싶을 때 ref 사용
  const count = ref(0)

  const name = ref('Alice')
  const myFunc = function (event) {
    console.log(event)
    console.log(event.currentTarget)
    console.log(`Hello ${name.value}!`)
  }

  const greeting = function (message) {
    console.log(message)
    // console.log(event)  --> 인자만 전달했기 때문 @click="greeting('bye') 부분
  }
  
  const warning = function (message, event) {
    console.log(message)
    console.log(event)
    // event 쓰려면 $event 사용하기
  }
</script>

<style scoped>

</style>