document.addEventListener('DOMContentLoaded', function() {
const formEl = document.querySelector('.form_compose')


    formEl.addEventListener('submit' , event => {
        event.preventDefault()

        const formData = new FormData(formEl)

        let userName = formData.get('username')
        let usePassword = formData.get('password')


        fetch('/savepro', {
            method: 'POST',
            body: JSON.stringify(
                {
                    username: userName,
                    userpassword: usePassword,
                }
            )
        }).then(res => {
            
            // console.log(res)
            return res.json()
        })
        .then(result => {
            // console.log(result)
            loaduserss()
        })

    })


const divEl = document.querySelector('.displayHer')
function loaduserss(){
let users = []
divEl.innerHTML = ""
    fetch('/loadusers')
    .then(req => {
        // console.log(req)
        return req.json()
    }).then(data => {
        // console.log(data)
        data.forEach(user => {
            users.push(user)
            // console.log(user)
        })
        // console.log(users)
        users.forEach( user => {
            
            divEl.innerHTML += `
            <div class="d">
            <h1 class="h11">${user.name}</h1>
            <h1>${user.email}</h1>
            <button class="delbtn" > delete </button>
            </div>
            `
        })
        let diver = document.querySelectorAll('.d')
        diver.forEach(function(dive){
            dive.addEventListener('click', function(e) {
                console.log(this.innerHTML); // Will refer to the current user element
                // console.log(e);
            });

        })
        let delBtn = document.querySelector('.delbtn')

        delBtn.addEventListener('click', (e) => {
            console.log(delBtn)
            console.log(e.target)
            // this.parentElement.querySelector('.h11')
            console.log("parentwoeks")

        })


    }
)}
})
