const api = 'http://192.168.0.18:8000'

export async function apiFetch() {
    const url = (`${api}/api/cifras-geojson`)
    try {
        const req = await fetch(url)
        return req.json()
    } catch{
        console.error('no response')
    }
}


export const health = async () => {
    try {
        const req = await fetch(`${api}/info`)
        return req.json()
    } catch {
        console.error('no response')
    }
}

export const cifrasGeojson = async () => {
    try {
        const router = `${api}/api/cifras/delitos-alto-impacto/geojson`
        const req = await fetch(router)
        return req.json()
    } catch {
        console.error('no response')
    }
}
