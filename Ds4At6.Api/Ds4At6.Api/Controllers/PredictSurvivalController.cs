using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.Xml;
using System.Threading.Tasks;
using Ds4At6.Api.Helpers;
using Ds4At6.Api.Models;
using Ds4At6.Api.Models.ApiRequests;
using Ds4At6.Api.Models.ViewModels;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace Ds4At6.Api.Controllers
{
    [Route("api/prediction")]
    [ApiController]
    public class PredictSurvivalController : ControllerBase
    {
        private readonly IPredictiveApiService apiService;
        private readonly DataContext dataContext;
        private readonly IDataHelper dataHelper;

        public PredictSurvivalController(IPredictiveApiService apiService,
            DataContext dataContext,
            IDataHelper dataHelper)
        {
            this.apiService = apiService;
            this.dataContext = dataContext;
            this.dataHelper = dataHelper;
        }

        [HttpGet]
        public async Task<ActionResult<SurvivalResult>> GetAsync([FromQuery] int scholarship, int crime, int inJail, int work, int study, int gender,
            int age, int teaching, int cases, int daysInPrison, int region)
        {
            var Crime = this.dataHelper.GetCrime(crime);
            var Region = this.dataHelper.GetRegion(region);
            var Result = new SurvivalResult();
            var EducationLevel = dataContext.Scholarship.Where(s => s.ScholarshipId == scholarship).FirstOrDefault().Level;

            var ObjectToClassify = new ClassifierRequest()
            {
                education_level=EducationLevel,
                weight= Crime.Weight,
                InJail=inJail,
                DidWork=work,
                DidStudies=study,
                IsMale= gender== 6 ? 1 : 0
            };

            var ObjectToPredict = new PredictionRequest()
            {
                age = age,
                education_level = EducationLevel,
                DidStudies=study,
                DidTeaching=teaching,
                Cases=cases,
                DaysInPrison=daysInPrison,
                gnic=Region.Gnic,
                Population=Region.Population,
                InJail = inJail
            };

            var Cluster = await this.apiService.GetClusterDescription(ObjectToClassify);
            var ClusterNumber = await this.apiService.GetClusterNumber(ObjectToClassify);
            ObjectToPredict.cluster = ClusterNumber;

            var Prediction = await this.apiService.GetSurvivalStats(ObjectToPredict);
            Result.ClusterDescription = Cluster;
            Result.Propability = Prediction;
            
            return Ok(Result);
        }

       
    }
}
