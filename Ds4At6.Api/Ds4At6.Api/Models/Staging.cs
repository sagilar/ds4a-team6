using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Staging
    {
        public string Internoen { get; set; }
        public string Delito { get; set; }
        public string Tentativa { get; set; }
        public string Agravado { get; set; }
        public string Calificado { get; set; }
        public string FechaIngreso { get; set; }
        public string FechaSalida { get; set; }
        public string FechaCaptura { get; set; }
        public string SituacionJuridica { get; set; }
        public string AnoNacimiento { get; set; }
        public double? Edad { get; set; }
        public string Genero { get; set; }
        public string EstadoCivil { get; set; }
        public string PaisInterno { get; set; }
        public string Departamento { get; set; }
        public string Ciudad { get; set; }
        public string Reincidente { get; set; }
        public string EstadoIngreso { get; set; }
        public string ActividadesTrabajo { get; set; }
        public string ActividadesEstudio { get; set; }
        public string ActividadesEnseñanza { get; set; }
        public string NivelEducativo { get; set; }
        public string HijosMenores { get; set; }
        public string CondicExpecional { get; set; }
        public string CodigoEstablecimiento { get; set; }
        public string Establecimiento { get; set; }
        public string DeptoEstablecimiento { get; set; }
        public string MpioEstablecimiento { get; set; }
        public string Regional { get; set; }
        public string Estado { get; set; }
        public string TituloDelito { get; set; }
        public string SubtituloDelito { get; set; }
    }
}
