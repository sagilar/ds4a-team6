using System;
using System.Collections.Generic;

namespace Ds4At6.Api.Models
{
    public partial class SpecialCondition
    {
        public SpecialCondition()
        {
            PersonCondition = new HashSet<PersonCondition>();
        }

        public int SpecialConditionId { get; set; }
        public string Condition { get; set; }

        public virtual ICollection<PersonCondition> PersonCondition { get; set; }
    }
}
