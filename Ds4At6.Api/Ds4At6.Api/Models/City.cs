using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class City
    {
        public City()
        {
            Person = new HashSet<Person>();
            Prison = new HashSet<Prison>();
        }

        public int CityId { get; set; }
        public int RegionId { get; set; }
        public string Name { get; set; }

        public virtual Region Region { get; set; }
        public virtual ICollection<Person> Person { get; set; }
        public virtual ICollection<Prison> Prison { get; set; }
    }
}
