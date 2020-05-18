<template>
    <div class="row">
        <div class="col-lg-3 col-6">        
            <div class="small-box bg-info">
                <div class="inner">
                <h3>{{ indicators.new_orders }}</h3>

                <p>Nuevos Pedidos</p>
                </div>
                <div class="icon">
                <i class="ion ion-bag"></i>
                </div>            
            </div>
        </div>
        <div class="col-lg-3 col-6">        
            <div class="small-box bg-warning">
                <div class="inner">
                <h3>{{ indicators.pending_orders }}</h3>

                <p>Pedidos Pendientes</p>
                </div>
                <div class="icon">
                    <i class="ion ion-ios-reload"></i>
                </div>
                
            </div>
        </div>        
        <div class="col-lg-3 col-6">        
            <div class="small-box bg-success">
                <div class="inner">
                <h3>{{ indicators.delivered_products }}</h3>

                <p>Productos Entregados</p>
                </div>
                <div class="icon">
                    <i class="ion ion-android-send"></i>
                </div>            
            </div>
        </div>

                
        <div class="col-lg-3 col-6">        
            <div class="small-box bg-light">
                <div class="inner">
                <h3>{{ indicators.new_products }}</h3>

                <p>Nuevos Productos</p>
                </div>
                <div class="icon">
                <i class="ion ion-android-add"></i>
                </div>            
            </div>
        </div>    
    </div>
</template>


<script>
export default {
    data: function (){
        return {
            'foo' : 'bar',
        }
    },
    props :{
        indicators : Object,
    }
}
</script>

<style scoped>
    
</style>