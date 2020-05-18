<template>
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Indicadores de Productos</h3>
        </div>
        <!-- /.card-header -->
        <div class="card-body">
            <template v-if="this.indicators.length > 0">
                <template v-if="this.donated !== undefined">
                    <h5>Productos Donados <strong>({{ this.donated.qty }})</strong></h5>
                    <div class="progress mb-3">
                        <div class="progress-bar bg-success" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" :style="{ 'width' : this.donated.qty / this.total * 100 + '%'}">
                            <span class="sr-only">20% Complete</span>
                        </div>
                    </div>
                </template>
                <h5 class="text-danger" v-else>No ha donado Productos</h5>
                <template v-if="this.sold !== undefined">
                    <h5>Productos Vendidos <strong>({{ this.sold.qty }})</strong></h5>
                    <div class="progress mb-3">
                        <div class="progress-bar bg-info" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" :style="{ 'width' : this.sold.qty / this.total * 100 + '%'}" >
                            <span class="sr-only">80% Complete</span>
                        </div>
                    </div>    
                </template>    
                <h5 class="text-danger" v-else>No ha vendido Productos</h5>

                
            </template>
            <h5 v-else>No Tiene productos venidos aun</h5>
            
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
    props:{
        'indicators' : Array
    },
    computed:{
        donated(){
            return this.indicators.find((indicator) => indicator.donated == true );
        },
        sold(){ 
            return this.indicators.find((indicator) => indicator.donated == false );
        },
        total(){
            return this.indicators.reduce(( (sum, indicator  ) => sum + parseFloat(indicator.qty) ), 0);
        }

    },
}
</script>

<style scoped>
    p {
        color:red;
    }
</style>