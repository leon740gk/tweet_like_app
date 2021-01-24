function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

function lookup(method, endpoint, callback, data) {
    let jsonData;
    if (data) {
        jsonData = JSON.stringify(data)
    }
    const xhr = new XMLHttpRequest()
    const url = `http://127.0.0.1:8000/api${endpoint}`

    xhr.responseType = 'json'
    xhr.open(method, url)
    const csrf_token = getCookie('csrftoken')
    xhr.setRequestHeader("Content-Type", "application/json")
    if (csrf_token) {
        xhr.setRequestHeader("HTTP-X-REQUESTED-WITH", "XMLHttpRequest")
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
        xhr.setRequestHeader("X-CSRFToken", csrf_token)
    }

    xhr.onload = function() {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = function(e) {
        console.log(e)
        callback("Error occurred", 400)
    }
    xhr.send(jsonData)
}

export function createTweet(newTweet, callback) {
    lookup("POST", "/tweets/create/", callback, {content: newTweet})
}

export function loadTweets(callback) {
    lookup("GET", "/tweets/", callback)
}