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


async function loadRooms() {
    const response = await fetch(`${API_BASE}/rooms/`)
    const rooms = await response.json()

    const roomsDiv = document.getElementById('rooms')
    const select = document.getElementById('room-select')

    //roomsDiv.innerHTML = ''
    //select.innerHTML = ''

    rooms.forEach(room => {
        roomsDiv.innerHTML += `
        <div class="room-card">
            <h3>${room.name}</h3>
            <p>Вместимость: ${room.capacity}</p>
            <p>Локация: ${room.location}</p>
        </div>
        `
    const opt = document.createElement('option')
    opt.value = room.id 
    opt.innerText = room.name
    select.appendChild(opt)
    });
}

loadRooms()
