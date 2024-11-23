//Função para confirmar exclusão
document.addEventListener('DOMContentLoaded', function() {
    const deleteForms = document.querySelectorAll('form[onsubmit="return confirmarExclusao(event);"]');
    
    deleteForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!confirm('Tem certeza que deseja excluir este registro?')) {
                event.preventDefault();
            }
        });
    });
});


// Temporizar o fechamento de alertas
document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll('.alert-dismissible');
    if (alerts) {
        alerts.forEach(function (alert) {
            setTimeout(function () {
                // Use o método fadeOut do Bootstrap
                alert.classList.add('fade');
                alert.classList.remove('show');

                setTimeout(function () {
                    alert.remove();
                }, 1000); // Tempo correspondente ao fade-out de .5s
            }, 3000); // 3 segundos antes de começar o fade-out
        });
    }
});
