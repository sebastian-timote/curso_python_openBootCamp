import sqlite3
import getpass

def main():
    crear_usuario(5, "simon", "otraclavemas")
def main2():
    username = input("Nombre de ususario: ")
    password = getpass.getpass("Contraseña: ")
    if (verifica_credenciales(username, password)):
        print("login correcto")
    else:
        print("login incorrecto")

def verifica_credenciales(username,password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("query a ejecutar: ", query)
    rows= cursor.execute(query)
    data = rows.fetchone()
    print("data es:", type(data))
    cursor.close()
    conn.close()
#con el isolation_level=None envia los datos directos ala db y no hay que commitearlos
def crear_usuario(identificador,usuario,clave):
    conn = sqlite3.connect('miaplicacion.db', isolation_level=None)
    cursor = conn.cursor()
    query = f"INSERT INTO users(id,username,password)  VALUES(?,?,?)"
    rows= cursor.execute(query, (identificador,usuario,clave))
    print(type(rows))
    #conn.commit()
    cursor.close()
    conn.close()
    
if __name__ == '__main__':
    main()  

