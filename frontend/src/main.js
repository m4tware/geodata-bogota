import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import "bootstrap/dist/css/bootstrap.min.css";

import navbar from './components/navbar';
import Router from './routes/Router'
import config from './routes/config';

import {health, cifrasGeojson} from './api/fetch';

document.querySelector('#navbar').innerHTML = `${navbar}`
document.querySelector('#app').innerHTML = config['/'].view
document.title = config['/'].title

// both funcs will be executed on startup, see console to
// check API communication:
health().then(api => console.log(api))
cifrasGeojson().then(api => console.log(api))

document.addEventListener('DOMContentLoaded', Router.init())
