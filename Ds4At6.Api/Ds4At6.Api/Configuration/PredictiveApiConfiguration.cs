using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Ds4At6.Api.Configuration
{

    public interface IPredictiveApiConfiguration
    {
        string AccessToken { get; set; }
        string BaseUrl { get; set; }
    }

    public class PredictiveApiConfiguration : IPredictiveApiConfiguration
    {
        public string AccessToken { get; set; }
        public string BaseUrl { get; set; }
    }

}


