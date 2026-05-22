#rosmeri anette miss castillo
#trabaja en la organizacion de un evento de precios.tienes una lista de celebridades.
#1.crea una lista llamada invitados con los nombres:"roberto downy jr","emma stone","cillian murphy"
#2.llegada de ultimo momento.agrega a "zendaya" al final de la lista 
#3.invitado VIP ."steven spleder" acaba de llegar y debe de ir al principio de la lista
#4.cancelacion."emma stone" aviso que no podra asitir
#5.seguridad.el ultimo de la lista se porto mal y debe ser retirado 
#6.imprime la lista final y cuantos invitados quedan en la lista

#punto no.1
invitados=["robert downy jr","emma stone","cillian murphy" ]
#punto no.2
invitados.append("zendaya")
#punto no.3
invitados.insert(0,"steven sprelber")
#punto no.4
#invitados.pop(2)
invitados.remove("emma stone")
#punto no.5
invitados.pop(3)
#punto no.6
print(invitados,"no. total invitados:",len(invitados))