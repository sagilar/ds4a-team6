using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class Scholarship
    {
        public Scholarship()
        {
            Person = new HashSet<Person>();
        }

        public int ScholarshipId { get; set; }
        public string Name { get; set; }

        public virtual ICollection<Person> Person { get; set; }
    }
}
