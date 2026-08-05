async function apiFetch() {
    const url = ('http://localhost:8000/mapas/api-test')
    try {
        const req = await fetch(url)
        const res = await req.json()
        console.log(res)
    } catch{
        console.error('unu')
    }
}

export default apiFetch