<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/questions">Manage Questions</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  background-color: #fe001a; /* Coca-Cola Red */
  padding: 10px 0;
}

nav {
  display: flex;
  justify-content: center;
  gap: 20px;
}

a {
  color: white; /* White color text */
  text-decoration: none;
  font-size: 18px;
  font-weight: bold;
}

a:hover {
  color: black; /* Hover color black */
  text-decoration: underline;
}
</style>
