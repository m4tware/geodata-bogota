const api = 'http://localhost:8000'

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
        const req = await fetch(`${api}/api/cifras-geojson`)
        return req.json()
    } catch {
        console.error('no response')
    }
}
