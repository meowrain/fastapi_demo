<script setup>
import { RouterLink, RouterView } from 'vue-router'
import SignInViews from './views/SignInViews.vue';
import DemoView from './views/DemoView.vue';
</script>

<template>
  <header>

    <div class="wrapper">
      <!-- <HelloWorld msg="You did it!" /> -->
      <!-- <SignInViews /> -->
      <DemoView></DemoView>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
