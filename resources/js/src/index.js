import Vue from 'vue';

window.axios = require('axios').default;

import HomeComponent from './components/HomeComponent';

window.swal = require('sweetalert2') 

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';


window.axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
window.axios.defaults.xsrfCookieName = "XCSRF-TOKEN";
window.axios.defaults.withCredentials = true


let token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
    window.axios.defaults.headers.common['X-CSRFToken'] = token.content;
    window.axios.defaults.headers.common['csrf-token'] = token.content;
    window.axios.defaults.headers.common['csrftoken'] = token.content;
    window.axios.defaults.headers.common['csrf_token'] = token.content;
    window.axios.defaults.headers.common['csrfmiddlewaretoken'] = token.content;
    window.axios.defaults.xsrfHeaderName = token.content
window.axios.defaults.xsrfCookieName = token.content
    
} else {
    console.error('CSRF token not found');
}

window.axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'

const App =  new Vue({
    el: "#app",
    components : {
        'home-component' : HomeComponent,
    }
});