<script setup>
import { RouterView } from 'vue-router'
import NavBarComponent from './components/NavBarComponent.vue'
</script>

<template>
  <header>
    <NavBarComponent></NavBarComponent>
  </header>

  <RouterView />
</template>

<style scoped></style>
