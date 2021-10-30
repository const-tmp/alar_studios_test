function deleteUser(user_id) {
    userName = document.getElementById(`userName-${user_id}`).textContent
    deleteUserInput.value = user_id;
    deleteUserMessage.textContent = `Delete user ${userName}?`
}


document.querySelector('.card-body').querySelectorAll('input').forEach(item => {
    item.addEventListener('input', event => {
        data = {}
        data[event.target.name] = event.target.checked
        makeRequest('PUT', `/api/users/${event.target.dataset.userId}`, data).then(response => {
            if (response['error']) {
                event.target.checked = !event.target.checked
            }
        })

    })
})


async function makeRequest(method, url = '', data = {}) {
    options = {
        method: method,
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          Authorization: authToken.value
        }
  }
  if (method != 'GET') {
    options.body = JSON.stringify(data)
  }
  const response = await fetch(url, options);
  return await response.json();
}
