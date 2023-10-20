import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { icons } from './assets/icons/Icons'
const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')
