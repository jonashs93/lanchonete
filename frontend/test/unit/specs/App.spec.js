import Vue from 'vue'
import App from '@/components/App'
import { shallowMount, createLocalVue, mount } from '@vue/test-utils'
import BootstrapVue from 'bootstrap-vue'
import Vue2Filters from 'vue2-filters'
import IngredienteFactory from '../factories/ingredienteFactory'

Vue.use(BootstrapVue)
Vue.use(Vue2Filters)

const localVue = createLocalVue()

localVue.use(BootstrapVue)
localVue.use(Vue2Filters)


describe('App.vue', () => {
  let ingredientePromotion = new IngredienteFactory()
  let ingredientes = [ingredientePromotion, new IngredienteFactory(), new IngredienteFactory(), new IngredienteFactory(), new IngredienteFactory()]
  let ingredientesIds = ingredientes.map(ingrediente => ingrediente.id)
  const wrapper = shallowMount(App, {
    data: function() {
      return {
        form: {
          lanche: 1,
          ingredientes: ingredientesIds
        },
        ingredientesOptions: ingredientes
      }
    }
  })
  const vm = wrapper.vm
  vm.calcPrice()

  let itemObject = {'lancheId': vm.form.lanche, 'ingredientesIds': ingredientesIds, 'valor': vm.valorLanche}
  vm.cesta.push(itemObject)
  vm.cesta.push(itemObject)
  vm.cesta.push(itemObject)
  vm.calcTotalPrice()
  let valorSemDesconto = vm.valorTotalPedido

  it('should render correct contents', () => {
    expect(vm.$el.querySelector('header h1').textContent)
      .toEqual('Novo Pedido')
  })

  it('should calculate sandwich price', () => {
    let price = ingredientes.reduce((prev, ingrediente) => prev + ingrediente.valor, 0)
    expect(vm.valorLanche).toEqual(price)
  })

  it('should calculate light promotion', () => {
    vm.calcTotalPrice()
    ingredientePromotion.alias = 'alface'
    vm.lightPromotion()

    let valorComDesconto = valorSemDesconto - ((vm.valorLanche / 10) * vm.cesta.length)
    expect(Math.round(vm.valorTotalPedido)).toEqual(Math.round(valorComDesconto))
  })

  it('should calculate meat promotion', () => {
      vm.calcTotalPrice()
      ingredientePromotion.alias = 'hamburguer_carne'
      vm.meatPromotion()

      let valorComDesconto = valorSemDesconto - (ingredientePromotion.valor *  Math.floor(vm.cesta.length / 3))
      expect(vm.valorTotalPedido).toEqual(valorComDesconto)
  })

  it('should calculate cheese promotion', () => {
    vm.calcTotalPrice()
    ingredientePromotion.alias = 'queijo'
    vm.cheesePromotion()

    let valorComDesconto = valorSemDesconto - (ingredientePromotion.valor *  Math.floor(vm.cesta.length / 3))
    expect(vm.valorTotalPedido).toEqual(valorComDesconto)
  })
})
