using Ds4At6.Api.Configuration;
using Ds4At6.Api.Models;
using Ds4At6.Api.Models.ApiRequests;
using Ds4At6.Api.Models.ViewModels;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

namespace Ds4At6.Api.Helpers
{
    public class PredictiveApiService : IPredictiveApiService
    {
        private readonly HttpClient _httpClient;
        private readonly IPredictiveApiConfiguration apiConfiguration;

        public PredictiveApiService(HttpClient httpClient, IPredictiveApiConfiguration apiConfiguration)
        {
            _httpClient = httpClient;
            this.apiConfiguration = apiConfiguration;
        }

        public async Task<List<DataPoint>> GetSurvivalStats(PredictionRequest model)
        {

            try
            {
                var request = JsonConvert.SerializeObject(model);
                var content = new StringContent(request, Encoding.UTF8, "application/json");
                var controller = "survival";

                var url = $"{controller}";
                var response = await _httpClient.PostAsync(url, content);
                var answer = await response.Content.ReadAsStringAsync();
                if (!response.IsSuccessStatusCode)
                {
                    throw new Exception("No response form predictive API");
                }

                var obj = JsonConvert.DeserializeObject<List<DataPoint>>(answer);
                return obj;
            }
            catch (Exception ex)
            {
                throw new Exception("No response form predictive API " + ex.Message);
            }
        }

        public async Task<string> GetClusterDescription(ClassifierRequest model)
        {

            try
            {
                var request = JsonConvert.SerializeObject(model);
                var content = new StringContent(request, Encoding.UTF8, "application/json");
                var controller = "Classify";

                var url = $"{controller}";
                var response = await _httpClient.PostAsync(url, content);
                var answer = await response.Content.ReadAsStringAsync();
                if (!response.IsSuccessStatusCode)
                {
                    throw new Exception("No response form predictive API");
                }
                return answer;
                
            }
            catch (Exception ex)
            {
                throw new Exception("No response form predictive API " + ex.Message);
            }
        }

        public async Task<int> GetClusterNumber(ClassifierRequest model)
        {

            try
            {
                var request = JsonConvert.SerializeObject(model);
                var content = new StringContent(request, Encoding.UTF8, "application/json");
                var controller = "ClassifyNumber";

                var url = $"{controller}";
                var response = await _httpClient.PostAsync(url, content);
                var answer = await response.Content.ReadAsStringAsync();
                if (!response.IsSuccessStatusCode)
                {
                    throw new Exception("No response form predictive API");
                }

                var obj = JsonConvert.DeserializeObject<int>(answer);
                return obj;
            }
            catch (Exception ex)
            {
                throw new Exception("No response form predictive API " + ex.Message);
            }
        }
    }


}
