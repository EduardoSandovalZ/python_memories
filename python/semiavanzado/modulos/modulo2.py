# Si nosotros vamos a importar un modulo en una carpeta fuera de la actual, debemos de hacerle append al sys
import sys
print(sys.path)
sys.path.append('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\modulos_eduardo')
# Una vez importado ya podemos usarlo
print(sys.path)
# Nos va a marcar alerta, pero no hay problema
import presentacion

eduardo = presentacion.presentacion('Eduardo')
print(eduardo)