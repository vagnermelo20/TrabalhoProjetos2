/**
 * Utility functions for Sistema de Gerenciamento de Alunos
 */

// Formatação de moeda brasileira
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

// Formatação de data brasileira
function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('pt-BR').format(date);
}

// Confirmação de exclusão
function confirmDelete(message = 'Tem certeza que deseja excluir este item?') {
    return confirm(message);
}

// Mascaramento de CPF
function maskCPF(cpf) {
    return cpf
        .replace(/\D/g, '')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})/, '$1-$2')
        .replace(/(-\d{2})\d+?$/, '$1');
}

// Mascaramento de telefone
function maskPhone(phone) {
    return phone
        .replace(/\D/g, '')
        .replace(/(\d{2})(\d)/, '($1) $2')
        .replace(/(\d{5})(\d)/, '$1-$2')
        .replace(/(-\d{4})\d+?$/, '$1');
}

// Mascaramento de CEP
function maskCEP(cep) {
    return cep
        .replace(/\D/g, '')
        .replace(/(\d{5})(\d)/, '$1-$2')
        .replace(/(-\d{3})\d+?$/, '$1');
}

// Limpar máscaras
function unmask(value) {
    return value.replace(/\D/g, '');
}

// Aplicar máscaras nos formulários
document.addEventListener('DOMContentLoaded', function() {
    // Aplicar máscara nos inputs de CPF
    const cpfInputs = document.querySelectorAll('input[name="cpf"], input[name$="_cpf"]');
    cpfInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            e.target.value = maskCPF(e.target.value);
        });
    });
    
    // Aplicar máscara nos inputs de telefone
    const phoneInputs = document.querySelectorAll('input[name="telefone"], input[name$="_telefone"]');
    phoneInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            e.target.value = maskPhone(e.target.value);
        });
    });
    
    // Aplicar máscara nos inputs de CEP
    const cepInputs = document.querySelectorAll('input[name="cep"]');
    cepInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            e.target.value = maskCEP(e.target.value);
        });
        
        // Buscar endereço automaticamente pelo CEP
        input.addEventListener('blur', function(e) {
            const cep = unmask(e.target.value);
            if (cep.length === 8) {
                fetch(`https://viacep.com.br/ws/${cep}/json/`)
                    .then(response => response.json())
                    .then(data => {
                        if (!data.erro) {
                            const form = input.closest('form');
                            if (form) {
                                const cidadeInput = form.querySelector('input[name="cidade"]');
                                const estadoSelect = form.querySelector('select[name="estado"]');
                                const bairroInput = form.querySelector('input[name="bairro"]');
                                
                                if (cidadeInput) cidadeInput.value = data.localidade;
                                if (estadoSelect) estadoSelect.value = data.uf;
                                if (bairroInput) bairroInput.value = data.bairro;
                            }
                        }
                    })
                    .catch(error => console.error('Erro ao buscar CEP:', error));
            }
        });
    });
    
    // Confirmar exclusão de itens
    const deleteButtons = document.querySelectorAll('.btn-delete, [data-action="delete"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            const message = button.dataset.message || 'Tem certeza que deseja excluir este item?';
            if (!confirmDelete(message)) {
                e.preventDefault();
            }
        });
    });
    
    // Formatar valores monetários
    const currencyElements = document.querySelectorAll('.currency');
    currencyElements.forEach(element => {
        const value = parseFloat(element.textContent);
        if (!isNaN(value)) {
            element.textContent = formatCurrency(value);
        }
    });
    
    // Formatar datas
    const dateElements = document.querySelectorAll('.date');
    dateElements.forEach(element => {
        element.textContent = formatDate(element.textContent);
    });
}); 