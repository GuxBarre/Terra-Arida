import random
import string

class Mole:
    
    def __init__(self):
        self.dicionario_mole = {
            'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
            'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
            'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 
            'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
            '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', 
            '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', 
            '(': '-.--.', ')':'-.--.-'}

        # Inversos para a decodificação:
        self.inversor = {v: k for k, v in self.dicionario_mole.items()}

        # Listas para senhas usadas e não usadas
        self.senhas_nao_usadas = []
        self.senhas_usadas = []

    def codificador(self):
        mensagem = input("Digite o que deve ser codificada: ").upper()
        codificado = ''.join(self.dicionario_mole[caracter] + " " for caracter in mensagem if caracter in self.dicionario_mole)
        print(f"Mensagem codificada: {codificado.strip()}\n")
        return codificado

    def decodificador(self): 
        mensagem = input("Digite o que deve ser decodificada: ")
        try:
            decodificado = ''.join(self.inversor[digito] for digito in mensagem.split())
            print(f"Mensagem decodificada: {decodificado}\n")
            return decodificado
        except KeyError:
            print("ERRO: Código inválido!\n")
            return None

    def random(self):
        while True:
            senha = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8))
            if (
                any(letra.isupper() for letra in senha) and 
                any(letra.isdigit() for letra in senha) and 
                any(letra in string.punctuation for letra in senha) and 
                not any(senha[i] == senha[i + 1] for i in range(len(senha) - 1))
            ):
                break
        senha_mole = ''.join(self.dicionario_mole[caracter.upper()] + " " for caracter in senha if caracter.upper() in self.dicionario_mole)
        
        # Adiciona a senha na lista de "não usadas"
        self.senhas_nao_usadas.append((senha, senha_mole.strip()))
        self.salvar_senhas_em_arquivo("nao_usadas")

        print(f"Senha gerada: {senha}\n")
        print(f"Senha em Mole: {senha_mole.strip()}\n")

        # Pergunta ao usuário se será usada e para qual finalidade
        usar = input("Essa senha será usada agora? (s/n): ").strip().lower()
        if usar == 's':
            finalidade = input("Para qual finalidade essa senha será usada? ")
            self.senhas_usadas.append((senha, senha_mole.strip(), finalidade))
            self.senhas_nao_usadas.remove((senha, senha_mole.strip()))
            self.salvar_senhas_em_arquivo("usadas")
            print(f"Senha usada para: {finalidade}\n")
        else:
            print("Senha salva para uso futuro.\n")
        return senha, senha_mole

    def salvar_senhas_em_arquivo(self, tipo):
        # Salva as senhas no arquivo correspondente
        if tipo == "nao_usadas":
            with open('senhas_nao_usadas.txt', 'w') as arquivo:
                for senha, mole in self.senhas_nao_usadas:
                    arquivo.write(f"{senha} | {mole}\n")
        elif tipo == "usadas":
            with open('senhas_usadas.txt', 'w') as arquivo:
                for senha, mole, finalidade in self.senhas_usadas:
                    arquivo.write(f"{senha} | {mole} | {finalidade}\n")

    def senha(self):
        senha = input("Qual a senha? ")
        if senha == "Terra Livre":
            self.codificador()
        elif senha == "Terra em Chamas":
            self.decodificador()
        elif senha == "Terra ao vento":
            self.random()
        else:
            print("ACESSO NEGADO! INTRUSO DETECTADO")

if __name__ == "__main__":
    sistema = Mole()
    sistema.senha()
