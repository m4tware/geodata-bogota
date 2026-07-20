import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import "bootstrap/dist/css/bootstrap.min.css";

import navbar from './components/navbar';
import Router from './routes/Router'
import config from './routes/config';

document.querySelector('#navbar').innerHTML = `${navbar}`
document.querySelector('#app').innerHTML = config['/'].view
document.title = config['/'].title

document.addEventListener('DOMContentLoaded', Router.init())
