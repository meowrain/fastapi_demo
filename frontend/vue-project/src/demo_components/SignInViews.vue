<template>
  <div>
    <form @submit.prevent="submitMethod">
      <div>
        <label for="username">Username: </label>
        <input type="text" id="username" v-model="username" />
      </div>

      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" />
      </div>

      <button type="submit">Submit</button>
    </form>

    <p>{{ responseData.data }}</p>
  </div>
</template>

<script setup lang="js">
import { ref } from 'vue'
import axios from 'axios'
const username = ref('')
const password = ref('')
const responseData = ref('')
async function submitMethod() {
  console.log('Username:', username.value)
  console.log('Password:', password.value)
  try {
    const response = await axios.post('http://127.0.0.1:8000/signin', {
      username: username.value,
      password: password.value
    })
    responseData.value = response
  } catch (err) {
    responseData.value = err
  }
}
</script>

<style scoped></style>
