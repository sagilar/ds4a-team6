using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class MaritalStatus
    {
        public MaritalStatus()
        {
            Person = new HashSet<Person>();
        }

        public int MaritalStatusId { get; set; }
        public string Name { get; set; }

        public virtual ICollection<Person> Person { get; set; }
    }
}
