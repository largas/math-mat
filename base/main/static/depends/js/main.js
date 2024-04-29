const allCards = document.querySelectorAll('.card')

document.querySelector('.filters').addEventListener("click", (event) => {
    if (event.target.tagName !== 'BUTTON') return false;

    let currentFilter = event.target.dataset['f']

    allCards.forEach(elem => {
        if (elem.classList.contains('hide')) {
            elem.classList.remove('hide')
        }
        if (!elem.classList.contains(currentFilter)) {
            elem.classList.add('hide')
        }
    })
})