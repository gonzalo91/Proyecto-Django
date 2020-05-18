<template>
    <div>
        <p>hola</p>
        <span>{{ foo }}</span>
    </div>
</template>


<script>
export default {
    data: function (){
        return {
            'foo' : 'bar',
        }
    }
}
</script>

<style scoped>
    p {
        color:red;
    }
</style>