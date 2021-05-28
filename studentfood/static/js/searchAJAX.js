let a = 5;
const testButton = document.querySelector('#ajax_click')
const pageNumberEl = document.querySelector("#page-number")
const testAllButton = document.querySelector('#ajax_click_all')
const get_html_button = document.querySelector("#get_html_click")
testAllButton.addEventListener("click", getAll)
testButton.addEventListener("click", makeRequest)
get_html_button.addEventListener("click", getHTML)



function makeRequest() {
    $.ajax(`https://repetitora.net/api/JS/Images?page=${pageNumberEl.value}&count=1`, {
    success: function(data) {
        data.forEach(el => {
            const img = document.createElement('img');
            img.src = el.thumbnail;
            document.getElementById('test_ajax').append(img)
        })
    }
})
}

function getAll() {
    $.ajax(`https://repetitora.net/api/JS/Images`, {
    success: function(data) {
        data.forEach(el => {
            const img = document.createElement('img');
            img.src = el.thumbnail;
            document.getElementById('ajax_all').append(img)
        })
    }
})
}

function getHTML () {
    $.ajax('http://127.0.0.1:8000/', {
        success: function (data) {
            console.log(data)
        }
    })
}
/* var test_js = document.getElementById('test_ajax')
test_js.style.background = '#a1a'

let set_color_elem = document.getElementsByClassName('row')
set_color_elem[0].style.background = 'blue'; */

a = 8;
console.log(a)