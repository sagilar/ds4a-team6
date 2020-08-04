using System.Collections.Generic;

namespace Ds4At6.Api.Models.ViewModels
{
    public class SurvivalResult
    {
        public string ClusterDescription { get; set; }

        public List<DataPoint> Propability { get; set; }
    }

    public class DataPoint
    {
        public decimal dia { get; set; }

        public double? prob { get; set; }
    }
}
