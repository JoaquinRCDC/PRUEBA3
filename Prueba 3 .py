#PRUEBA 3 - JOAQUIN ROMERO CARDENAS 
from itertools import cycle

dni = []
nombre = []
edad = []
pnacimiento = []
cnacimiento = []
fnacimiento = []
conyugal = []

def digito_verificador(dni):
    reversed_digits = map(int, reversed(str(dni)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def salir():
    print("Usted ha salido del menu.\nJoaquin Romero version del programa (1.0)")
    exit()
    

while True:

    op = int(input("\nBienvenido al sistema de autoservicio de atencion rapida de RENAPER, para comenzar seleccione una de las opciones que se muestran en el menu.\n\n-------- Menu Principal -------\n\n1. Grabar\n2. Buscar\n3. Imprimir certificados\n4. Eliminar\n5. Salir\n\n-------------------------------\n"))
    
    if op == 1:
        
        while True:
            grabar_dni = input("Ingrese dni a grabar (sin puntos ni digito verificador): ")

            if '-' in grabar_dni or len(grabar_dni)>8:

                print('Eror al grabar dni, ingrese dni sin digito verificador!')
                True
                
            elif '.' in grabar_dni:

                print('Eror al grabar rut, ingrese rut sin puntos!')
                True
            else:

                dv = digito_verificador(grabar_dni)
                dni.append(grabar_dni+'-'+str(dv))
                break
    
        while True:
            grabar_nombre = input("Ingrese nombre a grabar (debe tener como minimo 8 caracteres): ")
            if len(grabar_nombre)>=8:
                nombre.append(grabar_nombre.upper())
                break
            else:
                print("Ingrese un nombre con 8 caracteres como minimo")
                True
    
        while True:        
            grabar_edad = int(input("Ingrese edad (la edad debe ser mayor o igual a 0): "))
            if grabar_edad>=0:
                edad.append(grabar_edad)
                break
            else:
                print("Ingrese una edad valida")
                True
    
        grabar_pnacimiento = str(input("Ingrese pais de nacimiento: "))
        pnacimiento.append(grabar_pnacimiento.upper())
    
        grabar_cnacimiento = str(input("Ingrese ciudad de nacimiento: "))
        cnacimiento.append(grabar_cnacimiento.upper())

        grabar_fnacimiento = str(input("Ingrese su fecha de nacimiento separados por guiones (dd/mm/aa): "))
        fnacimiento.append(grabar_fnacimiento)
        
        while True:
            grabar_conyugal = int(input("Ingrese una opcion segun su estado conyugal:\n1.Soltero/a            2.Casado/a                3.Viudo/a           4.Divorciado/a                5.Separado/a\n"))

            if grabar_conyugal==1:
                conyugal.append('SOLTERO/A')
                break
            elif grabar_conyugal==2:
                conyugal.append('CASADO/A')
                break
            elif grabar_conyugal==3:
                conyugal.append('VIUDO/A')
                break
            elif grabar_conyugal==4:
                conyugal.append('DIVORCIADO/A')
                break
            elif grabar_conyugal==5:
                conyugal.append('SEPARADO/A')
                break
            else:
                print("Ingrese una opcion valida!")
                True

        print('\nUsuario grabado correctamente.')
        
        while True:
            continuar = int(input("\n¿Desea volver al menu principal? Ingrese una opcion.\n1.Volver al menu                      2.Salir del menu.\n"))
                    
            if continuar==1:
                break
            elif continuar==2:
                salir()
            else:
                print('Ingrese una opcion valida')
                True

    elif op ==2:
    
            buscar_dni = input("Ingrese dni de persona a buscar: ")
            buscar_dni += '-'+str(digito_verificador(buscar_dni))
            
            if buscar_dni in dni:             
                if dni.index(buscar_dni)>=0:
            
                    print(f"\nLos datos de la persona a buscar son:\n\nNombre: {nombre[dni.index(buscar_dni)]}\nEdad: {edad[dni.index(buscar_dni)]}\nPais de nacimiento: {pnacimiento[dni.index(buscar_dni)]}\nCiudad de nacimiento: {cnacimiento[dni.index(buscar_dni)]}\nFecha de nacimiento: {fnacimiento[dni.index(buscar_dni)]}\nEstado conyugal: {conyugal[dni.index(buscar_dni)]}")
                
                    if pnacimiento[dni.index(buscar_dni)] == 'ARGENTINA':
                        print('\nNacionalidad Argentina')
                    
                    while True:
                            continuar = int(input("\n¿Desea volver al menu principal? Ingrese una opcion.\n1.Volver al menu                      2.Salir del menu.\n"))
                    
                            if continuar==1:
                                break
                            elif continuar==2:
                                salir()
                            else:
                                print('Ingrese una opcion valida')
                                True
            else:
                print("\nIngrese un dni grabado anteriormente!")
                True
    
    elif op == 3:
        
            cert_dni = input("Ingrese dni para imprimir certificado: ")
            cert_dni+= '-'+str(digito_verificador(cert_dni))

            if cert_dni in dni:
                if dni.index(cert_dni)>=0: 
                    certificados = int(input('\nSeleccione una opcion segun el certificado que desea imprimir.\n\n1. Certificado de nacimiento.\n2. Certificado de estado conyugal.\n'))
        
                    if certificados == 1:
                        print(f'------- Certificado de nacimiento -------\n\nRENAPER CERTIFICA QUE LA PERSONA CON:\n\nDNI: {cert_dni}\nNombre: {nombre[dni.index(cert_dni)]}\nEdad: {edad[dni.index(cert_dni)]}\nNacio en el pais de: {pnacimiento[dni.index(cert_dni)]}\nEn la ciudad de: {cnacimiento[dni.index(cert_dni)]}\nCon fecha: {fnacimiento[dni.index(cert_dni)]}')

                        while True:
                            continuar = int(input("\n¿Desea volver al menu principal? Ingrese una opcion.\n1.Volver al menu                      2.Salir del menu.\n"))
                    
                            if continuar==1:
                                break
                            elif continuar==2:
                                salir()
                            else:
                                print('Ingrese una opcion valida')
                                True
                
                    elif certificados==2:
                        print(f'------- Certificado de estado conyugal -------\n\nRENAPER CERTIFICA QUE LA PERSONA CON:\n\nDNI: {cert_dni}\nNombre: {nombre[dni.index(cert_dni)]}\nEdad: {edad[dni.index(cert_dni)]}\nSe encuentra actualmente: {conyugal[dni.index(cert_dni)]}\n\n-------------------------------\n')

                    else:
                        print("Ingrese una opcion valida!")
            else:
                print('\nIngrese un dni grabado anteriormente!')
                break
            
    
    elif op ==4:


            eliminar_dni = input('Ingrese dni para eliminar: ')
            eliminar_dni += '-'+str(digito_verificador(eliminar_dni))
            
            if eliminar_dni in dni:
                if dni.index(eliminar_dni)>=0:
                
                    nombre.pop(dni.index(eliminar_dni))
                    edad.pop(dni.index(eliminar_dni))
                    pnacimiento.pop(dni.index(eliminar_dni))
                    cnacimiento.pop(dni.index(eliminar_dni))
                    dni.pop(dni.index(eliminar_dni))
                    
                    print("Usuario eliminado correctamente!")
                    
                    while True:
                            continuar = int(input("\n¿Desea volver al menu principal? Ingrese una opcion.\n1.Volver al menu                      2.Salir del menu.\n"))
                    
                            if continuar==1:
                                break
                            elif continuar==2:
                                salir()
                            else:
                                print('Ingrese una opcion valida')
                                True

            else:
                print("Ingrese un dni grabado anteriormente!")
                True

    elif op == 5:
        salir()


