using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Prison
    {
        public int PrisonId { get; set; }
        public string Name { get; set; }
        public int? CityId { get; set; }
        public int RegionalId { get; set; }

        public virtual City City { get; set; }
        public virtual Regional Regional { get; set; }
    }
}
