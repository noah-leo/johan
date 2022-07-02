i=0
while i<3:
      usuario=input("ingrese su usuario: ")
      i=i +1
      if str(usuario)=="johnjara":
            print("USUARIO CORRECTO")
            clave=input("ingrese su clave: ")
            if str(clave)=="1478":
                  print("Bienvenido")
                  break
            else:
                  print("vuelve a intentarlo, 2 veces")
                  if    i==3:
                        print("tarjeta retenida o consulta al admin")
                        break
      else:
            print("Usuario Incorrecto")
            if    i==3:
                  print("Tarjeta retenida o Consulta al admin")