async function renderizarAlunos() {
    const container = document.getElementById('lista-alunos');
    if (!container) return;

    // Busca os dados reais do banco via Flask
    const resposta = await fetch('/api/alunos');
    const alunosBanco = await resposta.json();

    container.innerHTML = ''; 

    alunosBanco.forEach(aluno => {
        const card = document.createElement('div');
        card.className = `student-card ${aluno.status === 'banheiro' ? 'status-banheiro' : ''}`;
        card.innerHTML = `
            ${aluno.nome}<br>
            <small>${aluno.status}</small>
        `;
        container.appendChild(card);
    });
    {{ url_for('static', filename='style.css') }}
}
