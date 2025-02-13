#!/bin/bash

#m, monto
#t, tiempo
#i, interes anual

echo "Ingrese el monto"
read m
echo "Introduzca la tasa de interés por año"
read t
echo "Ingresa el periodo de tiempo en años"
read i

echo "Iniciando el cálculo del interés simple..."

# Mensaje al final
d=$(expr $m\* $t \* $i )
echo "Cálculo completado."
echo $d
