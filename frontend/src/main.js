import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import "bootstrap/dist/css/bootstrap.min.css";

import navbar from './components/navbar';
import Router from './routes/Router'
import config from './routes/config';

import apiFetch from './api/fetch';

document.querySelector('#navbar').innerHTML = `${navbar}`
document.querySelector('#app').innerHTML = config['/'].view
document.title = config['/'].title

apiFetch()

document.addEventListener('DOMContentLoaded', Router.init())
