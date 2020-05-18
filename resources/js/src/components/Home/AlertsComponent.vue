<template>
    <div class="card card-default">
        <div class="card-header">
            <h3 class="card-title">
            <i class="fas fa-bullhorn"></i>
                Alertas
            </h3>
        </div>
        <!-- /.card-header -->
        <div class="card-body">
            <div class="callout callout-danger" v-if="this.productsWithoutStock.length > 0">
                <h5>No tiene stock de los siguientes productos:</h5>
                <p>
                    <ol>
                        <li v-for="product in this.productsWithoutStock" :key="product.id">{{ product.name }}</li>
                    </ol>
                </p>
            </div>
            <div class="callout callout-success" v-else>
                <h5>Felicidades, no tiene productos sin stock</h5>                
            </div>
            <div class="callout callout-info">
                <h5>Han visto su pagina:</h5>

                <p>{{ this.timesVisited }} veces</p>
            </div>                        
            <div class="callout callout-success">
                <h5>Hoy has entregado:</h5>
                <p>{{ this.ordersDelivered }} pedido(s)</p>
            </div>
            <blockquote class="quote-secondary">
                <p>Recuerda mantener siempre actualizado tu stock!</p>                        
                <small>Zalo</small>
            </blockquote>
        </div>
        <!-- /.card-body -->
    </div>
</template>


<script>
export default {
    data: function (){
        return {
            'foo' : 'bar',
        }
    },
    props:{
        'ordersDelivered' : Number,
        'timesVisited'    : Number,
        'productsWithoutStock' : Array,
    }
}
</script>

<style scoped>
    
</style>