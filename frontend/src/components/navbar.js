export const navbar = `
  <nav class="navbar navbar-expand-sm bg-body-tertiary fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand">GeoData Bogotá</a>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-link active" aria-current="page" href="/">Inicio</a>
          <div class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false" aria-current="page" >
            Mapas
            </a>
            <div class="dropdown-menu">
              <a class="nav-link disabled" href="map_cifras">Delitos y Reportes en Localidades</a>
              <a class="nav-link disabled" href="map_policia">Distribución de Presencia Policial</a>
            </div>
          </div>
          <a class="nav-link disabled" href="stats_cifras">Estadísticas</a>
          <a class="nav-link disabled" aria-disabled="true">Acerca de</a>
        </div>
      </div>
    </div>
  </nav>
`
