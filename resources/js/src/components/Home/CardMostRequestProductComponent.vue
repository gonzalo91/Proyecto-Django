<template>
    <div class="card">
        <div class="card-header">
            <h3 class="card-title bold">Productos Mas Solicitados Esta Semana</h3>
        </div>
        <!-- /.card-header -->
        <div class="card-body p-0">
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th style="width: 10px">#</th>
                        <th>Medicamento</th>                        
                        <th>Productos Vendidos</th>                        
                        <th style="width: 40px">Stock</th>
                    </tr>
                </thead>
                <tbody>
                    <template v-if="products.length > 0">
                        <tr v-for="(product, index) of products" :key="product.id">
                            <td>{{ index + 1 }}</td>
                            <td>{{ product.name }}</td>                        
                            <td>{{ product.dcount }}</td>    
                            <td><span class="badge bg-danger">{{ product.product__stock }}</span></td>
                        </tr>                                                    
                    </template>
                    <tr v-else >
                        <td colspan="4" class="text-center">
                            No Tiene productos venidos para esta semana
                        </td>

                    </tr>                                                    

                    
                    
                </tbody>
            </table>
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
        'products' : Array
    }
}
</script>

<style scoped>
    
</style>