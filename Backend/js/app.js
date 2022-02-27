const temp = document.getElementById('temperature');
const btn = document.getElementById('btn');
const feedDisplay = document.getElementById('temp-box');

url = 'http://localhost:8000/temperature/'

btn.addEventListener('click', async () => {

    while(temp.firstChild){
        temp.removeChild(temp.firstChild)
    }

    return fetch(url)
    .then(result => { return result.json() })
    .then(data => {
        const output = `<div><p>` + data.temperature + `</p></div>`;
        temp.innerAdjacentHTML(output)
        console.log(output)
    }).catch(err => console.error(err))
})