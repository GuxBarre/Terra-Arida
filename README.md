# Terra-Arida

O projeto **"Terra Arida"** visa criar um codificador e decodificador de **Código Morse**, com inspirações do mundo de "Avatar, a lenda de Aang". O sistema permite não apenas a conversão de mensagens para o Código Morse e vice-versa, mas também gera senhas seguras, adicionando um toque criativo e prático ao uso dessa linguagem universal.

## 🎯 Objetivo

O sistema desenvolvido tem os seguintes objetivos:

- **Codificação de mensagens:** Converte texto comum para Código Morse.
- **Decodificação de mensagens:** Interpreta sequências de Código Morse e as transforma em texto.
- **Geração de senhas aleatórias:** Cria senhas seguras e únicas com letras, números e caracteres especiais.
- **Conversão de senhas para Código Morse:** Gera a versão em Morse da senha criada.
- **Organização de senhas:** Permite salvar senhas em categorias de "usadas" e "não usadas".
- **Controle de acesso:** Simula autenticação através de frases de comando, como "Terra Livre" e "Terra em Chamas", para acionar funcionalidades específicas.

## 🛠️ Funcionalidades

1. **Codificador:** Converte texto para Código Morse.
2. **Decodificador:** Converte Código Morse de volta para texto.
3. **Gerador de Senhas:** Cria senhas seguras e gera suas versões em Código Morse.
4. **Armazenamento de Senhas:** Salva senhas em arquivos de texto e organiza entre usadas e não usadas.
5. **Sistema de Autenticação:** Usa frases de comando como "Terra Livre" para acionar as funcionalidades do sistema.

## 🔧 Ferramentas Utilizadas

- **Linguagem:** Python 3
- **Módulos:** 
  - `random` para gerar senhas aleatórias.
  - `string` para manipulação de caracteres alfanuméricos.
- **Manipulação de Arquivos:** Senhas são salvas em arquivos de texto para persistência dos dados.

## 📚 Aprendizado

Durante o desenvolvimento deste projeto, os seguintes conceitos foram explorados:

- Lógica de programação e manipulação de strings.
- Estruturação de classes e métodos em Python.
- Organização de dados e persistência em arquivos de texto.

## 🌟 Inspirado por Avatar

Assim como os elementos de **Avatar** interagem em harmonia, o sistema "Terra Arida" une criatividade e segurança para comunicação e gerenciamento de senhas, simbolizando a interação entre os mundos digital e real. As funcionalidades do sistema refletem as diferentes facetas do universo de "Avatar", utilizando código Morse como a linguagem que conecta as pessoas.

## 💡 Como Usar

1. **Executar o script Python**: Após baixar o projeto, basta executar o arquivo Python.
2. **Autenticação**: Quando o sistema solicitar a senha, use uma das frases de comando abaixo para acessar as funcionalidades:
   - **"Terra Livre"**: Ativa o codificador (para converter texto para Código Morse).
   - **"Terra em Chamas"**: Ativa o decodificador (para converter Código Morse de volta para texto).
   - **"Terra ao Vento"**: Ativa o gerador de senhas (para criar e gerar senhas seguras).
3. **Senhas Geradas**: As senhas geradas podem ser salvas para uso futuro, e são armazenadas em arquivos de texto.

## 📋 Exemplo de Uso

1. **Codificador:**
   - Digite a frase para ser codificada.
   - A frase será convertida para o formato Código Morse.

2. **Decodificador:**
   - Digite o Código Morse a ser decodificado.
   - O Código Morse será transformado de volta em texto.

3. **Gerador de Senhas:**
   - O sistema gera uma senha aleatória que é segura, com letras maiúsculas, números e caracteres especiais.
   - A senha é convertida para Código Morse e salva para uso futuro.

## 💾 Arquivos de Senhas

- **senhas_nao_usadas.txt**: Armazena senhas que ainda não foram usadas.
- **senhas_usadas.txt**: Armazena senhas que já foram utilizadas, com suas respectivas finalidades.

## 🔑 Exemplo de Senha Gerada

Uma senha gerada pode ser algo como:
