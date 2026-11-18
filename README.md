# Ambiente de Desenvolvimento WordPress com Docker

Este projeto disponibiliza um ambiente completo de desenvolvimento para WordPress utilizando Docker Compose. Inclui a aplicação WordPress, base de dados MariaDB, gestão de base de dados via phpMyAdmin, ambiente de desenvolvimento web via VS Code Server, automação via WP-CLI e um utilitário Python para geração de chaves de segurança[cite: 1, 2].

---

## 🚀 Serviços Incluídos

* **WordPress**: Plataforma WordPress na versão mais recente, acessível na porta `8080`.
* **MariaDB**: Servidor de base de dados (versão LTS)[cite: 2], acessível na porta `8082`[cite: 3, 4].
* **phpMyAdmin**: Interface web para gestão da base de dados MariaDB[cite: 2], acessível na porta `8081`[cite: 3, 4].
* **Code-Server**: Instância do VS Code acessível via navegador[cite: 2], mapeada para os ficheiros do WordPress na porta `8083`[cite: 3, 4].
* **WP-CLI**: Utilitário de linha de comandos configurado para instalar automaticamente o idioma `pt_BR` e definir o fuso horário para `America/Fortaleza`[cite: 2].
* **Script Python (`chave_hex.py`)**: Ferramenta para gerar chaves aleatórias de 128 bits nos formatos Hexadecimal e Base64.

---

## 📁 Estrutura do Ficheiro `.env`

O projeto utiliza um ficheiro `.env` para gerir as variáveis de ambiente[cite: 3, 5]. As portas por omissão e os IPs estáticos da rede Docker são os seguintes[cite: 3, 4]:

| Serviço | Porta Externa | IP Estático na Rede |
| :--- | :--- | :--- |
| **WordPress** | `80`[cite: 3, 4] | `172.20.0.3`[cite: 3, 4] |
| **phpMyAdmin** | `8080`[cite: 3, 4] | `172.20.0.4`[cite: 3, 4] |
| **MariaDB** | `3306`[cite: 3, 4] | `172.20.0.2`[cite: 3, 4] |
| **Code-Server** | `8443`[cite: 3, 4] | `172.20.0.5`[cite: 3, 4] |

> **Nota:** Os dados persistentes do WordPress e do MariaDB são armazenados nos diretórios `wp_data/` e `db_data/`, respetivamente, os quais estão ignorados no controlo de versões[cite: 2, 5].

---

## 🛠️ Pré-requisitos

* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados na máquina.
* [Python 3](https://www.python.org/) (opcional, apenas se pretender executar o script de geração de chaves localmente)[cite: 1].

---

## ⚙️ Passo a Passo de Configuração

### 1. Clonar o Repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
