<template>
    <div class="container-fluid" v-if="loaded" >
        <header-component :indicators="summary.header"></header-component>
        <div class="row">
            <div class="col-md-6">
                <mr-products-component :products="summary.mostRequestedProducts.num_details"></mr-products-component>
                
                <product-indicator-component :indicators="summary.getDonatedVsSold.num_details"></product-indicator-component>            
            </div>
            <div class="col-md-6">
                <alerts-component
                  :orders-delivered="summary.ordersOkToday.num_orders"
                  :times-visited="summary.timesVisited.times_visited"
                  :products-without-stock="summary.productsWithoutStock.products_without_stock"
                />
            </div>
            
        </div>
        <div class="row">
            <div class="col-12">
            <div class="card card-primary">
              <div class="card-header">
                <h3 class="card-title">Productos historicamente mas vendidos</h3>
              </div>
              <!-- /.card-header -->
              <div class="card-body">
                
                <div class="row mt-4">
                  <template v-if="this.summary.mostRequestedProductHistoric.length > 0">
                      <div class="col-sm-4 container-to-zoom" v-for="( product, index) in this.summary.mostRequestedProductHistoric" :key="product.id">
                        <div class="position-relative p-3 bg-gray" style="transition: all .5s;height: 180px;" :style="{'background': 'gray url('+product.image+') no-repeat center' }">
                          <div class="ribbon-wrapper ribbon-lg">
                            <div class="ribbon  text-lg" :class="{'bg-warning' : index == 0, 'bg-success' : index == 1, 'bg-primary' : index == 2, }">
                              {{ product.qty__sum }}
                            </div>
                          </div>
                          <div class="w-75 pl-3" style="background-color:rgba(0, 0, 0, 0.7)">
                            <div>
                                {{ product.name }} <br> 
                                <small>Ganancias Obtenidas: $ {{ parseFloat(product.price__sum).toFixed(2) }}</small>
                            </div>
                          </div>
                          
                        </div>
                      </div>                                                           
                  </template>
                  <div v-else class="col-md-12 text-center">
                    <h4 class="text-danger">No tiene productos vendidos</h4>
                  </div>
                  
                  
                </div>
              </div>
              <!-- /.card-body -->
            </div>
            <!-- /.card -->
          </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <pending-orders-component @orderConfirmed="getApi" :orders="summary.getTodayOrdersNotDispatched.orders"></pending-orders-component>       
            </div>
        </div>
    </div>
    
</template>


<script>
import HeaderComponent from './Home/HeaderComponent';
import MostRequestedProductComponent from './Home/CardMostRequestProductComponent';
import ProductIndicatorComponent from './Home/ProductIndicatorComponent';
import AlertsComponent from './Home/AlertsComponent';
import PendingOrdersComponent from './Home/PendingOrdersComponent';

export default {
    mounted(){
        this.getApi();
    },
    components:{
        'header-component'      : HeaderComponent,
        'mr-products-component' : MostRequestedProductComponent,
        'product-indicator-component' : ProductIndicatorComponent,
        'alerts-component'      : AlertsComponent,
        'pending-orders-component'      : PendingOrdersComponent,
        
    },  
    data: function (){
        return {
            'summary' : {},
            'loaded'  : false,
        }
    },
    methods : {
        getApi(){            
            axios.get('administrador/home')
                  .then( resp => {
                      this.summary = resp.data                      
                      this.loaded  = true; 
                  })
        }
    },
}
</script>

<style scoped>
    .container-to-zoom:hover .position-relative,
    .container-to-zoom:focus .position-relative {
        transform: scale(1.05);
    }
</style>