import 'bootstrap/dist/js/bootstrap.bundle.min.js';

import { homepage } from './pages/homepage'
import Router from './routes/Router'

document.querySelector('#app').innerHTML = `
  ${homepage}
`

document.addEventListener('DOMContentLoaded', Router.init())
