<template>
  <div>
    <!-- template syntax -->
    <p>Message: {{ msg }}</p>
    <!-- html 문법 자체를 보여주는 것. 실제 HTML 출력 시 v-html 사용
     절대 클라이언트(사용자)가 입력한 값을 할당하면 안됨-->
    <div v-html="rawHtml"></div>
    <!-- v-bind : 넣고 싶은 바인딩 값을 데려오기,,-->
    <div v-bind:id="dynamicId"></div>
    {{ number + 1 }}
    {{ ok ? 'YES' : 'NO' }}
    {{ msg.split('').reverse().join('') }}

    <!-- directive -->
    <div v-bind:id="`list-${id}`"></div>
    <p v-if="seen">Hi there</p>
    <a v-bind:href="myUrl">Link</a>
    <button v-on:click="doSomething">button</button>
    <!-- prevent로 인해 제출 버튼을 눌러도 변화 없음.-->
    <form v-on:submit.prevent="onSubmit">
      <input type="submit">
    </form>
  </div>
</template>

<script setup> 
  import { ref } from 'vue'
  
  const msg = 'Hello' //template의 msg 부분에 보여지게 됨
  const rawHtml = ref('<span style="color:red">This should be red.</span>')
  const dynamicId = ref('my-id')
  const number = ref(1)   //number의 숫자가 반응형으로 변동
  const ok = ref(true)
  const seen = ref(true)
  const id = ref(100)
  const myUrl = 'https://www.google.co.kr/'

  const doSomething = function () {
    console.log('button clicked')
  }
  const onSubmit = function () {
    console.log('form submitted')
  }
</script>

<style scoped>

</style>