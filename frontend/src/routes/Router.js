const Router = {
    init: () => {
        const links = document.querySelectorAll('#navbar-component .nav-link')
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault()
            })
        })
    }
}

export default Router