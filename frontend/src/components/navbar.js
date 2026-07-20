const navbar = `
  <nav id="navbar-component" class="navbar navbar-expand-sm bg-body-tertiary fixed-top">
    <div class="container-fluid">
      <a class="navbar-brand">GeoData Bogotá</a>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-link active" aria-current="page" href="/">Inicio</a>
          <div class="nav-item dropdown">
            <div class="nav-link dropdown-toggle" role="button" data-bs-toggle="dropdown" aria-expanded="false" aria-current="page" >
            Mapas
            </div>
            <div class="dropdown-menu">
              <a class="nav-link" href="/mapas/cifras">Delitos y Reportes en Localidades</a>
              <a class="nav-link" href="/mapas/policia">Distribución de Presencia Policial</a>
            </div>
          </div>
          <a class="nav-link" href="/estadisticas">Estadísticas</a>
          <a class="nav-link" href="/acerca-de" aria-disabled="false">Acerca de</a>
        </div>
      </div>
    </div>
  </nav>
`

export default navbar
