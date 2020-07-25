using Dapper;
using Ds4At6.Api.Models.ViewModels;
using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Configuration;
using System.Collections.Generic;
using System.Data;
using System.Linq;

namespace Ds4At6.Api.Helpers
{
    public class DataHelper : IDataHelper
    {
        private string ConnectionString;

        public DataHelper(IConfiguration configuration)
        {
            ConnectionString = configuration.GetConnectionString("DefaultConnection");
        }

        public List<CrimesByMaritalStatusViewModel> GetCrimesByMaritalStatus()
        {
            var procedure = "GetCrimesByMaritalStatus";

            using SqlConnection connection = new SqlConnection(ConnectionString);
            return connection.Query<CrimesByMaritalStatusViewModel>(procedure, null, commandType: CommandType.StoredProcedure).ToList();
        }

        public List<CrimesByRegionViewModel> GetCrimesByRegion()
        {
            var procedure = "GetCrimesByRegion";

            using SqlConnection connection = new SqlConnection(ConnectionString);
            return connection.Query<CrimesByRegionViewModel>(procedure, null, commandType: CommandType.StoredProcedure).ToList();
        }

        public List<CrimesByScholarshipViewModel> GetCrimesByScholarship()
        {
            var procedure = "GetCrimesByScholarship";

            using SqlConnection connection = new SqlConnection(ConnectionString);
            return connection.Query<CrimesByScholarshipViewModel>(procedure, null, commandType: CommandType.StoredProcedure).ToList();
        }
    }
}
