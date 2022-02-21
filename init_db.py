#motore piu utilizzato per la creazione di app, un modulo
import sqlite3 

#con la funzione connect mi connetto al database
connection = sqlite3.connect('database.db')
with open('crea_posts.sql') as f:
    connection.executescript(f.read()) 
    #serve per eseguire lo script di nostro interesse, le istruzioni si trovano nel file
    # e vengono messe come argomento della funzione execute script, read ovvero crea_posts_sql
#salviamo le modifiche
connection.commit()
connection.close()

#in sostanza lancia lo script che crea il database