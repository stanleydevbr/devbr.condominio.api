## Condômino
Como um administrador do condomínio,
Eu quero acessar e gerenciar informações sobre cada condômino,
Incluindo detalhes de contato, a unidade que ocupam e o status de pagamento das taxas do condomínio,
Para que eu possa manter um registro atualizado e preciso de todos os condôminos e suas obrigações financeiras.

Cenários de Aceitação:

1. Dado que estou na página de detalhes do condômino,
   Quando eu seleciono um condômino específico,
   Então eu devo ver as informações de contato, a unidade que ocupam e o status de pagamento das taxas do condomínio.

2. Dado que estou na página de detalhes do condômino,
   Quando eu atualizo as informações de um condômino,
   Então as informações atualizadas devem ser salvas e exibidas corretamente.

3. Dado que estou na página de detalhes do condômino,
   Quando eu registro um pagamento de taxa de condomínio,
   Então o status de pagamento do condômino deve ser atualizado para refletir o pagamento.

### Modelo de entidade

```csharp
public class Condomino
{
    public int Id { get; set; }
    public string Nome { get; set; }
    public string Email { get; set; }
    public string Telefone { get; set; }
    public Unidade Unidade { get; set; }
    public bool StatusPagamento { get; set; }

    // Métodos adicionais conforme necessário
}
```   

Neste modelo:

Id é a chave primária.
Nome, Email e Telefone são as informações de contato do condômino.
Unidade é uma referência à unidade que o condômino ocupa. Isso pressupõe que você tenha uma classe Unidade separada.
StatusPagamento é um booleano que indica se o condômino está em dia com as taxas do condomínio. True indica que o pagamento está em dia, e false indica que o condômino está inadimplente.