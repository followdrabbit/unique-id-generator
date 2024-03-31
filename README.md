# Document Hash and Code Generator

Este projeto fornece uma ferramenta que gera um código único baseado no hash SHA-256 de um documento e permite verificar o hash de um documento a partir de um código fornecido. O código gerado é um identificador alfanumérico de 12 dígitos, separado por hífens, que pode ser revertido para confirmar a integridade do documento original.

## Funcionalidades

- **Geração de Código**: Gera um código único baseado no hash SHA-256 do conteúdo de um documento.
- **Verificação de Hash**: Verifica se um código fornecido corresponde ao hash SHA-256 de um documento.

## Como Usar

### Pré-requisitos

Para usar esta ferramenta, você precisa ter Python instalado em sua máquina.

### Executando o Script

1. Clone o repositório ou faça download do script `hash_code_generator.py`.
2. Abra o terminal ou prompt de comando.
3. Navegue até o diretório onde o script está localizado.
4. Execute o script usando Python:

Para gerar um código a partir de um documento:

```bash
python hash_code_generator.py <caminho_do_documento>
```

Para verificar um documento a partir de um código:

```bash
python hash_code_generator.py <caminho_do_documento> --code <codigo_unico>
```

### Exemplo de Uso

Para gerar um código para o arquivo documento.txt:

```bash
python hash_code_generator.py documento.txt
```

Se o documento tiver um hash SHA-256 válido, o script exibirá o hash e o código gerado.

Para verificar o código de um documento:

```bash
python hash_code_generator.py documento.txt --code ABCD-EFGH-IJKL
```

Se o código corresponder ao hash do documento, o script confirmará a correspondência.

## Sobre o Autor

- **Raphael de Carvalho Florencio**
- Cargo: Arquiteto de Segurança da Informação
- LinkedIn: [raphaelflorencio](https://linkedin.com/in/raphaelflorencio)

Sou apaixonado por desafios e sempre em busca de aprender coisas novas. Atualmente, estou focado em estudar Inteligência Artificial, visando não apenas melhorar os processos e sistemas de segurança, mas também buscar eficiência e inovação nas áreas de desenvolvimento. Meu interesse em pesquisa e desenvolvimento me motiva a fomentar mudanças culturais, contribuindo para o avanço tecnológico em segurança da informação.

## Contato

Para saber mais ou entrar em contato com Raphael, visite seu perfil no LinkedIn.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.