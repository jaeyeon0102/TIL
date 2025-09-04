import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', ()=>{
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
    },
    {
      name: '김두리',
      balance: 10000
    },
    {
      name: '김서이',
      balance: 100
    },
    
  ])
  const getBalanceByName = computed(() => {
    return (name) => {
      return balances.value.find(balance => balance.name === name)
    }
  })

  const increaseBalance = (name) => {
    const userInfo = balances.value.find(balance => balance.name === name)

    if (userInfo){
      userInfo.balance += 1000
    }
  }

  return {balances, getBalanceByName, increaseBalance }
})