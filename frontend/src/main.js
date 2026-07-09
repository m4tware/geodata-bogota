import './style.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

document.querySelector('#app').innerHTML = `
<div data-bs-theme="dark">
  <nav class="navbar navbar-expand-sm bg-body-tertiary fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand">GeoData Bogotá</a>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-link active" aria-current="page" href="{{ url_for('home') }}">Inicio</a>
          <div class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false" aria-current="page" >
            Mapas
            </a>
            <div class="dropdown-menu">
              <a class="nav-link" href="{{ url_for('map_cifras') }}">Delitos y Reportes en Localidades</a>
              <a class="nav-link" href="{{ url_for('map_policia') }}">Distribución de Presencia Policial</a>
            </div>
          </div>
          <a class="nav-link" href="{{ url_for('stats_cifras') }}">Estadísticas</a>
          <a class="nav-link disabled" aria-disabled="true">Acerca de</a>
        </div>
      </div>
    </div>
  </nav>

  <section class="position-relative vh-100 d-flex align-items-center justify-content-center text-center text-white" style="background: black;">
    <img src="https://colombiavisible.com/wp-content/uploads/2021/12/shutterstock_599811131.jpg" 
        class="position-absolute top-0 start-0 w-100 h-100 object-fit-cover" 
        style="opacity:0.45;" 
        alt="Bogotá">

    <div class="container position-relative">
      <h1 class="display-4 fw-bold">Delitos, Reportes y Presencia Policial</h1>
      <p class="lead mt-3">
        Proyecto abierto a toda la ciudadanía con fines informativos sobre los hurtos en las diferentes 
        localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad.
      </p>
    </div>
  </section>
</div>
`
