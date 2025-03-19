/**
 * Dashboard scripts for Sistema de Gerenciamento de Alunos
 */

document.addEventListener('DOMContentLoaded', function() {
    // Configurações comuns para todos os gráficos
    const commonOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    padding: 20,
                    boxWidth: 15,
                    font: {
                        size: 12
                    }
                }
            },
            tooltip: {
                enabled: true,
                callbacks: {
                    label: function(context) {
                        let label = context.label || '';
                        if (label) {
                            label += ': ';
                        }
                        if (context.parsed !== null) {
                            label += context.parsed;
                        }
                        return label;
                    }
                }
            }
        }
    };

    // Gráfico de escolaridade (pizza)
    const ctxEscolaridade = document.getElementById('graficoEscolaridade');
    if (ctxEscolaridade) {
        const escolaridadeData = JSON.parse(ctxEscolaridade.dataset.valores || '{}');
        const labels = Object.keys(escolaridadeData);
        const values = Object.values(escolaridadeData);
        
        if (labels.length) {
            new Chart(ctxEscolaridade, {
                type: 'pie',
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: [
                            '#3498db', '#2ecc71', '#f39c12', '#e74c3c', 
                            '#9b59b6', '#1abc9c', '#34495e', '#d35400'
                        ],
                        borderColor: '#ffffff',
                        borderWidth: 1
                    }]
                },
                options: {
                    ...commonOptions,
                    title: {
                        display: true,
                        text: 'Distribuição por Escolaridade'
                    }
                }
            });
        } else {
            ctxEscolaridade.parentElement.innerHTML = '<div class="alert alert-info">Nenhum dado disponível para exibição</div>';
        }
    }

    // Gráfico de raça/cor (barras)
    const ctxRaca = document.getElementById('graficoRaca');
    if (ctxRaca) {
        const racaData = JSON.parse(ctxRaca.dataset.valores || '{}');
        const labels = Object.keys(racaData);
        const values = Object.values(racaData);
        
        if (labels.length) {
            new Chart(ctxRaca, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Alunos',
                        data: values,
                        backgroundColor: '#3498db',
                        borderColor: '#2980b9',
                        borderWidth: 1
                    }]
                },
                options: {
                    ...commonOptions,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                precision: 0
                            }
                        }
                    }
                }
            });
        } else {
            ctxRaca.parentElement.innerHTML = '<div class="alert alert-info">Nenhum dado disponível para exibição</div>';
        }
    }

    // Gráfico de situação profissional (donut)
    const ctxProfissional = document.getElementById('graficoProfissional');
    if (ctxProfissional) {
        const profissionalData = JSON.parse(ctxProfissional.dataset.valores || '{}');
        const labels = Object.keys(profissionalData);
        const values = Object.values(profissionalData);
        
        if (labels.length) {
            new Chart(ctxProfissional, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: [
                            '#2ecc71', '#3498db', '#f39c12', '#e74c3c', 
                            '#9b59b6', '#1abc9c', '#34495e', '#d35400'
                        ],
                        borderColor: '#ffffff',
                        borderWidth: 1
                    }]
                },
                options: commonOptions
            });
        } else {
            ctxProfissional.parentElement.innerHTML = '<div class="alert alert-info">Nenhum dado disponível para exibição</div>';
        }
    }

    // Filtros de pesquisa nos formulários
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        const clearButton = document.getElementById('clearFilters');
        if (clearButton) {
            clearButton.addEventListener('click', function(e) {
                e.preventDefault();
                const inputs = searchForm.querySelectorAll('input, select');
                inputs.forEach(input => {
                    input.value = '';
                });
                searchForm.submit();
            });
        }
    }
}); 