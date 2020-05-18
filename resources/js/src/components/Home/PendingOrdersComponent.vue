<template>
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Pedidos Por Atender</h3>

            
        </div>
        <!-- /.card-header -->
        <div class="card-body table-responsive p-0" style="height: auto;">
            <table class="table table-head-fixed text-nowrap">
            <thead>
                <tr>
                <th>ID</th>
                <th>Cliente</th>
                <th>Monto ($)</th>
                <th>Estatus</th>
                <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <template v-if="orders.length > 0">
                    <tr  v-for="(order, index) in orders" :key="order.id" >
                        <td>{{ order.order__id }}</td>
                        <td>{{ order.order__user__username }}</td>
                        <td>{{ parseFloat(order.amount).toFixed(2) }}</td>
                        <td><span class="tag tag-success">Por entregar</span></td>
                        <td>
                            <button 
                                @click="message({'order': order, 'title' : '¿Ya se ha entregado el pedido?', 'index' : index},confirm)" 
                                title="Pedido Completado" 
                                class="btn btn-success btn-rounded mr-2">
                                <i class="ion ion-android-checkmark-circle"></i>
                            </button>
                            /  
                            <button 
                                @click="message({'order': order, 'title' : '¿Esta seguro de cancelar el pedido?', 'index' : index},cancel)" 
                                class="btn btn-danger btn-rounded ml-2" title="Cancelar Pedido">
                                    <i class="ion ion-android-close"></i>
                            </button>
                        </td>
                    </tr>     
                </template>                 
                <tr v-else class="text-center">
                    <td colspan="5"> No Tiene ordenes Para hoy</td>    
                </tr>                                  
            </tbody>
            </table>
        </div>
        <!-- /.card-body -->                    
    </div>
</template>


<script>

export default {
    mounted(){
        
    },  
    data: function (){
        return {
            'foo' : 'bar',
        }
    },
    methods:{     
        message({title, order, index}, callback){
            swal.fire({
                title: title,        
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Si!'
            }).then((result) => {
                if (result.value) {
                    callback(order);
                }
            })
        },
        confirm(order, index){
            var params = new URLSearchParams();
            params.append('order_id', order.order__id);
            params.append('action', 'confirm');

            axios.post('administrador/action_order',  params).then( _ => {
                swal.fire(
                    'Bien!',
                    'Orden Confirmada',
                    'success'
                )
                this.orders.splice(index, 1)
                this.$emit('orderConfirmed')
            })
            
            
        },
        cancel(order, index){
            var params = new URLSearchParams();
            params.append('order_id', order.order__id);
            params.append('action', 'cancel');

            axios.post('administrador/action_order', params ).then( _ => {
                swal.fire(
                    'Bien!',
                    'Orden Cancelada',
                    'success'
                )
                this.orders.splice(index, 1)
            })
            
        }
    },
    props:{
        'orders' : Array
    }
}
</script>

<style scoped>
    
</style>