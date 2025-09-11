<script setup>
import BusinessCard from './component/BusinessCard.vue';

</script>

<template>
  <body>
    <header>
      <h1>명함 관리 페이지</h1>
    </header>
    
    <main>
      <article>
        <p class="center">명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
        <h3 class="center">보유 명함 목록</h3>
        <div> 
          <BusinessCard />
        </div>
      </article>
    </main>
    
    <footer>
      <p>2023 My Business Cards</p>
    </footer>

  </body>

</template>

<style scoped>
body{
  display: flex;
  flex-direction: column;   /* 위→아래 정렬 */
  justify-content: center;
  align-items: center;
  margin: 0;
  min-height: 100vh; 
}
header{
  background-color: blue;
  color: white;
  width: 300px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
}
main{
  flex: 1;
  display: flex;
  justify-content: center;
  /* align-items: center; */
}

footer{
  background-color: lightgrey;
  height: 60px;
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}
.center{
  text-align: center;
}



</style>
