let nome = prompt("Digite o nome do aluno: ");
let nota1 = parseFloat(prompt("Digite a primeira Nota: "));
let nota2 = parseFloat(prompt("Digite a segunda Nota: "));
let media = (nota1+nota2)/2;
if(media >= 6){
    alert("Aprovado!");
}else{
    alert("Reprovado");
}