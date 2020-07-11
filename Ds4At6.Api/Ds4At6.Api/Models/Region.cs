using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Region
    {
        public Region()
        {
            City = new HashSet<City>();
        }

        public int RegionId { get; set; }
        public string Name { get; set; }
        public int CountryId { get; set; }

        public virtual Country Country { get; set; }
        public virtual ICollection<City> City { get; set; }
    }
}
