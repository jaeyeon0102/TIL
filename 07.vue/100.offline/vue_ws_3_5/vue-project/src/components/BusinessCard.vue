<template>
  <p>이름 <input></input>  직함 <input></input>  <button>명함 추가</button></p>
  <p>{{ cardMsg }}</p>
  <div class="card-container">
    <BusinessCardDetail 
     v-for = "card in businessCards"
     :key=" card.name"
     :person="card"
     @delete-card-func="deleteCard"
     />
  </div>
</template>

<script setup>
import { ref , computed} from "vue"
import BusinessCardDetail from "./BusinessCardDetail.vue";


const businessCards = ref([
  {name: '일론 머스크', title: '테슬라 테크노킹'},
  {name: '래리 엘리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'},
])

const cardNum = computed(() => businessCards.value.length)

const cardMsg = computed(() => {
  return cardNum.value === 0 ? '명함이 없습니다. 새로운 명함을 추가해 주세요' : `현재 보유 중인 명함 개수 : ${cardNum.value}`
})

function deleteCard(person){
  businessCards.value = businessCards.value.filter(card => card !== person)
}
</script>

<style scoped>
.card-container{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

p{
  text-align: center;
}

input{
  border: 1px solid blue;
  width: 250px;
  height: 30px;
  border-radius: 8px;
}

button{
  border: 1px solid blue;
  width: 80px;
  height: 35px;
  border-radius: 8px;
  background-color: whitesmoke;
}

</style>