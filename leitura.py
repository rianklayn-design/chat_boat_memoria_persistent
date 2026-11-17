def ensinar():
    pergunta=input("Digite a pergunta:").strip().lower()
resposta= input("Digite a resposta:").strip().lower()

with open ("cerebro.txt", "a", encoding="utf-8") as arquivo:
    arquivo.white(f"{pergunta}-{resposta}\n")

def conversar():
    fala = input("você: ").strip().lower()
    encontrou= False

   try:
      with open("cwerebro.txt", "r", encoding= "utf-8") as arquivo:
          linhas= arquivo.readlines() 
      for linha in linhas:
          dados=linhas.strip().split("-")
          if len(dados)==2:
              pergunta_salva,resposta_salva= dados[1]
              if fala == pergunta:
                  print(f"bot:{resposta}")
                  encontrou: True
                  break
              

      if not encontrou:
                print("bot: desculpe, nao sei a resposta. use a opçao 2 para me ensinar.  ")
                
 
except FileExistsError:
                 print("bot meu cerebo esta vazio! me ensine algo primeiro .")

                  
def listar_conhecimento():
 base_dados = []
 try:
         with open("cerebo.txt", "r", encoding="utf-8")
   as arquivo:
 linhas = arquivo.readlines()
 for linha in linhas:
       dados = linha.strip().split(" -") 
       if len(dados) == 2:
             
        #criar tuplo (pergunta, resposta) e adiciona na lista
        base_dados.append((dados[0]),dados [1])