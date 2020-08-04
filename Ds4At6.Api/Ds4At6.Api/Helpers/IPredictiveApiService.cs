using Ds4At6.Api.Models;
using Ds4At6.Api.Models.ApiRequests;
using Ds4At6.Api.Models.ViewModels;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Ds4At6.Api.Helpers
{
    public interface IPredictiveApiService
    {
        Task<string> GetClusterDescription(ClassifierRequest model);

        Task<int> GetClusterNumber(ClassifierRequest model);

        Task<List<DataPoint>> GetSurvivalStats(PredictionRequest model);
    }
}