const path = require('path');

const { VueLoaderPlugin } = require('vue-loader')

module.exports = {
    output: {
        path : path.resolve(__dirname, 'static/app/js'),
        filename : 'app.js',        
    },
    entry : {
        main : './resources/js/src/index.js'
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.css$/,
                use: [
                    'vue-style-loader',
                    'css-loader'
                ]
            }
        ]
    },
    resolve: {
        extensions: [
          '.js',
          '.vue'
        ],  
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        },      
    },
    
    plugins: [
        new VueLoaderPlugin()
    ]

}