namespace Domain.Entities
{
    public class Condomino
    {
        public int Id { get; set; }
        public string Nome { get; set; }
        public string Email { get; set; }
        public string Telefone { get; set; }
        public Unidade Unidade { get; set; }
        public bool StatusPagamento { get; set; }

    }
}