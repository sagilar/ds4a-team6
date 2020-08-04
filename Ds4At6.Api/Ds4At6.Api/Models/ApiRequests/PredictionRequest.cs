using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Models.ApiRequests
{
    public class PredictionRequest
    {
        public int age { get; set; }
        public int education_level { get; set; }

        public int DidStudies { get; set; }

        public int DidTeaching { get; set; }

        public int Cases { get; set; }
        public int DaysInPrison { get; set; }
        public double gnic { get; set; }

        public double Population { get; set; }
        public int InJail { get; set; }

        public int cluster { get; set; }
    }
}
