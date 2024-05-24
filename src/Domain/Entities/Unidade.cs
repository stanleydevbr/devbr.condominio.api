namespace Domain.Entities
{
    public class Unidade
    {
        public int Numero {get; set;}
        public string Ocupante {get; set;}
        public string Localizacao {get; set;}
        public string Descricao {get; set;}
        public decimal valorAluguel {get; set;}
        public int NumeroQuartos { get; set; }
        public int NumeroSalas { get; set; }
        public int NumeroVagasGaragem { get; set; }
        public int Andar { get; set; }
        public decimal ValorCondominio { get; set; } //talvez essa propriedade não seja adequada para essa classe 
        public DateTime DataDeChegadaAPropriedade {get; set;}
        public DateTime DataDeSaidaDaPropriedade {get; set;}







       


    }
}