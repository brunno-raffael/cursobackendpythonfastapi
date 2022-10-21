async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais')
    console.log(response.data)
    const animais = response.data

    const lista = document.getElementById('lista-animais')
    console.log(lista)

    lista.innerHTML = ''

    animais.forEach(animal => {
        const item = document.createElement('li')
        item.innerText = animal.nome

        lista.appendChild(item)        
    })
}

function manipularFormulario() {
    const form_animal = document.getElementById('form-lista')
    const input_nome = document.getElementById('nome')

    console.log(form_animal)
    
    form_animal.onsubmit = (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value

        console.log(nome_animal)

        const response = axios.post('http://localhost:8000/animais', {
            id: 0,
            nome: nome_animal,
            idade: 4,
            sexo: 'Macho',
            cor: 'Bege'
        })
        
        carregarAnimais()
        console.log(response.data)
        alert('Animal Cadastrado!')
    }
}

function app() {
    console.log('App Iniciada!')
    carregarAnimais()
    manipularFormulario()
}

app()