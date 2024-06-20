async function getData(username) {
    const url = "http://127.0.0.1:8080/api/" + username
    const response = await fetch(url)
    try {
        if (response.ok) {
            const data = await response.json()
            return data
        }
    } catch (error) {
        console.log("Account what you inspire is locked");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    let btn = document.querySelector("#submit");
    let inputElement = document.querySelector("#url-input");
    let responseElement = document.querySelector(".text-response-area");
    btn.addEventListener("click", async () => {
        let inputValue = inputElement.value
        let data = await getData(inputValue)
        try {
            responseElement.innerHTML = data;
        } catch (error) {
            console.log(error);

        }
    })
})