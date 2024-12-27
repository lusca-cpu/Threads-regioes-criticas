import threading
from estoque import * 
from produtor import *
from consumidor import *
import time
import random

def produtores(prod, e, loc, stop_event):
    while not stop_event.is_set():
        tempo = random.randint(1,5)
        time.sleep(tempo)
        prod.criar_produto(prod.produto)
        loc.acquire()
        e.preenche_estoque(prod)
        loc.release()

def consumidores(con, e, loc, stop_event):
    while not stop_event.is_set():
        tempo = random.randint(1,3)
        time.sleep(tempo)
        loc.acquire()
        e.consome_estoque(con)
        loc.release()
        

def main():
    loc = threading.Lock()
    est = Estoque(1, [])  
    stop_event = threading.Event()  

    threads = []
    for i in range(3):
        pod = Produtor(i, [])
        con = Consumidor(i)
        # Passar funções sem chamá-las, usando args para passar argumentos
        p = threading.Thread(target=produtores, args=(pod, est, loc, stop_event))
        c = threading.Thread(target=consumidores, args=(con, est, loc, stop_event))
        threads.extend([p, c])
        p.start()
        c.start()

    try:
        while True:
            time.sleep(2)  # Aguarda sinal de interrupção (Ctrl+C)
    except KeyboardInterrupt:
        print("Encerrando as threads...")
        stop_event.set()  
        for t in threads:
            t.join()  

    print("Programa encerrado.")

if __name__ == '__main__':
    main()
        