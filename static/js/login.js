function login() {
    var phone = document.getElementById("phone").value
    var password = document.getElementById("password").value
    window.Document(phone)
    if (username == "" || password == "") {
        var elem = document.getElementById('modal1')
        var instances = M.Modal.init(elem)
        instances.open()
    } else {
        document.getElementById("log_form").submit()
    }
}






