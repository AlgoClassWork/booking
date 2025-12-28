const API_BASE = 'http://127.0.0.1:8000/api'
let authToken = ''

async function login() {
    const user = document.getElementById('username').value
    const password = document.getElementById('password').value
    authToken = btoa(`${user}:${password}`)
    try {
        const response = await fetch(`${API_BASE}/rooms/`, {
            headers: {'Authorization': `Basic ${authToken}`}
        })

        if (response.ok) {
            document.getElementById('auth-status').innerText = `Успешная авторизация`
        } else {
            document.getElementById('auth-status').innerText = `Ошибка входа`
            authToken = ''
        }
    } catch (e) {
        console.error('Ошибка сети')
    }
}

