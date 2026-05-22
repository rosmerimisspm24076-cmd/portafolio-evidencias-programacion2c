Materias=("matematicas","fisica","quimica","biologia","historia","geografia","literatura")
Materias.append("ingles")
Materias.insert("educacio fisica")
print(Materias{2})

docente=("juan perez","fulanito perez","perecila sanches")
print(docente{0})

conjunto={1,2,3,4,5}
conjunto.add(6)
conjunto.add(6)
print(conjunto)

alumno={"nombre":"carlos","edad":20,"carrera":"ingenieria"}
print(alumno{"nombre"})
print(alumno{"edad"})

print(Materias)
lista_conjunto=list(conjunto)#convirtiendo el conjunto a una lista
conjunto_materias=set(Materias)#convirtiendo el conjunto de la lista de materias a un conjunto
print(conjunto_materias)

