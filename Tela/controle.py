# Importacao das ferramentas de tela abaixo:
from PyQt5 import uic, QtWidgets
# Def p/ criar uma funcao para que o Python entenda.
def executar():
    salario = float(tela.txtSalario.text())
    descontos = float(tela.txtDescontos.text())
    resultado = salario-descontos
    tela.lblResultado.setText(str(resultado))

# esses sao para trazer ferramentas e tela do Pip 
app = QtWidgets.QApplication([])
tela = uic.loadUi ('Tela teste.ui')
tela.btnCalcular.clicked.connect(executar)
#formulario = uic.loadUi('Tela // Tela teste.ui') usar assim caso de erro para puxar a tela, usando // estou dizendo que a 'Tela teste.ui' esta na pasta Tela 

#aki para mostrar e executar a tela
tela.show()
app.exec()