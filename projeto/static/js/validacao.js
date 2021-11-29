onload = function() {

    document.getElementById('id_cpf').addEventListener('focus', exibeAjuda);
    document.getElementById('id_email').addEventListener('focus', exibeAjuda);
    document.getElementById('id_usuario').addEventListener('focus', exibeAjuda);
    document.getElementById('id_cpf').addEventListener('blur', validaCampo);
    document.getElementById('id_email').addEventListener('blur', validaCampo);
    document.getElementById('id_usuario').addEventListener('blur', validaCampo);
}

function validaForm(evento) {
    console.log("formulário não enviado")
    evento.preventDefault();
}

function validaCampo(evento) {
    var msgcpf = document.getElementById('idMensagemCPF');
    var msgemail = document.getElementById('idMensagemEmail');
    var msgusuario = document.getElementById('idMensagemUsuario');
    var msgtelefone = document.getElementById('idMensagemTelefoneResponsavel');
    msgcpf.innerHTML = "&nbsp;";
    msgemail.innerHTML = "&nbsp;";
    msgusuario.innerHTML = "&nbsp;";
}

function exibeAjuda(evento) {

    var msgcpf = document.getElementById('idMensagemCPF');
    var msgemail = document.getElementById('idMensagemEmail');
    var msgusuario = document.getElementById('idMensagemUsuario');

    switch(evento.target.id) {
        case 'id_usuario':
            console.log("Validacao de nome de usuario")
            msgusuario.innerHTML = "Informe o Nome de Usuário que será utilizado para logar no site.";
            break;
        case 'id_cpf':
            console.log("Validacao de cpf")
            msgcpf.innerHTML = "Entre o CPF com apenas números (sem pontos ou traços).";
            break;
        case 'id_email':
            console.log("Validacao de Email")
            msgemail.innerHTML = "Informe o seu Email.";
            break;
        default:
    }

}