# Exercícios do Módulo

## Encapsulamento

1. Crie uma classe chamada `Pessoa` com os atributos `nome` e `idade`. Utilize o encapsulamento para definir esses atributos como privados e crie métodos para acessá-los (getters) e modificá-los (setters).
2. Implemente uma classe `ContaBancaria` com os atributos `saldo` e `limite`. Utilize o encapsulamento para tornar esses atributos privados e forneça métodos para depositar e sacar dinheiro da conta, respeitando o limite.
3. Crie uma classe `Produto` com os atributos `nome`, `preco` e `desconto`. Utilize o encapsulamento para tornar o atributo `desconto` privado e crie um método para aplicar o desconto ao preço do produto.

## Herança

1. Crie uma classe base chamada `Animal` com o método `fazer_som()`. Em seguida, crie duas classes derivadas, como `Cachorro` e `Gato`, que herdam de `Animal` e implementam o método `fazer_som()` com sons diferentes para cada classe.
2. Implemente uma hierarquia de classes para um sistema de funcionários de uma empresa. Crie uma classe base `Funcionario` com atributos como `nome` e `salario`, e em seguida crie classes derivadas como `Gerente`, `Analista` e `Estagiario`, cada uma com atributos específicos e comportamentos adicionais.
3. Crie uma classe base `Forma`. Em seguida, crie classes derivadas como `Retangulo` e `Triangulo` que herdam de `Forma` e implementam seus próprios cálculos de área e perímetro.

## Polimorfismo

1. Crie uma função chamada `som_animal` que recebe um objeto `Animal` como parâmetro e chama o método `fazer_som()`. Chame essa função com objetos de diferentes classes derivadas e observe o comportamento polimórfico.
2. Implemente uma classe base `Veiculo` com o método `acelerar()`. Em seguida, crie classes derivadas como `Carro`, `Moto` e `Caminhao`, que herdam de `Veiculo` e implementam o método `acelerar()` de maneira diferente em cada classe.
3. Crie uma função chamada `calcular_area_total` que recebe uma lista de objetos `Forma` (da atividade de herança) e calcula a área total somando as áreas de cada forma. Chame essa função com diferentes objetos e verifique o comportamento polimórfico.

**Atividade combinando os conceitos:**
Crie uma classe chamada `Pessoa` com os atributos `nome` e `idade`. Utilize o encapsulamento para torná-los privados. Em seguida, crie uma classe `Aluno` que herda de `Pessoa` e adiciona o atributo `matricula`. Implemente métodos para acessar e modificar a matrícula. Por fim, crie uma função que recebe uma lista de objetos `Pessoa` (que podem ser tanto objetos `Pessoa` quanto objetos `Aluno`) e exibe o nome e a idade de cada pessoa, usando o polimorfismo para tratar os objetos de forma genérica.
