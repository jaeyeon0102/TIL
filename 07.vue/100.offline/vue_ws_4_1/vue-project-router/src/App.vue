<script setup>

</script>

<template>
  <nav>
    <p>
      <router-link to="/">Home</router-link>
    </p>
    <p>
      <router-link to="/products">Products</router-link>
    </p>
    <p>
      <router-link to="/favorite">Favorite</router-link>
    </p>
  </nav>
  <main>

    <RouterView />
  </main>
</template>

<style scoped>
nav{
  background-color: gray;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  color: white;

}
p a{
  margin: 15px;
  color: inherit;
  text-decoration: none;
}
</style>
