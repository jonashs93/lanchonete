<template>
  <div id="app">
    <div class="container p-5">
      <header>
        <h1>Novo Pedido</h1>
      </header>

      <b-form @submit="onSubmit" v-if="show">
        <b-form-group id="input-group-3" label="Lanche:" label-for="input-3">
          <b-form-select
            id="input-3"
            v-model="form.lanche"
            :options="lanchesOptions"
            value-field="id"
            text-field="nome"
            @change="setIngredientes"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-3" label="Ingredientes:" label-for="input-3">
          <b-form-select v-model="form.ingredientes" :options="ingredientesOptions" value-field="id" text-field="nome" multiple @change="calcPrice"></b-form-select>
        </b-form-group>
      </b-form>

      <p> Valor do Lanche: {{ this.valorLanche | currency }}</p>
      <b-button variant="outline-primary" @click="addLanche">Adicionar Lanche</b-button>

      <p> Valor Total do Pedido: {{ this.valorTotalPedido | currency }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'app',
  data () {
    return {
      form: {
        lanche: null,
        ingredientes: []
      },
      lanchesOptions: [],
      ingredientesOptions: [],
      cesta: [],
      valorLanche: 0.0,
      valorTotalPedido: 0.0,
      show: true
    }
  },

  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
    },

    resetForm () {
      // Reset our form values
      this.form.lanche = null
      this.form.ingredientes = []
      this.valorLanche = 0.0
      // Trick to reset/clear native browser form validation state
      this.show = true
      // this.$nextTick(() => {
      //   this.show = true
      // })
    },

    setIngredientes () {
      let lancheSelected = this.lanchesOptions.find(lanche => lanche.id === this.form.lanche)
      this.form.ingredientes = lancheSelected.ingredientes
      this.calcPrice()
    },

    calcPrice () {
      this.valorLanche = 0.0
      this.form.ingredientes.forEach((ingredienteId, index) => {
        let ingredienteSelected = this.ingredientesOptions.find(ingrediente => ingrediente.id === ingredienteId)
        this.valorLanche += parseFloat(ingredienteSelected.valor)
      })
    },

    addLanche () {
      let itemObject = {'lancheId': this.form.lanche, 'ingredientesIds': this.form.ingredientes, 'valor': this.valorLanche}
      this.cesta.push(itemObject)
      this.calcTotalPrice()
      this.calcDiscount()
      this.resetForm()
    },

    calcTotalPrice () {
      this.valorTotalPedido = 0.0
      this.cesta.forEach((item, index) => {
        item.ingredientesIds.forEach((ingredienteId, index) => {
          let ingredienteSelected = this.findIngrediente(ingredienteId)
          this.valorTotalPedido += parseFloat(ingredienteSelected.valor)
        })
      })
    },

    calcDiscount () {
      this.lightPromotion()
      this.meatPromotion()
      this.cheesePromotion()
    },

    lightPromotion () {
      let hasAlface = false
      let hasBacon = false
      this.cesta.forEach((item, index) => {
        item.ingredientesIds.forEach((ingredienteId, index) => {
          let ingredienteSelected = this.findIngrediente(ingredienteId)
          if (ingredienteSelected.alias === 'alface') {
            hasAlface = true
          } else if (ingredienteSelected.alias === 'bacon') {
            hasBacon = true
          }
        })

        if (hasAlface && !hasBacon) {
          let discount = item.valor / 10
          this.valorTotalPedido -= discount
        }
      })
    },

    meatPromotion () {
      this.promotionTake3Pay2('hamburguer_carne')
    },

    cheesePromotion () {
      this.promotionTake3Pay2('queijo')
    },

    promotionTake3Pay2 (ingredienteType) {
      let price = 0
      let qntItem = 0
      this.cesta.forEach((item, index) => {
        item.ingredientesIds.forEach((ingredienteId, index) => {
          let ingredienteSelected = this.findIngrediente(ingredienteId)
          if (ingredienteSelected.alias === ingredienteType) {
            qntItem += 1
            price = ingredienteSelected.valor
          }
        })
      })

      if (qntItem >= 3) {
        let qntDiscount = Math.floor(qntItem / 3)
        let discount = qntDiscount * price

        this.valorTotalPedido -= discount
      }
    },

    async fetchLanchesOptions () {
      axios.get(`http://127.0.0.1:8000/lanches/`)
        .then(response => {
          this.lanchesOptions = response.data
        })
        .catch(e => console.log(e))
    },

    async fetchIngredientesOptions () {
      axios.get(`http://127.0.0.1:8000/ingredientes/`)
        .then(response => {
          this.ingredientesOptions = response.data
        })
        .catch(e => console.log(e))
    },

    findIngrediente (ingredienteId) {
      let ingrediente = this.ingredientesOptions.find(ingrediente => ingrediente.id === ingredienteId)
      return ingrediente
    }
  },

  created () {
    this.fetchLanchesOptions()
    this.fetchIngredientesOptions()
  }
}
</script>
