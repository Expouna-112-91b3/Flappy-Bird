import multiprocessing as multip
import time

def centroide_mao(centroide, q):
  for i in centroide:

    q.put(i)

    time.sleep(1)


def flappy_app(q):

  done = False

  while done == False:
    teste = q.get()

    if teste:
      print("tem numero")
    
    else:
      print("num tem")

if __name__ == "__main__":
  
  centroide = [1, 2, 3, 4, 5, 6, 7, 8, "", "", ""]

  q = multip.Queue()
  p1 = multip.Process(target=flappy_app, args=(q,))
  p2 = multip.Process(target=centroide_mao, args=(centroide, q))

  p1.start()
  p2.start()