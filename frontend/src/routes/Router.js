import config from "./config"

const Router = {
    init: () => {
        const links = document.querySelectorAll('#navbar-component a.nav-link')
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault()
                Router.navigate(e.target.getAttribute('href'))
            })
        })
        window.addEventListener('popstate', (e) => {
            Router.navigate(e.state.route, false)
        })
    },
    navigate: (route, pushToHistory = true) => {
        if (pushToHistory) history.pushState({route}, null, route)
        let app = document.getElementById('app')
        let toRender = config[route]
        app.innerHTML = toRender.view
        document.title = toRender.title
    }
}

export default Router