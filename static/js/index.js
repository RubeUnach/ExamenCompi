
function analizarCodigo() {
   
    const codigo = document.getElementById('insert').value;
    fetch('/lex', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ codigo: codigo }),
    })
}