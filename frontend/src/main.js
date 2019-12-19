import Vue from 'vue'
import App from './components/App.vue'
import BootstrapVue from 'bootstrap-vue'
import Vue2Filters from 'vue2-filters'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

var Vue2FiltersConfig = {
  currency: {
    symbol: 'R$',
    decimalDigits: 2,
    thousandsSeparator: '.',
    decimalSeparator: ',',
    spaceBetweenAmountAndSymbol: true
  }
}

Vue.use(Vue2Filters, Vue2FiltersConfig)

new Vue({
  el: '#app',
  render: h => h(App)
})
