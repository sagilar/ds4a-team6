using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Country
    {
        public Country()
        {
            Region = new HashSet<Region>();
        }

        public int CountryId { get; set; }
        public string Name { get; set; }

        public virtual ICollection<Region> Region { get; set; }
    }
}
