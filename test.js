const first_hours = prompt("Write hours first moment:")
const first_minutes = prompt("Write minutes first moment:")
const first_second = prompt("Write second first moment:")
const second_hours = prompt("Write hours second moment:")
const second_minutes = prompt("Write minutes second moment:")
const second_second = prompt("Write second second moment:")

delta_hours = first_hours - second_hours
delta_minutes = first_minutes - second_minutes
delta_second = first_hours - second_second

delta_second_total = delta_hours * 3600 + delta_minutes * 60 + delta_second

let elcho = document.querySelector('#root')
elcho.innerHTML = `
<div>
<h1>${delta_second_total}</h1>
</div>
`