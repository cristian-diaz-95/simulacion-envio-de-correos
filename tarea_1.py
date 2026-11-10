ruta_arch="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\lectura_archivos\\mbox.txt"
ruta_dest="D:\\Users\\CRISTIAN DBAY\\Desktop\\curso de python\\python\\lectura_archivos\\tarea_1_result.txt"
with open(ruta_arch,'r',encoding="utf-8") as arch, \
    open(ruta_dest,'w',encoding="utf-8") as dest:
    email=[]
    final=[]
    for linea in arch:
        if linea.startswith("From: "):
            email.append(linea.split(" ")[1])
    email.reverse()
    for i in range(len(email)):
        email[i]=email[i].strip("\n")
    lst_emails=list(dict.fromkeys (email))
    for i in range (len(lst_emails)):
        final.append(lst_emails[i]+"  enviado [ok]")
    dest.writelines('\n'.join (final))
    
    print(f"conjunto terminado")

arch.close()
